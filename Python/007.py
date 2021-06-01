from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(nth):
    n, count = 2, 0
    while count < nth:
        if is_prime(n):
            count += 1
        n += 1
    return n - 1

# n = 6
n = 10001
print(solve(n))