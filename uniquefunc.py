def unique(l_gen):
    l_gen = sorted(l_gen)
    n = 0
    q = [1]
    out = {}
    for i in l_gen[1::]:
        if i == l_gen[n]:
            q[-1]+=1
            out[str(i)] = q[-1]
        else:
            q.append(1)
        n+=1
    return out
