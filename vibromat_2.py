import numpy as np

w = [78, 131, 107, 64, 127, 169, 156, 125, 144, "в37"]

answer = []

print(w[-1])
print([])
loadf = []


for i in range(0, len(w) - 1):
    load = w[i] / 4
    loadf.append(load)
    if 35 <= load <= 48:
        answer.append("Vibromat SM 60/50")
        print("Vibromat SM 60/50", "blue")
    else:
        if 49 <= load <= 100:
            answer.append("Vibromat SM 120/50")
            print("Vibromat SM 120/50", "green")
        else:
            if 101 <= load <= 198:
                answer.append("Vibromat SM 250/50")
                print("Vibromat SM 250/50", "brown")
            else:
                if 199 <= load <= 329:
                    answer.append("Vibromat SM 470/50")
                    print("Vibromat SM 470/50", "red")
                else:
                    if 330 <= load <= 794:
                        answer.append("Vibromat SM 940/50")
                        print("Vibromat SM 940/50", "grey")
                    if load < 35:
                        answer.append(" недоVibromat SM 60/50")
                        print(" недоVibromat SM 60/50", "blue")
print(answer)
answer = sorted(answer)
values, counts = np.unique(answer, return_counts=True)
d = dict()
for i in range(0, len(values)):
    d.update({values[i]: counts[i] * 4})
print(d)
