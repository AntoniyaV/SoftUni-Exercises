fires_str = input()
water = int(input())

fires = fires_str.split("#")
total_effort = 0
total_fire = 0

print("Cells:")

for cell in fires:
    cell_list = cell.split(" = ")
    fire_type = cell_list[0]
    cell_value = int(cell_list[1])
    effort = 0

    if (fire_type == "High" and 81 <= cell_value <= 125) \
            or (fire_type == "Medium" and 51 <= cell_value <= 80) \
            or (fire_type == "Low" and 1 <= cell_value <= 50):

        water -= cell_value
        if water >= 0:
            print(f" - {cell_value}")

            effort = 0.25 * cell_value
            total_fire += cell_value
        else:
            water += cell_value
            continue

    total_effort += effort

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
