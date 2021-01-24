from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
bullets_starting_count = len(bullets)

while True:
    if not locks:
        bullets_used = bullets_starting_count - len(bullets)
        earned_money = intelligence_value - (bullets_used * bullet_price)
        print(f"{len(bullets)} bullets left. Earned ${earned_money}")
        break

    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break

    for i in range(len(bullets)):
        if i == gun_barrel_size and bullets:
            print("Reloading!")
            break

        if not locks:
            break

        current_bullet = bullets.pop()
        if current_bullet <= locks[0]:
            print("Bang!")
            locks.popleft()

        else:
            print("Ping!")
