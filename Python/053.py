def solve(n, N):
    count, row = 0, [0] * (n + 1)
    for i in range(n + 1):
        for j in range(i, -1, -1):
            if j == 0 or j == i:
                row[j] = 1
            else:
                row[j] = row[j] + row[j - 1]
            if row[j] > N:
                count += 1
    return count

n, N = 100, 1000000
print(solve(n, N))