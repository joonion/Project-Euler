def arrive(n):
    s, m = str(n), 0
    for i in range(len(s)):
        m += int(s[i]) ** 2
    if m == 89 or m == 1:
        return m
    else:
        return arrive(m)

def solve(n):
    count = 0
    for i in range(1, n + 1):
        if arrive(i) == 89:
            count += 1
    return count

# print(arrive(44))
# print(arrive(85))

n = 10000000
print(solve(n))

