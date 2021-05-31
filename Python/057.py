'''
Utilizing the continued fraction.
Generalization can be obtained by the Euclid's algorithm.
'''
def solve(N):
    count = 0
    n, d = 1, 1
    for _ in range(N):
        n, d = n + 2 * d, n + d
        if len(str(n)) > len(str(d)):
            count += 1
    return count

n = 1000
print(solve(n))

# n = 8
# for i in range(1, n + 1):
#     solve(i)
#     print()