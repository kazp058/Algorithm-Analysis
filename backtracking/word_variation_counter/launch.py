def esvalida(solucion, nivel):
    idx = 0
    while (idx < nivel and solucion[idx] != solucion[nivel]):
        idx += 1
    return idx == nivel


def variations(solucion, nivel, n, m, out):
    for letra in range(n):
        solucion[nivel] = letra
        if (esvalida(solucion, nivel)):
            if (nivel == m - 1):
                out += 1
            else:
                out = variations(solucion, nivel + 1, n, m, out)

    return out


n = 5
m = 3
out = 0
print(variations([0]*m, 0, n, m, 0))
