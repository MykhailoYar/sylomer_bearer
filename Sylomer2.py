def Sylomer(length, width, dim_sr, boundary, numbers):

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
