def truncable(n, primes):
    for i in range(len(primes)):
        if n % primes[i] == 0:
            return False
    primes.append(n)
    m = n
    while m > 0:
        if m not in primes:
            return False 
        m //= 10
    m = n
    while m > 0:
        if m not in primes:
            return False 
        m %= 10 ** (len(str(m)) - 1)
    return True

def solve():
    primes = [2, 3, 5, 7]
    truncables = []
    n = 11
    while len(truncables) < 11:
        if truncable(n, primes):
            truncables.append(n)
            print(n)
        n += 2
    return truncables

answer = solve()
print(sum(answer), answer)
