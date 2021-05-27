def trim(s):
    return s.replace("\"", "")

def score(s, nth):
    score = 0
    for i in range(len(s)):
        score += ord(s[i]) - ord('A') + 1
    return score * nth

def solve(strs):
    total = 0
    for i in range(len(strs)):
        total += score(strs[i], i + 1)
    return total

strs = list(map(trim, input().split(',')))
strs.sort()
answer = solve(strs)
print(answer)
