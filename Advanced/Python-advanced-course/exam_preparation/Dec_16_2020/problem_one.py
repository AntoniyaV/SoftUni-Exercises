from collections import deque


def get_collection_info(collection):
    return "none" if not collection else ', '.join([str(x) for x in collection])


males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches_count = 0

while males and females:
    female = females[0]
    male = males[-1]

    if female <= 0:
        female = females.popleft()
        continue

    if male <= 0:
        males.pop()
        continue

    if female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if female == male:
        matches_count += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2

males.reverse()

print(f"Matches: {matches_count}")
print(f"Males left: {get_collection_info(males)}")
print(f"Females left: {get_collection_info(females)}")
