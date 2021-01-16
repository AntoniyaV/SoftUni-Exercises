from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

for _ in range(len(orders)):
    if orders[0] <= quantity:
        quantity -= orders[0]
        orders.popleft()
    else:
        break

if not orders:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join(str(n) for n in orders)}")
