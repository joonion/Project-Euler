def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

def lcm(n, m):
    return n * m // gcd(n, m)

def solve(n):
    m = 1
    for i in range(2, n + 1):
        m = lcm(m, i)
    return m

# n = 10
n = 20
print(solve(n))
