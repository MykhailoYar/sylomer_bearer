# версія №1 - залежність довжини опори від напрямку порізки
# перенести розкладку до кількості типів опор?
# import matplotlib

def vibromat(l0, w, h, n, stype, coord, coor, ratio=0):
    s = coord[0]
    zero = s
    cor = coord[1]

    # # довжина опори в плані, мм
    # l0= 200
    # # ширина опори в плані, мм
    # w = 200
    # # висота опори в плані, мм
    # h = 50
    # # кількість опор
    # n = 12
    #
    # stype = 42

    sizes = [l0, w, h, n, stype]

    side = 1500
    if l0 == w:
        side = side - side % w

    # if side==1200:
    #     side2 = 1500
    # else:
    #     side2 = 1200

    # print('Сторона порізки : ', side)

    ls = l0 * h / 25

    # print('----')
    strip = round(ls / side)

    l_gen = []
    general = []
    for q in range(0, n):  # цикл по кількості опор
        lf = []
        while sum(lf) != ls:
            l0 = ls * 25 / h
            while l0 != 0:
                if s == 0 and l0 >= side:
                    lf.append(int(side))
                    general.append(int(side))
                    coor.append([cor * w, s, side, q, w])
                    cor += 1
                    if cor < ratio:
                        s = zero
                    l0 -= side
                if s == 0 and l0 < side:
                    if l0 != 0:
                        lf.append(int(l0))
                        general.append(int(l0))
                        coor.append([cor * w, s, l0, q, w])
                    s = l0
                    l0 = ls * 25 / h
                    break
                if s != 0:
                    if l0 > side - s:
                        l0 -= side - s
                        if side - s != 0:
                            lf.append(int(side - s))
                            general.append(int(side - s))
                        coor.append([cor * w, s, side - s, q, w])
                        cor += 1
                        s = 0
                        if cor < ratio:
                            s = zero
                    else:
                        if l0 != 0:
                            lf.append(int(l0))
                            general.append(int(l0))
                        coor.append([cor * w, s, l0, q, w])
                        s += l0
                        l0 = 0
        # print(q+1, ' ',lf, '  ' , sum(lf))
        l_gen.append(sorted(lf))
    if s == 0:
        rent = s
    else:
        rent = side - s
    # print('Метри погонні : ',(ls*n+rent)*w/1000/side)
    # print('----')
    # print('Остача клієнту : ', str(int(rent))+' x '+str(w)+' x '+'25 мм' )
    # print('----')
    # print(unique(l_gen))
    # print('----')
    u = general
    #
    # print(coor)
    return [coor, u]
