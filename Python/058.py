from math import sqrt

def is_prime(n):
    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    n, step = 1, 2
    prime_count = 0
    while True:
        for _ in range(4):
            n += step
            if is_prime(n):
                prime_count += 1
        if prime_count / (2 * int(sqrt(n)) - 1) < 0.1:
            return int(sqrt(n))
        step += 2

print(solve())