from itertools import permutations

def solve():
    perms = list(permutations("123456789"))
    pandigits = set([])
    for k in range(len(perms)):
        pstr = "".join(perms[k])
        for i in range(5):
            for j in range(i + 1, 5):
                if (eval(pstr[:i+1]+"*"+pstr[i+1:j+1]) == eval(pstr[j+1:])):
                    pandigits.add(int(pstr[j+1:]))
                    print(int(pstr[j+1:]))
    return sum(pandigits)

answer = solve()
print(answer)

