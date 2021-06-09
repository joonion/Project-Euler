from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(maxp):
    primes = [2]
    n = 3
    while n <= maxp:
        if is_prime(n):
            primes.append(n)
        n += 2
    return primes

def check_prime_power(primes, check):
    for a in range(len(primes)):
        if primes[a] ** 2 >= len(check): break
        for b in range(len(primes)):
            if primes[a] ** 2 + primes[b] ** 3 >= len(check): break
            for c in range(len(primes)):
                n = primes[a] ** 2 + primes[b] ** 3 + primes[c] ** 4
                if n >= len(check): break
                check[n] = 1
    return sum(check)

def solve(n):
    maxp = int(sqrt(n))
    primes = find_primes(maxp)
    check = [0] * n
    return check_prime_power(primes, check)

# n = 50
n = 50000000
print(solve(n))
