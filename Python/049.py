def find_primes(d):
    sieve = [i for i in range(10 ** d)]
    sieve[1] = 0 # 1 is not a prime.
    sieve[2] = 2 # 2 is the first prime.
    for i in range(3, len(sieve), 2):
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0
    dprime = []
    for i in range(len(sieve)):
        if sieve[i] != 0 and len(str(sieve[i])) == d:
            dprime.append(i)
    return dprime

def find_sequences(primes):
    table = {}
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            n, m = primes[i], primes[j]
            if sorted(str(n)) == sorted(str(m)):
                diff = m - n
                if diff not in table:
                    table[diff] = [(n, m)]
                else:
                    table[diff].append((n, m))
    return table

def solve(d):
    dprime = find_primes(d)
    seqmap = find_sequences(dprime)
    for key in seqmap.keys():
        for p1 in seqmap[key]:
            for p2 in seqmap[key]:
                if p1[1] == p2[0]:
                    print(p1[0], p1[1], p2[1], end="")
                    print()

d = 4
answer = solve(d)
print(answer)
