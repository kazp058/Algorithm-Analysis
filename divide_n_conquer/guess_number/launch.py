from models import randomNumber


def busqueda(numero_aleatorio: randomNumber, cota_inferior, cota_superior):
    if cota_inferior == cota_superior:
        x = cota_inferior
    else:
        centro = (cota_inferior + cota_superior) // 2
        if numero_aleatorio.menor_igual(centro):
            x = busqueda(numero_aleatorio, cota_inferior, centro)
        else:
            x = busqueda(numero_aleatorio, centro + 1, cota_superior)
    return x


def adivinar(numero_aleatorio: randomNumber):
    cota_inferior = 5000
    cota_superior = 1

    while numero_aleatorio.menor_igual(cota_inferior):
        cota_inferior = cota_inferior // 2

    while not numero_aleatorio.menor_igual(cota_superior):
        cota_superior = cota_superior * 2

    print("cotas tomadas: (%i, %i)" % (cota_inferior, cota_superior))

    return busqueda(numero_aleatorio, cota_inferior, cota_superior), cota_inferior, cota_superior


rand = randomNumber()
res, cota_inferior, cota_superior = adivinar(rand)

print("numero adivinado: %i\nnumero generado: %i" % (res, rand.value))
print("cotas tomadas: (%i, %i)" % (cota_inferior, cota_superior))
