from math import factorial

def path(x, y, n):
    if x > n or y > n:
        return 0
    elif x == n and y == n:
        return 1
    else:
        return path(x + 1, y, n) + path(x, y + 1, n)

def path2(x, y, n, D):
    if x > n or y > n:
        return 0
    elif x == n and y == n:
        D[x][y] = 1
    elif D[x][y] == -1:
        D[x][y] = path2(x + 1, y, n, D) + path2(x, y + 1, n, D)
    return D[x][y]

# returns binomial(2n, n)
def path3(n):
    return factorial(2 * n) // (factorial(n) ** 2)

def solve(n):
    D = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    return path2(0, 0, n, D)
    
# n = 2
n = 20
answer = path3(n)
print(answer)
