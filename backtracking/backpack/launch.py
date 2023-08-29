from models import Objeto


def mochila(objetos, solucion, nivel, n, m, peso, beneficio, mejorSolucion, mejorValor):

    peso = peso + objetos[nivel].peso
    beneficio = beneficio + objetos[nivel].valor

    solucion[nivel] = objetos[nivel]
    if peso <= m:
        if nivel == n - 1:
            if mejorValor < beneficio:
                mejorValor = beneficio
                mejorSolucion = solucion.copy()
        else:
            mejorSolucion, mejorValor = mochila(objetos, solucion, nivel + 1, n, m, peso,
                                                beneficio, mejorSolucion, mejorValor)

    peso = peso - objetos[nivel].peso
    beneficio = beneficio - objetos[nivel].valor

    solucion[nivel] = None
    if (nivel == n - 1):
        if (mejorValor < beneficio):
            mejorValor = beneficio
            mejorSolucion = solucion.copy()
    else:
        mejorSolucion, mejorValor = mochila(objetos, solucion, nivel + 1, n, m, peso,
                                            beneficio, mejorSolucion, mejorValor)
    return mejorSolucion, mejorValor


N = 20  # cantidad de objetos
M = 40  # peso maximo que puede aguantar la mochila

objetos = []
solucion = [None] * N

for i in range(N):
    objetos.append(Objeto.make_random(i))


res = mochila(objetos, solucion, 0, N, M, 0, 0, [], 0)
filtered = list(filter(lambda x: x != None, res[0]))

accum_beneficio = 0
accum_peso = 0
output_beneficio = res[1]
for __f in filtered:
    print(__f)
    accum_beneficio += __f.valor
    accum_peso += __f.peso

print("peso acumulado: %i\nbeneficio acumulado: %i\nretorno algt: %i\n" %
      (accum_peso, accum_beneficio, output_beneficio))
