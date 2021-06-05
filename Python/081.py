def shortest(row, col, M, D):
    if row < 0 or col < 0:
        return INF
    elif row == 0 and col == 0:
        D[row][col] = M[row][col]
    elif D[row][col] == INF:
        D[row][col] = M[row][col] + \
                      min(shortest(row - 1, col, M, D), \
                          shortest(row, col - 1, M, D))
    return D[row][col]

def solve(n, M):
    D = [[INF for _ in range(n)] for _ in range(n)]
    return shortest(n - 1, n - 1, M, D)

INF = 0xFFFFFFFF
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(','))))
print(solve(n, matrix))   