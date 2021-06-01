def is_prime(n, primes):
    for i in range(len(primes)):
        if n % primes[i] == 0:
            return False
    return True

def solve(nth):
    n, primes = 3, [2]
    while len(primes) < nth:
        if is_prime(n, primes):
            primes.append(n)
        n += 2
    return primes[-1]

# n = 6
n = 10001
print(solve(n))