def solve(n, S):
    product, greatest, start, end = 0, 0, 0, 0
    for i in range(len(S)):
        product *= int(S[i])
        if product == 0:
            product, start, end = int(S[i]), i, i
        else:
            if end - start + 1 < n:
                end += 1
            else:
                start, end = start + 1, end + 1
                product //= int(S[start - 1])
        if greatest < product:
            greatest = product
    return greatest

# n = 4
n = 13
S = ""
for i in range(20):
    S += input()
print(solve(n, S))
