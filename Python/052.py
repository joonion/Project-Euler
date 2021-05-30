def permutable(n, m):
    if sorted(str(n)) == sorted(str(n * m)):
        return True
    return False
    
def permutable_all(n):
    for m in range(2, 7):
        if not permutable(n, m):
            return False
    return True

def solve():
    n = 1
    while True:
        if permutable_all(n):
            return n
        n += 1

print(solve())
