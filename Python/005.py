from math import gcd

def solve(n):
    lcm = 1
    for i in range(2, n + 1):
        lcm = lcm * i // gcd(lcm, i)
    return lcm

# n = 10
n = 20
answer = solve(n)
print(answer)
