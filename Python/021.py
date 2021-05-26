from math import floor, sqrt

def proper_divisors(n):
    divs = set([1])
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return list(divs)
    
def d(n):
    return sum(proper_divisors(n))

def is_amicable(n):
    a = d(n)
    b = d(a)
    return True if n == b and n != a else False

def solve(n):
    s = 0
    for i in range(1, n + 1):
        if is_amicable(i):
            s += i
    return s

n = 10000
answer = solve(n)
print(answer)
