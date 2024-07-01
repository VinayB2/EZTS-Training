def minCoins(amt):
    coins = 0
    while amt > 0:
        if amt >= 7:
            coins += 1
            amt -= 7
        elif amt >= 5:
            coins += 1
            amt -= 5
        else: 
            coins += amt
            break
    return coins

def minCoins2(amt, coins):
    if amt < 7 or amt < 4 or amt == 0:
        return coins + amt
    a = minCoins2(amt - 7, coins + 1)
    b = minCoins2(amt - 5, coins + 1)
    c = minCoins2(amt - 1, coins + 1)
    return min(a, b, c)
print(minCoins2(18, 0))


mincoin = float('inf')
def minCoins2(amt, coins, lst):
    global mincoin
    if amt == 0:
        if coins < mincoin: mincoin = coins
    if amt < 7 or amt < 4:
        return coins + amt
    for i in lst:
        minCoins2(amt - i, coins + 1, lst)
        
minCoins2(18, 0, [7, 5, 1])
print(mincoin)