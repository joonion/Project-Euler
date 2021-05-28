from math import floor, sqrt

def is_triangle(word):
    s = 0
    for i in range(len(word)):
        s += ord(word[i]) - ord('A') + 1
    n = 8 * s + 1
    if n == floor(sqrt(n)) ** 2:
        return True
    else:
        return False    

def solve(words):
    count = 0
    for i in range(len(words)):
        if is_triangle(words[i]):
            count += 1
    return count

def trim(s):
    return s.replace("\"", "")

words = list(map(trim, input().split(",")))
answer = solve(words)
print(answer)
