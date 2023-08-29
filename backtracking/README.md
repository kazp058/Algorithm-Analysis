```
VueltaAtras()
    prepararRecorridoNivel(nivel)
    por cada posibilidad en ese nivel:
        solucion[nivel] = posibilidad
        si es valida(solucion, nivel):
            tratarsolucion()
        sino:
            VueltaAtras()
```
