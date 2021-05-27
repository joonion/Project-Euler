def solve(n):
    F = [1, 1]
    while len(str(F[-1])) < n:
        F.append(F[-1] + F[-2])
    return len(F)

# n = 3    
n = 1000
answer = solve(n)
print(answer)
