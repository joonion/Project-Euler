from math import factorial

def solve(n):
    m, s = factorial(n), 0
    while m != 0:
        s += m % 10
        m = m // 10
    return s

# n = 10
n = 100
answer = solve(n)
print(answer)
