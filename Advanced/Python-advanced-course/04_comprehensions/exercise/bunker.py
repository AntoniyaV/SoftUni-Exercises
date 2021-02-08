def set_categories(some_categories):
    return {category: {} for category in some_categories}


def add_to_bunker(info, some_bunker):
    for line in info:
        category, item, item_info = line
        some_bunker[category][item] = {'quantity': 0, 'quality': 0}
        for data in item_info.split(';'):
            data_name, data_value = data.split(':')
            some_bunker[category][item][data_name] = int(data_value)
    return some_bunker


def calculate_items_data_in_bunker(some_bunker, data_name):
    return sum([some_bunker[category][item][data_name] for category in some_bunker for item in some_bunker[category]])


def find_average_quality(some_bunker, data_name):
    quality_sum = calculate_items_data_in_bunker(some_bunker, data_name)
    categories_count = len(some_bunker)
    return quality_sum / categories_count


def print_result(result):
    items_count = calculate_items_data_in_bunker(result, 'quantity')
    avg_quality = find_average_quality(result, 'quality')
    print(f"Count of items: {items_count}")
    print(f"Average quality: {avg_quality:.2f}")
    return [print(f"{category} -> {', '.join([item for item in result[category]])}") for category in result]


categories = input().split(', ')
n = int(input())

bunker = set_categories(categories)
all_info = []

for _ in range(n):
    all_info.append(input().split(' - '))

bunker = add_to_bunker(all_info, bunker)
print_result(bunker)