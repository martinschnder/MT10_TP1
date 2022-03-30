def test_neutral(t):
    for i in range(len(t)):
        neutral = true
        for j in range(len(t)):
            if t[i][j] != j or t[j][i] != j:
                neutral = false
        if neutral == true:
            return i