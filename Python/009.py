
def Pythagorean(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

def solve():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if Pythagorean(a, b, c):
                return a, b, c
    return None

a, b, c = solve()
print(a * b * c)
