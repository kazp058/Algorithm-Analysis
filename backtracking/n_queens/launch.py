def isValid(sol, level):
    valid = True
    idx = 0
    while idx < level and valid:

        if sol[idx] == sol[level] or abs(sol[level] - sol[idx]) == level - idx:
            valid = False
        idx += 1
    return valid


def n_queens(sol, level, n, out):
    for __i in range(n):
        sol[level] = __i
        if isValid(sol, level):
            if level == n - 1:
                out.append(sol.copy())
            else:
                out = n_queens(sol, level + 1, n, out)
    return out


columns = 8
sol = [0]*columns
solutions = n_queens(sol, 0, columns, [])
print(solutions)
print("posiblidades: %i" % len(solutions))
