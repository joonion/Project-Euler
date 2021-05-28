from itertools import permutations
from math import floor, sqrt

def is_prime(n):
    if n % 2 == 0: 
        return False
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime(perms):
    for i in range(len(perms)):
        n = int("".join(perms[i]))
        if is_prime(n):
            return n
    return 0

def solve():
    for i in range(9):
        s = "987654321"
        perms = list(permutations(s[i:]))
        prime = find_prime(perms)
        if prime != 0:
            return prime
    return None 

answer = solve()
print(answer)
