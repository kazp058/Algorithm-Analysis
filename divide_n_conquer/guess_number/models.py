import random


class randomNumber:
    def __init__(self) -> None:
        self.value = random.randint(0, 500)

    def menor_igual(self, m):
        return m >= self.value
