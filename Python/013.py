def solve1(n, nstr):
    s = 0
    for i in range(n):
        s += int(nstr[i])
    return str(s)[::-1]

def ladd(s1, s2):
    digits, carry = "", 0
    length = max(len(s1), len(s2))
    for i in range(length):
        d1 = int(s1[i]) if i < len(s1) else 0
        d2 = int(s2[i]) if i < len(s2) else 0
        digits += str((d1 + d2 + carry) % 10)
        carry = (d1 + d2 + carry) // 10
    if carry != 0:
        digits += str(carry)
    return digits

def solve(n, nstr):
    sumstr = ""
    for i in range(n):
        sumstr = ladd(sumstr, nstr[i][::-1])
    return sumstr

n = 100
nstr = ["" for _ in range(n)]
for i in range(n):
    nstr[i] = input()
answer = solve(n, nstr)
print(answer[::-1][:10], answer)
