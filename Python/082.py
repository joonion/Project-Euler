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
    for row in range(n):
        D[row][0] = M[row][0]
    for col in range(1, n):
        for row in range(n):
            D[row][col] = M[row][col] + D[row][col - 1]
        for row in range(1, n):
            D[row][col] = min(D[row][col], M[row][col] + D[row - 1][col])
        for row in range(n - 2, -1, -1):
            D[row][col] = min(D[row][col], M[row][col] + D[row + 1][col])
    smallest = INF
    for row in range(n):
        if smallest > D[row][n - 1]:
            smallest = D[row][n - 1]
    return smallest

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(','))))
INF = 0
for i in range(n):
    for j in range(n):
        INF += matrix[i][j]
print(solve(n, matrix))   