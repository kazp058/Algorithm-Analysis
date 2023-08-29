## Dividir y conquistar con combinacion

```
DividirConquistar(arreglo)
    si arreglo.tamaño = 1:
        solucion = arreglo
    sino:
        pivote = arreglo.tamaño // 2
        grupo_1 = DividirConquistar(arreglo[0: pivote])
        grupo_2 = DividirConquistar(arreglo[pivote + 1: arreglo.tamaño])
        solucion = combinar(grupo_1, grupo_2)

    return solucion
```

## Dividir y conquistar sin combinacion

```
DividirConquistar(arreglo)
    si arreglo.tamaño = 1:
        solucion = arreglo
    sino:
        pivote = arreglo.tamaño // 2

        si esValido(arreglo[0: pivote]):
            solucion = DividirConquistar(arreglo[0: pivote])
        sino:
            solucion = DividirConquistar(arreglo[pivote + 1: arreglo.tamaño])

    return solucion
```
