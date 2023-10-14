import numpy
import pandas
import math
import re
from Static import measure as ms
from Sylomer2 import Sylomer as sr
import tkinter as tk
from tkinter import filedialog
from drawing import drawing
import PyPDF2

def start(l1,l2,mass,dim_sr,bh,energy,sylomer_type,\
      thickness,numbers,price,from_file):

    file = 'Load-Factor.txt'

    length = max(l1, l2)
    width = min(l1, l2)
    inform = sr(length, width, dim_sr, bh,numbers)
    out = numpy.empty((0, 9), dtype=int)
    for i in inform:
        number = i[0] * i[1]
        dim = i[2:len(i) + 1]
        numbers=i[0:2]
        for j in dim:
            k = ms(j, j, number, mass, energy,thickness,file,\
                   price,sylomer_type,numbers)
            k2 = ms(j, width, i[0], mass, energy,thickness,file,\
                    price,sylomer_type,numbers)
            k = numpy.array(k+k2 )
            for q in k:
                out = numpy.vstack([out, q])
    try:
        out=numpy.unique(out, axis=0)
        x = numpy.array([[i for i in range(1, out.shape[0] + 1)]])

        out = out[out[:, 5].argsort()]
        out = out[::-1]
        out=numpy.concatenate((out, x.T), axis=1)

        out = out[out[:, 8].argsort()]
        out = out[::-1]
        out = numpy.concatenate((out, x.T), axis=1)

        y= numpy.array([[ (i+j)/2 for i,j in out[:,9:11] ]])
        out = numpy.concatenate((out, y.T), axis=1)
        out = out[out[:, 11].argsort()]

        # print(y)
        d2 = pandas.DataFrame({'SR': out[:, 0],'Quantity': out[:, 1],\
                                'Length':out[:,2],'Width':out[:,3],\
                                'Thickness':out[:,4],\
                               'Capacity': out[:, 5], 'Rows': out[:, 6],\
                               'Columns':out[:,7],'Price':out[:,8],\
                               # })
                               '#1':out[:,9],'#2':out[:,10],'#3':out[:,11]})
        d2 = d2.sort_values(by=['#3'])
        # ascending = False
        pandas.set_option('display.expand_frame_repr', False)

        print(d2)
        num= int((input('Номер рішення :')))
        des=d2.values
        from_file[9:13]=des[num][0:4]
        from_file[8]=des[num][4]
        #des=numpy.array( [ des[0], des[1], des[2],des[3] ])
        print(from_file)
    except ValueError:
        from_file = from_file[0:9]

    return from_file

def start2(dim_sr,bh,energy,sylomer_type,\
    numbers,price):

    root = tk.Tk()
    root.update()
    root.filename = filedialog.askopenfilenames(initialdir='C:/Users/Acoustic Group/Desktop', title='Оберіть шаблон для заповнення')
    root.destroy()
    df = pandas.read_excel(list(root.filename)[0])

    lis = list(root.filename)[0]
    out = re.split(r'/?', lis)
    print(out)
    directory = ''
    for i in out[0:-1]:
        directory+= i + '/'
    print(directory)



    print(list(root.filename)[0])

    z = df.values
    [x,y]=numpy.shape(z)
    y2=y
    all=[]
    for from_file in z:
        if math.isnan(from_file[3])==False:
            if numpy.shape(from_file)!=(9,) and math.isnan(from_file[10])==True:
                print(from_file)

                print('\n' + from_file[0] + ' Габарити:' + str(from_file[1]) + ' x ' + str(from_file[2]))
                l1 = from_file[1]
                l2 = from_file[2]
                thickness = [from_file[8]]
                try:
                    b = re.split('\W+', thickness[0])
                    thickness = [int(i) for i in b]
                except TypeError:
                    thickness = [from_file[8]]
                mass = from_file[7]
                from_file[6] = round(from_file[6] * 100, 0) / 100
                from_file = start(l1, l2, mass, dim_sr, bh, energy, sylomer_type, \
                                   thickness, numbers, price, from_file)

            if numpy.shape(from_file)==(9,):
                from_file=numpy.append(from_file,numpy.array([0,0,0,0]))
                print(from_file)

                print('\n'+ from_file[0]+' Габарити:'+str(from_file[1])+' x '+str(from_file[2]))
                l1=from_file[1]
                l2=from_file[2]
                thickness =[from_file[8]]
                try:
                    b = re.split('\W+', thickness[0])
                    thickness = [int(i) for i in b]
                except TypeError:
                    thickness = [from_file[8]]
                mass = from_file[7]
                from_file[6]=round(from_file[6]*100,0)/100
                from_file=start(l1, l2, mass, dim_sr, bh, energy, sylomer_type, \
                      thickness, numbers, price,from_file)
            all.append(from_file)

            if math.isnan(from_file[10])==True:
                y2-=1
    if y2==y:
        Out=drawing(all,directory)
        out=Out[0]
        number = Out[1]
        pdf_merger = PyPDF2.PdfFileMerger()

        for i in range(1,number):
            with open(directory+'#'+str(i)+'.pdf', 'rb') as f:
                reader = PyPDF2.PdfFileReader(f)
                pdf_merger.append(fileobj=f)
        # writing combined pdf to output pdf file
        with open(directory+'Розкладка.pdf', 'wb') as f:
            pdf_merger.write(f)

        print('here')
        all.append(math.nan for i in range(0, y))
        all=all+out

    dfc=list(df.columns)
    if len(dfc)==9:  dfc=dfc+['Sylomer SR', 'Кількість опор' ,'Ширина, мм', 'Довжина, мм']
    df = pandas.DataFrame(all,columns = dfc)

    root = tk.Tk()
    root.update()
    root.filename = filedialog.asksaveasfilename(initialdir=directory, title="Збереження заповненого шаблону",
                                                 defaultextension = '.xlsx')

    root.destroy()

    print(root.filename)

    df.to_excel(root.filename,index=False)





