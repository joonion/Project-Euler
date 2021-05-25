def is_palindrome(n):
    m, d = n, 0
    while m != 0:
        d = d * 10 + m % 10
        m //= 10
    return n == d

def solve(d):
    n, m = 10 ** (d - 1), 10 ** d
    largest, x, y = 0, 0, 0
    for i in range(n, m):
        for j in range(i + 1, m):
            p = i * j
            if is_palindrome(p) and p > largest:
                largest, x, y = p, i, j
    return largest, x, y

# d = 2
d = 3
answer, i, j = solve(d)
print(answer, i, j)
