def solve(n, m):
    S = set([])
    for a in range(n, m + 1):
        for b in range(n, m + 1):
            S.add(a ** b)
    return len(S)

# n, m = 2, 5
n, m = 2, 100
answer = solve(n, m)
print(answer)