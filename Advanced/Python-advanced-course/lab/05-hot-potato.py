from collections import deque

kids = deque(input().split())
tosses = int(input())

while not len(kids) == 1:
    for i in range(tosses):
        if i == tosses - 1:
            print(f'Removed {kids.popleft()}')
            break
        else:
            kids.append(kids.popleft())

print(f'Last is {kids.popleft()}')


