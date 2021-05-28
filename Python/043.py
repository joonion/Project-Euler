from itertools import permutations

def is_divisible(nstr):
    p = [2, 3, 5, 7, 11, 13, 17]
    for i in range(len(p)):
        if int(nstr[(i + 1):(i + 4)]) % p[i] != 0:
            return False
    return True

def solve():
    s = "0123456789"
    perms = list(permutations(s))
    total = 0
    for i in range(len(perms)):
        nstr = "".join(perms[i])
        if is_divisible(nstr):
            total += int(nstr)
    return total

answer = solve()
print(answer)
