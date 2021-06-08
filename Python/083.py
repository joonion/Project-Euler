from queue import PriorityQueue

def neighbors(row, col, n, M):
    N, dir = [], [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(len(dir)):
        nrow, ncol = row + dir[i][0], col + dir[i][1]
        if 0 <= nrow < n and 0 <= ncol < n and M[nrow][ncol] > 0:
            N.append((nrow, ncol))
    return N

def dijkstra(srow, scol, n, M):
    PQ, length = PriorityQueue(), M[srow][scol]
    PQ.put((length, (srow, scol)))
    M[srow][scol] = -1
    while not PQ.empty():
        length, v = PQ.get()
        row, col = v[0], v[1]
        if row == col == n - 1:
            return length
        for v in neighbors(row, col, n, M):
            nrow, ncol = v[0], v[1]
            PQ.put((length + M[nrow][ncol], (nrow, ncol)))
            M[nrow][ncol] = -1
    return None

def solve(n, M):
    return dijkstra(0, 0, n, M)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(','))))
INF = 0
for i in range(n):
    for j in range(n):
        INF += matrix[i][j]

print(solve(n, matrix))
