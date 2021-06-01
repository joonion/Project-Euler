def solve(n):
    a, b, s = 1, 2, 0
    while b <= n:
        a, b = b, a + b 
        if a % 2 == 0:
            s += a
    return s

n = 4000000
print(solve(n))
