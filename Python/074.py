def len_fact_chain(n, chain, factorial):
    s, m = str(n), 0
    for i in range(len(s)):
        m += factorial[int(s[i])]
    if m in chain:
        return len(chain)
    else:
        chain.append(m)
        return len_fact_chain(m, chain, factorial)

def solve(n, length):
    factorial = [1] + [i for i in range(1, 10)]
    for i in range(1, 10):
        factorial[i] *= factorial[i - 1]
    count = 0
    for i in range(1, n):
        if len_fact_chain(i, [i], factorial) == length:
            count += 1
    return count

n, m = 1000000, 60
print(solve(n, m))
