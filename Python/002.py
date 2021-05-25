def solve():
    a, b, s = 1, 2, 2
    while b <= 4000000:
        a, b = b, a + b 
        if b % 2 == 0:
            s += b
    return s

answer = solve()
print(answer)
