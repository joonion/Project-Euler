def is_palindrome(n):
    s, r = str(n), str(n)[::-1]
    return s == r

def solve(d):
    n, m, largest = 10 ** (d - 1), 10 ** d, 0
    for i in range(n, m):
        for j in range(i + 1, m):
            p = i * j
            if largest < p and is_palindrome(p):
                largest = p
    return largest

# d = 2
d = 3
print(solve(d))
