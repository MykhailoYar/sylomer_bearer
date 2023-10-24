import numpy

g = 9.81
file_data = 'Load-Factor.txt'

def measure(length, width, n, m, energy, thickness, price, sr, inform):

    out = []
    interval = [round(i, 1) for i in numpy.arange(0.3, 10.1, 0.1)]
    for i in thickness:
        q_factor = round((length * width) / (2 * i * (length + width)), 2)
        if (100 * q_factor) % 5 == 0 and (100 * q_factor) % 10 != 0:
            q_factor = q_factor + 0.05
        q_factor = round(q_factor, 1)
        ratio = length / i
        with open(file_data) as file:
            for line in file:
                ind = interval.index(q_factor)
                line2 = line[0:len(line) - 2]
                line = [float(i) for i in line2.split(',')]
                if line[0] in sr:
                    max_load = line[ind]
                    s = length * width * 10 ** -6
                    x = float(max_load) / g * 10 ** 6 * (s * n)
                    d = round(m / x * 100, 1)
                    if d < energy[1] and d > energy[0] and ratio >= 2:
                        if line[0] != 110:
                            koef = 25
                        else:
                            koef = 12.5
                        square = n * s * i / koef
                        final_price = price[line[0]] * square
                        if n == inform[0] * inform[1]:
                            v = [line[0], n, length, width, i, d, inform[1], inform[0], final_price]
                        else:
                            v = [line[0], int(n), length, width, i, d, n, 1, final_price]
                        out.append(v)
    return out
