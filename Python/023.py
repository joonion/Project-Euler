from math import floor, sqrt

def proper_divisors(n):
    d = [1]
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                d.append(i)
            else:
                d.append(i)
                d.append(n // i)
    return d  

def is_abundant(n):
    if sum(proper_divisors(n)) > n:
        return True
    return False

def abundants(n):
    a = []
    for i in range(12, n):
        if is_abundant(i):
            a.append(i)
    return a

def solve(n):
    a = abundants(n)
    numbers = [False] * n
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] + a[j] < n:
                numbers[a[i] + a[j]] = True
    s = 0
    for i in range(1, len(numbers)):
        if numbers[i] == False:
            s += i
    return s

n = 28123 
answer = solve(n)
print(answer)
