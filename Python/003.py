from math import floor, sqrt

# returns the list of prime factors
def solve(n):
    sqrtn = floor(sqrt(n))
    for i in range(2, sqrtn + 1):
        if n % i == 0:
            return [i] + solve(n // i)
    return [n]

# n = 13195
n = 600851475143 
factors = solve(n)
print(factors)
print(max(factors))