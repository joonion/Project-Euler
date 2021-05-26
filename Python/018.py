def maxpath(row, col, T, D):
    if row == len(T) - 1:
        return T[row][col]
    elif D[row][col] == -1:
        D[row][col] = T[row][col] + \
                      max(maxpath(row + 1, col, T, D), \
                          maxpath(row + 1, col + 1, T, D))
    return D[row][col]

def solve(n, T):
    D = [[] for _ in range(n)]
    for i in range(n):
        D[i] = [-1 for _ in range(len(T[i]))]
    return maxpath(0, 0, T, D)

n = 15
T = [[] for _ in range(n)]
for i in range(n):
    T[i] = (list(map(int, input().split())))
answer = solve(n, T)
print(answer)