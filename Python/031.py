def search(i, wallet, change, coins):
    W = sum(wallet)
    if change < W:
        return 0
    elif change == W:
        return 1
    else:
        count = 0
        for j in range(i, len(coins)):
            count += search(j, wallet + [coins[j]], change, coins)
        return count

def solve1(change, coins):
    return search(0, [], change, coins)

coins = [1, 2, 5, 10, 20, 50, 100, 200]
change = 200
# coins = [1, 2, 5]
# change = 5
answer = solve1(change, coins)
print(answer)
