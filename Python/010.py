# returns all the primes below n 
def solve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0 # 1 is not a prime
    for i in range(2, n):
        for j in range(i + i, n, i):
            sieve[j] = 0
    primes = []
    for i in range(2, n):
        if sieve[i] != 0:
            primes.append(sieve[i])
    return primes

# n = 10
n = 2000000
primes = solve(n)
print(sum(primes), len(primes))
