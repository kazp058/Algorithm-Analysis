import random


class Objeto:

    def __init__(self, id, peso, valor) -> None:
        self.id = id
        self.peso = peso
        self.valor = valor

    def make_random(id):
        return Objeto(id, random.randrange(5, 20), random.randrange(10, 50))

    def __str__(self) -> str:
        return "%i >> peso: %i valor: %i" % (self.id, self.peso, self.valor)
