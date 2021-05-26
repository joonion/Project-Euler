def collatz_length2(n, D):
    if n not in D:
        next = n // 2 if n % 2 == 0 else 3 * n + 1
        D[n] = 1 + collatz_length2(next, D)
    return D[n]

def collatz_length(n):
    length = 1
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        length += 1
    return length

def solve(n):
    D = {1:1}
    maxn, maxlen = 0, 0
    for i in range(1, n):
        length = collatz_length2(i, D)
        if maxlen < length:
            maxn, maxlen = i, length
    return maxn, maxlen        

n = 1000000
answer, maxlen = solve(n)
print(answer, maxlen)
