def test_neutral(t):
    for i in range(len(t)):
        neutral = true
        for j in range(len(t)):
            if t[i][j] != j or t[j][i] != j:
                neutral = false
        if neutral == true:
            print(i, 'est neutre')

def symmetric(t):
    for i in range(len(t)):
        sym = false
        for j in range(len(t)):
            if t[i][j] == t[j][i]:
                sym = true
                print((i, j))

def associative(t):
    ass = true
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(len(t)):
                if t[t[i][j]][k] != t[i][t[j][k]]:
                    ass = false
                    break
    return ass

def is_morphisme(f, t1, t2):
    for i in range(len(t1)):
        for j in range(len(t1)):
                if f[t1[i][j]] != t2[f[i]][f[j]]:
                    return false
    return true

def lagrange(G):
    for i in G.list():
        H = G.subgroup([i])
        if (G.order() % H.order() != 0):
            return false
    return true

def is_bijection(f):
    for i, value in enumerate(f):
        for j, value2 in enumerate(f):
            if (j != i):
                if value == value2:
                    return false
    return true

def all_applications():
    aplications = []
    for a in range(4):
        for b in range(4):
                for c in range(4):
                        for d in range(4):
                            result.append([a, b, c, d])
    return aplications



