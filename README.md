# Algorithm-Analysis

Nota: En algunos casos se puede observar que se usan objetos dentro de ciertas implementaciones, realmente esto no es necesario y tampoco cambia en mucho la logica del algoritmo, uno de los motivos por los que prefiero hacer uso de clases es que es mas facil de visualizar.

Por ejemplo, la clase _Tarea_:

```python

class Tarea:

    def __init__(self, id, esfuerzo, puntaje) -> None:
        self.id = id
        self.esfuerzo = esfuerzo
        self.puntaje = puntaje

```

Esta clase Tarea podria ser reemplazada por una tupla

```python
    tarea = (0,5,11) #(id, esfuerzo, puntaje)
```

Obviamente durante la implementacion es mas facil observar a que se esta accediendo en una clase que en una tupla.

```python
    tarea_tupla = (0,5,11) #(id, esfuerzo, puntaje)
    tarea_objeto = Tarea(0, 5, 11)

    print(tarea_tupla[1]) #Imprime el esfuerzo
    print(tarea_objeto.esfuerzo) #Imprime el esfuerzo
```

Tambien en ciertos casos habran metodos implementados en estas clases, estos generalmente no son importantes para el algoritmo, solo permiten simplificar el codigo pero no tienen implicaciones directas en el algoritmo.

## Strategy:

- [brute force](https://github.com/kazp058/Algorithm-Analysis/tree/main/brute_force)
- [backtracking](https://github.com/kazp058/Algorithm-Analysis/tree/main/divide_n_conquer)
- [Dividir y conquistar](https://github.com/kazp058/Algorithm-Analysis/tree/main/divide_n_conquer)
- [greedy](https://github.com/kazp058/Algorithm-Analysis/tree/main/greedy_algorithms)
