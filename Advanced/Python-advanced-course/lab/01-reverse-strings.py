line = list(input())
reverse_line = []

for i in range(len(line)):
    reverse_line.append(line.pop())

print(''.join(reverse_line))