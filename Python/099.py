def solve(n):
    largest, line = 0, 1
    for i in range(n):
        m, k = map(int, input().split(','))
        print(line)
        num = m ** k
        if largest < num:
            largest, line = num, i + 1
    return line

n = 1000
print(solve(n))
