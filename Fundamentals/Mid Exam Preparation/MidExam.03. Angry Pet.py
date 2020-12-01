ratings = [int(n) for n in input().split()]
entry_point = int(input())
item_type = input()
price_type = input()

ep_rating = ratings[entry_point]
left_range = []
right_range = []
left_sum = 0
right_sum = 0

if item_type == "cheap":
    left_range = [ratings[i] for i in range(0, entry_point) if ratings[i] < ep_rating]
    right_range = [ratings[i] for i in range(entry_point + 1, len(ratings)) if ratings[i] < ep_rating]

elif item_type == "expensive":
    left_range = [ratings[i] for i in range(0, entry_point) if ratings[i] >= ep_rating]
    right_range = [ratings[i] for i in range(entry_point + 1, len(ratings)) if ratings[i] >= ep_rating]

if price_type == "positive":
    left_sum = sum([price for price in left_range if price > 0])
    right_sum = sum([price for price in right_range if price > 0])

elif price_type == "negative":
    left_sum = sum([price for price in left_range if price < 0])
    right_sum = sum([price for price in right_range if price < 0])

elif price_type == "all":
    left_sum = sum(left_range)
    right_sum = sum(right_range)

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
else:
    print(f"Right - {right_sum}")
