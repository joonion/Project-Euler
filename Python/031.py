def solve(change, coins):
    D = [[0 for _ in range(len(coins))] for _ in range(change + 1)]
    for i in range(change + 1):
        D[i][0] = 1
    for i in range(change + 1):
        for j in range(1, len(coins)):
            D[i][j] += D[i][j - 1]
            if coins[j] <= i:
                D[i][j] += D[i - coins[j]][j]
    return D[change][len(coins) - 1]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
change = 200
# coins = [1, 2, 5]
# change = 5
answer = solve(change, coins)
print(answer)
