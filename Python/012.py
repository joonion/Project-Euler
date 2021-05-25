from math import floor, sqrt

def div_count(n):
    count = 0
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            count += 1 if i * i == n else 2
    return count 

def divisors(n):
    d = []
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d

def triangular(n):
    return n * (n + 1) // 2

def solve():
    n = 1
    while div_count(triangular(n)) <= 500:
        n += 1 
    return triangular(n)

answer = solve()
print(answer)
