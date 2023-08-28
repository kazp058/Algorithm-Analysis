from models import *

M = 70
N = 1000000000

def greedy_students(grade, tasks):
    selected_tasks = []
    remaining_grade = grade

    for __idtask in range(len(tasks)):
        task = tasks[__idtask]
        if remaining_grade >= task.score:
            remaining_grade -= task.score
            selected_tasks.append(task)

    if remaining_grade > 0:
        prefered_idtask = -1
        for __idtask in range(len(tasks)):
            task = tasks[__idtask]
            if (__idtask not in selected_tasks 
                or prefered_idtask < 0 
                or (tasks[prefered_idtask].effort >= task.effort 
                    and tasks[prefered_idtask].score < task.score)):
                prefered_idtask = __idtask
        selected_tasks.append(task)
    return selected_tasks

# Diseñe un algoritmo que seleccione las tareas
# que le otorgan una nota mayor o igual a la 
# minima que requieren el menor esfuerzo del
# estudiante

tasks = [Task.make_random(t) for t in range(N)]
ordered = sorted(tasks)
selected = greedy_students(M, ordered)

acum_score = 0
acum_effort = 0
for s in selected:
    acum_score += s.score
    acum_effort += s.effort
    print("%s" %(s))
print("\neffort: %i score: %i"%(acum_effort, acum_score))