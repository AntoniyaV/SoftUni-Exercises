data = input()
chars = ""
result = ""

for i in range(len(data)):
    if data[i].isdigit():
        n = 1
        number = data[i]

        while i + n in range(len(data)) and data[i + n].isdigit():
            number += data[i + n]
            n += 1

        result += chars.upper() * int(number)
        chars = ""

    else:
        chars += data[i]

print(f"Unique symbols used: {len(set(result))}")
print(result)