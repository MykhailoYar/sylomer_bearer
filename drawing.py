import pandas

from draw import draw
from vibromat_super import vibromat


def drawing(all, directory):
    s28 = []
    s42 = []
    s55 = []
    s110 = []
    s220 = []
    s850 = []
    s1200 = []
    for a in all:
        if int(a[9]) == 28: s28.append(a[8::])
        if int(a[9]) == 42: s42.append(a[8::])
        if int(a[9]) == 55: s55.append(a[8::])
        if int(a[9]) == 110: s110.append(a[8::])
        if int(a[9]) == 220: s220.append(a[8::])
        if int(a[9]) == 850: s850.append(a[8::])
        if int(a[9]) == 1200: s1200.append(a[8::])
    s28 = pandas.DataFrame(s28, columns=['-1', '0', '1', '2', '3'])
    s28 = s28.sort_values(by=['2'], ascending=False)
    s42 = pandas.DataFrame(s42, columns=['-1', '0', '1', '2', '3'])
    s42 = s42.sort_values(by=['2'], ascending=False)
    s55 = pandas.DataFrame(s55, columns=['-1', '0', '1', '2', '3'])
    s55 = s55.sort_values(by=['2'], ascending=False)
    s110 = pandas.DataFrame(s110, columns=['-1', '0', '1', '2', '3'])
    s110 = s110.sort_values(by=['2'], ascending=False)
    s220 = pandas.DataFrame(s220, columns=['-1', '0', '1', '2', '3'])
    s220 = s220.sort_values(by=['2'], ascending=False)
    s850 = pandas.DataFrame(s850, columns=['-1', '0', '1', '2', '3'])
    s850 = s850.sort_values(by=['2'], ascending=False)
    s1200 = pandas.DataFrame(s1200, columns=['-1', '0', '1', '2', '3'])
    s1200 = s1200.sort_values(by=['2'], ascending=False)

    alls = [s28, s42, s55, s110, s220, s850, s1200]
    number = 1
    out = []
    general = []
    for s in alls:
        s = s.values
        if len(s) == 0:
            None
        else:
            for i in range(0, len(s)):
                if i == 0:
                    coord = [0, 0]
                    coor = []
                    q = 0
                    plus = 0
                    names = '\n' + str(int(s[i][3])) + ' x ' + str(int(s[i][4])) + ' x ' + str(
                        int(s[i][0])) + ' - ' + str(int(s[i][2])) + ' шт'
                    [coor, general] = vibromat(s[i][4], s[i][3], s[i][0], int(s[i][2]), int(s[i][1]), coord, coor)
                else:
                    if s[i][4] == s[i - 1][4]:
                        coord = [coor[len(coor) - 1][1] + s[i - 1][4],
                                 coor[len(coor) - 1][0] / s[i - 1][3]]  # coor[len(coor)-1][0]/i[3]
                        a = vibromat(s[i][4], s[i][3], s[i][0], int(s[i][2]), int(s[i][1]), coord, coor)
                        coor = a[0]
                        general += a[1]
                        names += '\n' + str(int(s[i][3])) + ' x ' + str(int(s[i][4])) + ' x ' + str(
                            int(s[i][0])) + ' - ' + str(int(s[i][2])) + ' шт'
                    if s[i][4] != s[i - 1][4]:
                        # name ='#'+str(number)+' SR'+str(int(s[i][1]))+' '+str(int(s[i-1][3]))+'x'+str(int(s[i-1][4]))
                        name = '#' + str(number)
                        # names += '\n' + str(int(s[i-1][3])) + ' x ' + str(int(s[i-1][4])) + ' x ' + str(int(s[i-1][0])) + ' - ' + str(int(s[i-1][2])) + ' шт'
                        names = '\n' + str(int(s[i][3])) + ' x ' + str(int(s[i][4])) + ' x ' + str(
                            int(s[i][0])) + ' - ' + str(int(s[i][2])) + ' шт'
                        last = draw(coor, 1500, 1200, 0, name, q, plus, str(int(s[i][1])), number, general, names,
                                    directory)
                        general = []
                        number += 1
                        q = 1
                        if s[i][3] == s[i - 1][3]:
                            coord = [coor[len(coor) - 1][1] + s[i - 1][4], 0]
                            plus += last - s[i][3]
                        else:
                            ratio = s[i - 1][3] / s[i][3] - s[i - 1][3] % s[i][3]
                            coord = [coor[len(coor) - 1][1] + s[i - 1][4], 0]  # coor[len(coor)-1][0]/i[3]
                            plus += last
                        coor = []
                        a = vibromat(s[i][4], s[i][3], s[i][0], int(s[i][2]), int(s[i][1]), coord, coor, ratio)
                        ratio = 0
                        coor = a[0]
                        general += a[1]
                        if i == len(s) - 1:
                            names += '\n' + str(int(s[i][3])) + ' x ' + str(int(s[i][4])) + ' x ' + str(
                                int(s[i][0])) + ' - ' + str(int(s[i][2])) + ' шт'
                            # name ='#'+str(number)+' SR'+str(int(round(s[i][1],0)))+' '+str(int(round(s[i][3],0)))+'x'+str(int(round(s[i][4],0)))
                            name = '#' + str(number)
                            last = draw(coor, 1500, 1200, 0, name, q, plus, str(int(s[i][1])), number, general, names,
                                        directory)
                            general = []
                            names = ' '
                            plus += last
                            number += 1
            if q == 0:
                # name ='#'+str(number)+' SR' + str(int(round(s[i][1],0))) + ' ' + str(int(round(s[i - 1][3],0))) + 'x' + str(int(round(s[i - 1][4],0)))
                name = '#' + str(number)
                # names += '\n' + str(int(s[i][3])) + ' x ' + str(int(s[i][4])) + ' x ' + str(int(s[i][0])) + ' - ' + str(int(s[i][2])) + ' шт'
                last = draw(coor, 1500, 1200, 0, name, q, plus, str(int(s[i][1])), number, general, names, directory)
                q = 1
                plus += last
                general = []
                names = ' '
                number += 1
            out.append(['SR' + str(int(s[i][1])) + ', п.м', plus / 1000])
    return [out, number]
