import PyPDF2
import math
import numpy
import os
import pandas
import re

from calculation.static import measure as ms
from drawing.drawing import drawing
import tkinter as tk
from tkinter import filedialog

def sylomer(length, width, dim_sr, boundary, numbers):

    x = [i for i in range(50, 1, -1)]   # max number per side
    boundary_low, boundary_high = boundary[0], boundary[1]
    dim_sr2 = []

    for i in dim_sr:
        d1 = [j for j in range(i, 11 * i, i)]
        dim_sr2 = dim_sr2 + d1

    dim_sr, out, inform = sorted(set(dim_sr2)), {}, []
    for i in x:
        for j in x:
            d = [i, j]
            mark = round(j / i, 2)
            if mark < 1:
                out_dim = f'{i} x {j}'
                for f in dim_sr:
                    try:
                        gap_l = (length - i * f) / (i - 1)
                        gap_w = (width - j * f) / (j - 1)
                        if (gap_l < boundary_high and gap_l >= boundary_low) \
                                and \
                                (gap_w < boundary_high and gap_w >= boundary_low):
                            d.append(f)
                    except ZeroDivisionError:
                        None
                if len(d) > 2 and i * j <= numbers:
                    out[out_dim] = d
                    inform.append(d)
    return inform


def selection(dims, mass, dim_sr, all_distance, energy, sylomer_type, thickness, numbers, price, from_file):
    """
    Select the best configuration
    :param dims: list of dimensions, mm
    :param mass: total mass, kg
    :param dim_sr: cutting step of material
    :param all_distance: min and max allowed distance between bearings, mm
    :param energy: min and max power of bearing, %
    :param sylomer_type: list of SR marks
    :param thickness: list of thicknesses in mm
    :param numbers: max possible numbers of bearings
    :param price: current price euro/m2
    :param from_file: input data
    :return: extended from file with selected configuration
    """

    length, width = max(dims), min(dims)
    inform = sylomer(length, width, dim_sr, all_distance, numbers)
    out = numpy.empty((0, 9), dtype=int)
    for i in inform:
        number = i[0] * i[1]
        dim = i[2:len(i) + 1]
        numbers = i[0:2]
        for j in dim:
            # square bearing
            k = ms(j, j, number, mass, energy, thickness, price, sylomer_type, numbers)
            # rectangular bearing
            k2 = ms(j, width, i[0], mass, energy, thickness, price, sylomer_type, numbers)
            k = numpy.array(k + k2)
            for q in k:
                out = numpy.vstack([out, q])
    try:
        out = numpy.unique(out, axis=0)
        x = numpy.array([[i for i in range(1, out.shape[0] + 1)]])

        out = out[out[:, 5].argsort()]
        out = out[::-1]
        out = numpy.concatenate((out, x.T), axis=1)

        out = out[out[:, 8].argsort()]
        out = out[::-1]
        out = numpy.concatenate((out, x.T), axis=1)

        y = numpy.array([[(i + j) / 2 for i, j in out[:, 9:11]]])
        out = numpy.concatenate((out, y.T), axis=1)
        out = out[out[:, 11].argsort()]

        d2 = pandas.DataFrame({'SR': out[:, 0], 'Quantity': out[:, 1], 'Length': out[:, 2], 'Width': out[:, 3],
                               'Thickness': out[:, 4], 'Capacity': out[:, 5], 'Rows': out[:, 6], 'Columns': out[:, 7],
                               'Price': out[:, 8], 'Per capacity': out[:, 9], 'Per price': out[:, 10],
                               'Combined rank': out[:, 11]})

        d2 = d2.sort_values(by=['Combined rank'])
        pandas.set_option('display.expand_frame_repr', False)

        print(d2)
        num = int((input('Number of configuration :')))
        des = d2.values
        from_file[9:13] = des[num][0:4]
        from_file[8] = des[num][4]
    except ValueError:
        from_file = from_file[0:9]

    return from_file


def comparison_table(dim_sr, all_distance, energy, sylomer_type, numbers, price):
    """
    Prepare comparison table
    :param dim_sr: cutting step of material
    :param all_distance: min and max allowed distance between bearings, mm
    :param energy: min and max power of bearing, %
    :param sylomer_type: list of SR marks
    :param numbers: max possible numbers of bearings
    :param price: current price euro/m2
    :return: file with selected configuration
    """

    # select and read file with data and convert it to DataFrame
    root = tk.Tk()
    root.update()
    root.filename = filedialog.askopenfilenames(initialdir='C:/Users/Acoustic Group/Desktop',
                                                title='Select the Excel with input data')
    root.destroy()
    file_location = root.filename[0]
    df = pandas.read_excel(file_location)
    directory = os.path.dirname(file_location)

    # prepare for calculations
    input_data = df.values
    data_columns = input_data.shape[1]
    y2 = data_columns
    all = list()

    for data_line in input_data:

        # print units name and dimensions
        print('{source_name}, overall dimensions: {length}x{width} mm'.format(source_name=data_line[0],
                                                                              length=data_line[1],
                                                                              width=data_line[2]))
        # match variables and input data
        dims, mass, thickness = data_line[1:3], data_line[7], [float(x.strip()) for x in str(data_line[8]).split(',')]
        # round mass ratio
        data_line[6] = round(data_line[6], 2)

        # if not enough input data or configuration of vibration insulation material were done before
        if numpy.shape(data_line) != (9, ) and math.isnan(data_line[10]):
            data_line = selection(dims, mass, dim_sr, all_distance, energy, sylomer_type, thickness, numbers, price,
                              data_line)

        # run if no selected configuration were selected before
        if numpy.shape(data_line) == (9, ):
            data_line = numpy.append(data_line, numpy.array([0, 0, 0, 0]))
            data_line = selection(dims, mass, dim_sr, all_distance, energy, sylomer_type, thickness, numbers, price,
                              data_line)

        all.append(data_line)

        if math.isnan(data_line[10]) == True:
            y2 -= 1

    if y2 == data_columns:

        # drawing Placement of the material.pdf
        # Out = drawing(all, directory)
        # out = Out[0]
        # number = Out[1]
        # pdf_merger = PyPDF2.PdfFileMerger()
        #
        # for i in range(1, number):
        #     with open(directory + '#' + str(i) + '.pdf', 'rb') as f:
        #         _ = PyPDF2.PdfFileReader(f)
        #         pdf_merger.append(fileobj=f)
        # # writing combined pdf to output pdf file
        # with open(directory + 'Placement of the material.pdf', 'wb') as f:
        #     pdf_merger.write(f)

        all.append(math.nan for _ in range(0, data_columns))
        # all = all + out

    dfc = list(df.columns)
    if len(dfc) == 9:
        dfc = dfc + ['Sylomer SR', 'Amount of bearings', 'Width, mm', 'Length, mm']
    df = pandas.DataFrame(all, columns=dfc)

    root = tk.Tk()
    root.update()
    root.filename = filedialog.asksaveasfilename(initialdir=directory, title="Saving",
                                                 defaultextension='.xlsx')
    root.destroy()
    df.to_excel(root.filename, index=False)
