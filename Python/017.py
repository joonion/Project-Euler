def solve(n):
    N = 2 ** n
    s = 0
    while N != 0:
        s += N % 10
        N //= 10
    return s 

# n = 15
n = 1000
answer = solve(n)
print(answer)