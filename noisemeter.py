# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:01:08 2017

@author: User
"""

# -*- coding: utf-8 -*-
import csv
import tkinter as tk
from tkinter import filedialog

level = 1  # 1-октавні, не1-третьоктавні
q = [3, 4, 5]
Measure = [['wall'], ['ceil'], ['wall']]
t = 0
t2 = 1
if level != 1:
    f = ['Time', 'Leq A', 'Number', '20', '25', '31.5', '40', '50', '63', '80',
         '100', '125', '160', '200', '250', '315', '400', '500',
         '630', '800', '1000', '1250', '1600', '2000', '2500', '3150', '4000', '5000']
    k = [12, len(f) - 3, 2]  # початок і кінець рядка з третьоктавними смугами;
else:
    f = ['Time', 'Leq A', 'Number', '31.5', '63', '125', '250', '500', '1000', '2000', '4000', '8000', '16000']
    k = [5, len(f) - 3, 3]
for i in range(1, len(q)):
    q[i] = q[i] + q[i - 1]


root = tk.Tk()
root.update()
root.filename = filedialog.askopenfilenames(initialdir='/', title='Choose a file')
# print (root.tk.splitlist(filez))
root.destroy()
filez = list(root.filename)  # масив назв файлів
match2 = list()
graph = list()  # список з вихідними даними
final = list()

print(filez)
final.append(f)
final.append(Measure[0])
# final.append(Measure [t] )
for i in range(0, len(filez)):
    x_file = open(filez[i], "r")
    ansil = list([i])
    ansit = list([1])
    gl = list()
    leqa = list()

    # import re

    # pattern = r'[0-9][0-9]_[0-9][0-9]_[0-9][0-9].csv'
    # match = re.findall(pattern, filez[i])
    # print(match)
    # mat = re.findall(pattern, filez[i])  # для масиву 3окт
    # match2.append(mat)  # для масиву 3окт
    import csv

    with open(filez[i]) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            time = list(row)
            try:
                it = time.index('Время:') + 1
                ansit.append(time[it])
                break
            except ValueError:
                None

        for row in reader:
            time = list(row)
            try:
                il = time.index('Leq') + k[0]
                x = time.index('Leq') + 2
                ansil.append(time[il:il + k[1]])
                leqa.append(time[x])
            except ValueError:
                None

    graph.append(ansit[1])  # time
    graph.append(leqa[len(leqa) - 1])  # leq A
    graph.append(i + 1)  # number
    graph = graph + ansil[len(ansil) - k[2]]  # values
    final.append(graph)
    graph = list()
##    if i==q[t]-1:
##        final.append(list())
##        m=Measure[t2]
##        final.append(m)
##        #print(m)
##        if t<len(q)-1:
##            t+=1
##            if t2<len(Measure)-1:
##                t2+=1

file = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
# with open(file_name+'.csv', 'w') as csvfile:
with file:
    writer = csv.writer(file, delimiter=';', lineterminator='\n')
    for i in range(0, len(final)):
        # 2*len(q)-1
        writer.writerow(final[i])
