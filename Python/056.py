def digitsum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

def solve(n):
    largest = 0
    for a in range(1, 100):
        for b in range(1, 100):
            s = digitsum(a ** b)
            if largest < s:
                largest = s
    return largest                

n = 100
print(solve(n))
