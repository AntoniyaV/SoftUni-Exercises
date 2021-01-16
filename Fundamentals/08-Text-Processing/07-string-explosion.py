explosion_data = input()

strength = 0
new_el = "*"
additional_strength = 0

for i in range(len(explosion_data)):
    if explosion_data[i] == ">":
        strength = int(explosion_data[i + 1]) + additional_strength
        start = i + 1
        end = i + strength + 1

        for sub_i in range(start, end):
            if sub_i >= len(explosion_data):
                break
            if explosion_data[sub_i] == ">":
                additional_strength = end - sub_i
                break

            explosion_data = explosion_data[:sub_i] + new_el + explosion_data[sub_i + 1:]
            additional_strength = 0

explosion_data = explosion_data.replace("*", "")
print(explosion_data)