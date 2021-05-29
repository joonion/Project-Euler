def solve(n):
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    return str(s)

# n = 10
n = 1000
answer = solve(n)
print(answer[len(answer)-10:len(answer)])
