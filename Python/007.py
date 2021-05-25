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

# nth = 6
nth = 10001
answer = solve(nth)
print(answer)