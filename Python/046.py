def is_prime(n, primes):
    for i in range(len(primes)):
        if n % primes[i] == 0:
            return False
    return True

def is_Goldbach(n, primes):
    i, x = 1, n - 2
    while x > 1:
        if x in primes:
            print(n, x, i)
            return True
        i += 1
        x = n - 2 * i * i
    return False

def solve():
    primes = [2]
    n = 3
    while True:
        if is_prime(n, primes):
            primes.append(n)
        elif not is_Goldbach(n, primes):
            return n
        n += 2 

answer = solve()
print(answer)
