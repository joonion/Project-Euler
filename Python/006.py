def solve(n):
    s1 = n * (n + 1) * (2 * n + 1) // 6
    s2 = (n * (n + 1) // 2) ** 2
    return s2 - s1

# n = 10
n = 100
print(solve(n))
