import random

class Task:
    
    def __init__(self, id, effort, score) -> None:
        self.id = id
        self.effort = effort
        self.score = score
    
    def make_random(__id):
        return Task(__id, random.randrange(1,10), random.randrange(5,20))
    
    def __str__(self) -> str:
        return "id: %i >> effort: %s  score: %s" %(self.id, str(self.effort), str(self.score))
    
    def __lt__(self,other):
        return self.effort < other.effort