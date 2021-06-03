def solve(n):
    sieve = [True] * (n + 1)
    s = 0
    for i in range(2, n + 1):
        if sieve[i] == True:
            s += i
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return s

# n = 10
n = 2000000
print(solve(n))
