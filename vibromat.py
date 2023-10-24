import numpy as np

w = [78, 131, 107, 64, 127, 169, 156, 125, 144]

answer, capa, loadf = [], [], []

for i in range(0, len(w) + 1):
    if i == 0:
        load = w[i] / 4
    else:
        if i == len(w):
            load = w[i - 1] / 4
        else:
            load = (w[i] + w[i - 1]) / 4
    loadf.append(load)
    if 35 <= load <= 48:
        answer.append("Vibromat SM 60/50")
        capa.append(round(load / 59, 2))
    else:
        if 49 <= load <= 100:
            answer.append("Vibromat SM 120/50")
            capa.append(round(load / 110, 2))
        else:
            if 101 <= load <= 198:
                answer.append("Vibromat SM 250/50")
                capa.append(round(load / 226, 2))
            else:
                if 199 <= load <= 329:
                    answer.append("Vibromat SM 470/50")
                    capa.append(round(load / 392, 2))
                else:
                    if 330 <= load <= 794:
                        answer.append("Vibromat SM 940/50")
                        capa.append(round(load / 794, 2))
                    if load < 35:
                        answer.append("недоVibromat SM 60/50")
                        capa.append(0)
print(answer)
print(capa)
answer = sorted(answer)
values, counts = np.unique(answer, return_counts=True)
d = dict()
for i in range(0, len(values)):
    d.update({values[i]: counts[i] * 2})
print(d)
