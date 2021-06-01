from math import sqrt

def solve(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return solve(n // i)
    return n

# n = 13195
n = 600851475143 
print(solve(n))