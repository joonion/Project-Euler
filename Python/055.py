def is_Lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True

def solve(n):
    count = 0
    for i in range(1, n):
        if is_Lychrel(i):
            print(i)
            count += 1
    return count

# print(is_Lychrel(47))
# print(is_Lychrel(349))
# print(is_Lychrel(196))

n = 10000
print(solve(n))
