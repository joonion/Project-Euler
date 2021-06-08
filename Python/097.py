n = 28433 * (2 ** 7830457) + 1
s = ""
for i in range(10):
    s += str(n % 10)
    n //= 10
print(s[::-1])
