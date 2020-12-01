change = float(input())
coins = 0

change_st = int(change * 100)

while change_st > 0:
    if change_st >= 200:
        coins += 1
        change_st -= 200
    elif change_st >= 100:
        coins += 1
        change_st -= 100
    elif change_st >= 50:
        coins += 1
        change_st -= 50
    elif change_st >= 20:
        coins += 1
        change_st -= 20
    elif change_st >= 10:
        coins += 1
        change_st -= 10
    elif change_st >= 5:
        coins += 1
        change_st -= 5
    elif change_st >= 2:
        coins += 1
        change_st -= 2
    elif change_st >= 1:
        coins += 1
        change_st -= 1

print(coins)