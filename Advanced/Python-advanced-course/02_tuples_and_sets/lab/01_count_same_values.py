nums = tuple(float(x) for x in input().split())
numbers_occurrences = {}

for num in nums:
    if num not in numbers_occurrences:
        numbers_occurrences[num] = nums.count(num)

for number, occurrence in numbers_occurrences.items():
    print(f'{number} - {occurrence} times')
