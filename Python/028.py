def direction(dir, n, row, col):
    if row == col and row <= 0:
        return 0 # turn to the right
    elif row == col and row > 0:
        return 1 # turn to the left
    elif row + col == 0 and col < 0:
        return 2 # turn to the top
    elif row + col == 1 and col > 0:
        return 3 # turn to the bottom
    return dir
    
def solve(n):
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    M = [[0 for _ in range(n)] for _ in range(n)]
    row, col, dir = 0, 0, 0
    for i in range(1, n * n + 1):
        M[row + n // 2][col + n // 2] = i
        dir = direction(dir, n, row, col)
        row, col = row + move[dir][0], col + move[dir][1]
    # returns the sum of the numbers on the diagonal
    s = 0
    for i in range(n):
        s += M[i][i] + M[i][n - 1 - i]
    return s - 1

# n = 5
n = 1001
answer = solve(n)
print(answer)
