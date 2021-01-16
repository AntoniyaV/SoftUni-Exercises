num_lines = int(input())

result = 0

for i in range(num_lines):
    letter = input()
    result += ord(letter)

print(f"The sum equals: {result}")