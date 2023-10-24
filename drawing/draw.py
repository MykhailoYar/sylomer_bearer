import tkinter as tk

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle as rc


def unique(l_gen):
    l_gen = sorted(l_gen)
    n, q, out = 0, [1], {}
    for i in l_gen[1::]:
        if i == l_gen[n]:
            q[-1] += 1
            out[str(i)] = q[-1]
        else:
            q.append(1)
        n += 1
    return out


def draw(coor, side, side2, rent, xxx, plus, text, number, strip, names, directory):

    root = tk.Tk()
    # p1 = root.winfo_screenwidth()
    # p2 = root.winfo_screenheight()
    # fig = plt.figure(figsize=(p1 / 96, p2 / 96))
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, aspect='equal')
    size = len(coor) - 1
    j = side2
    while coor[size][0] > j:
        j += side2
    stop = j
    last = coor[size][0] + coor[size][4]
    p = rc((0, 0), last, side + coor[size][4], fill=False)
    ax.add_patch(p)

    plt.xlim((0, stop + coor[size][4]))
    plt.ylim((0, side))

    y = []
    x2 = [i for i in range(0, 101 * side2, side2)]
    for i in x2:
        if plus <= i <= plus + stop:
            if abs(plus - i) > 100 and abs(last + plus - i) > 100:
                y.append(i)
    y.append(last + plus)  # edge of the material
    y.append(plus)  # right edge
    y.append(stop + plus)  # left edge
    x = [i - plus for i in y]

    plt.xticks(sorted(list(set(x))), sorted(list(set(y))))
    plt.title('Розкладка матеріалу Sylomer SR' + text + ' товщиною 25 мм' \
              + '\nЛист #' + str(number), fontsize=14)

    u = unique(strip)
    text = 'Кількість смуг шириною ' + str(coor[0][4]) + ' мм: '
    lt = [len(text)]
    for i in u:
        text += '  ' + i + ' - ' + str(u.get(i)) + ';'
        if len(text) - lt[-1] > stop / 50:
            lt.append(len(text))
    general = []
    for i in coor:
        general.append(i[2] + i[1])
        if i[3] % 2 != 0:
            color1 = 'r'
        else:
            color1 = 'g'
        p = rc((i[0], i[1]), i[4], i[2], fill=True, facecolor=color1, edgecolor='black')
        ax.add_patch(p)
    if rent != 0:
        p = rc((i[0], i[1] + i[2]), i[4], rent, fill=True, facecolor='gray', edgecolor='black')
        ax.add_patch(p)
    if stop / side < 297 / 210:
        orient = 'portrait'
    else:
        orient = 'landscape'

    l = list(set(general))
    l.append(0)
    l.append(side)
    l = sorted(list(set(l)))

    plt.xlim((0, stop + coor[size][4]))
    plt.ylim((0, side))
    plt.yticks(l)

    plt.xlabel(text + names, fontsize=14)

    plt.savefig(directory + xxx + '.pdf', papertype='a4', \
                orientation=orient)

    return last
