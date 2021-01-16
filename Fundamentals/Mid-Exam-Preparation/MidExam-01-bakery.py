import math
biscuits_per_day_per_worker = int(input())
workers = int(input())
total_biscuits_comp = int(input())

biscuits_per_day = biscuits_per_day_per_worker * workers
amount_of_biscuits = 20 * biscuits_per_day + math.floor(10 * 0.75 * biscuits_per_day)

# for day in range(1, 31):
#     if day % 3 == 0:
#         amount_of_biscuits += math.floor(0.75 * biscuits_per_day)
#     else:
#         amount_of_biscuits += biscuits_per_day

print(f"You have produced {amount_of_biscuits} biscuits for the past month.")

if amount_of_biscuits > total_biscuits_comp:
    difference = amount_of_biscuits - total_biscuits_comp
    percentage = difference / total_biscuits_comp * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")

else:
    difference = total_biscuits_comp - amount_of_biscuits
    percentage = difference / total_biscuits_comp * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")