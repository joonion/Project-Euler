def double_palindrome(n):
    s = str(n)
    b = str(bin(n))[2:]
    if s == s[::-1] and b == b[::-1]:
        return True 
    return False 

def solve(n):
    s = 0
    for i in range(1, n):
        if double_palindrome(i):
            s += i
    return s

n = 1000000
answer = solve(n)
print(answer)
