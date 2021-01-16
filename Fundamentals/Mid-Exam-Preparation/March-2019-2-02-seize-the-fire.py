fire_levels = input().split("#")
water = int(input())

total_effort = 0
put_out_cells = []

for fire in fire_levels:
    fire_type, value = fire.split(" = ")
    value = int(value)

    if fire_type == "High" and value not in range(81, 126):
        continue
    elif fire_type == "Medium" and value not in range(51, 81):
        continue
    elif fire_type == "Low" and value not in range(1, 51):
        continue

    if water < value:
        continue

    water -= value
    current_effort = 0.25 * value
    total_effort += current_effort
    put_out_cells.append(value)

    if water == 0:
        break

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")
