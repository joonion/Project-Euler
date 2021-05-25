def solve(n, d, A):
    largest, direction, maxi, maxj = 0, 0, 0, 0
    for i in range(n - d + 1):
        for j in range(n - d + 1):
            hori, vert, diagup, diagdn = 1, 1, 1, 1
            for k in range(d):
                hori *= A[i][j + k]
                vert *= A[i + k][j]
                diagup *= A[i + k][j + k]
                diagdn *= A[i + k][j - k + d - 1]
            if largest < hori:
                largest, direction, maxi, maxj = hori, 0, i, j
            if largest < vert:
                largest, direction, maxi, maxj = vert, 1, i, j
            if largest < diagup:
                largest, direction, maxi, maxj = diagup, 2, i, j
            if largest < diagdn:
                largest, direction, maxi, maxj = diagdn, 3, i, j + d - 1
    return largest, direction, maxi, maxj

n, d = 20, 4
A = [[] for _ in range(n)]
for i in range(n):
    A[i] = list(map(int, input().split()))
answer, direction, i, j = solve(n, d, A)
print(answer, direction, i, j)