def circular_prime(n, sieve):
    s = str(n)
    l = len(s)
    for _ in range(l - 1):
        s = s[1:] + s[0]
        if sieve[int(s)] == 0:
            return False
    return True 

def solve(n):
    sieve = [0, 1] + [i for i in range(2, n + 1)]
    for i in range(2, n + 1):
        for j in range(i + i, n + 1, i):
            sieve[j] = 0
    count = 0
    for i in range(2, n + 1):
        if sieve[i] != 0 and circular_prime(i, sieve):
            count += 1
    return count

n = 1000000
answer = solve(n)
print(answer)