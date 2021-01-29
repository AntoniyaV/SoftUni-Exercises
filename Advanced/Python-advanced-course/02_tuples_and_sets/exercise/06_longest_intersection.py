def get_numbers_in_a_range(range_info):
    start, end = range_info.split(',')
    start, end = int(start), int(end)
    return set(num for num in range(start, end + 1))


n = int(input())

first_range = set()
second_range = set()
longest_intersection = []

for _ in range(n):
    info_first, info_second = input().split('-')

    first_range = get_numbers_in_a_range(info_first)
    second_range = get_numbers_in_a_range(info_second)
    intersection = first_range & second_range

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
