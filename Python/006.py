def solve(n):
    sum1 = n * (n + 1) * (2 * n + 1) // 6
    sum2 = (n * (n + 1) // 2) ** 2
    return sum2 - sum1

# n = 10
n = 100
answer = solve(n)
print(answer)
