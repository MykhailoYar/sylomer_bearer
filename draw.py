import tkinter as tk

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle as rc

from uniquefunc import unique


def draw(coor, side, side2, rent, xxx, qz, plus, text, number, strip, names, directory):
    root = tk.Tk()
    p1 = root.winfo_screenwidth()
    p2 = root.winfo_screenheight()
    fig = plt.figure(figsize=(p1 / 96, p2 / 96))
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
    y.append(last + plus)  # межа матеріалу
    y.append(plus)  # правий край
    y.append(stop + plus)  # лівий край
    x = [i - plus for i in y]

    plt.xticks(sorted(list(set(x))), sorted(list(set(y))))
    plt.title('Розкладка матеріалу Sylomer SR' + text + ' товщиною 25 мм' \
              + '\nЛист #' + str(number), fontsize=14)

    u = unique(strip)
    text = 'Кількість смуг шириною ' + str(coor[0][4]) + ' мм: '
    lt = [len(text)]
    for i in u:
        # text+='\n'+'                                    '\
        #       +i+' x '+str(s[1])+' - ' + str(u.get(i))+';'
        text += '  ' + i + ' - ' + str(u.get(i)) + ';'
        if len(text) - lt[-1] > stop / 50:
            # text+='\n '
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
    #     text+='\n Залишок:'+str(int(rent))+' мм'
    # name_file = 'SR'+str(s[4])+' '+str(s[0])+' x '+str(s[1])\
    #           +' x '+str(s[2])+' мм '+str(s[3]) + ' шт'
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

    # text='Кількість смуг'
    # lt=[len(text)]
    # for i in u:
    #    # text+='\n'+'                                    '\
    #     #       +i+' x '+str(s[1])+' - ' + str(u.get(i))+';'
    #     text +='  '+i+' - ' + str(u.get(i))+';'
    #     if len(text)-lt[-1]>stop/50:
    #         text+='\n '
    #         lt.append(len(text))
    #
    # print(text)
    plt.xlabel(text + names, fontsize=14)
    # plt.show()

    plt.savefig(directory + xxx + '.pdf', papertype='a4', \
                orientation=orient)
    # plt.close()
    return last
