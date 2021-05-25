def solve(n):
    s = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s

# n = 10
n = 1000
answer = solve(n)
print(answer)
