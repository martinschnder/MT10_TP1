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

def morphisme(f, t1, t2):
    morp = true
    for i in range(len(t1)):
        for j in range(len(t1)):
                if f[t1[i][j]] != t2[f[i]][f[j]]:
                    morp = false
                    break
    return morp

def lagrange(G):
    for i in G.list():
        H = G.subgroup([i])
        if (G.order() % H.order() != 0):
            return false
    return true

