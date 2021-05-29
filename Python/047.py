from math import floor, sqrt

def prime_factors(n):
    if n <= 1:
        return []
    else:
        if n % 2 == 0:
            return [2] + prime_factors(n // 2)
        for i in range(3, floor(sqrt(n)) + 1, 2):
            if n % i == 0:
                return [i] + prime_factors(n // i)
        return [n]

def is_consecutive(n, m):
    for i in range(len(m)):
        if len(set(prime_factors(m[i]))) != n:
            return False
    return True

def solve(n):
    m = []
    for i in range(1, n + 1):
        m.append(i)
    while True:
        if is_consecutive(n, m):
            return m
        m.append(m.pop(0) + n)

# n = 2
# n = 3
n = 4
answer = solve(n)
print(answer[0], answer)
