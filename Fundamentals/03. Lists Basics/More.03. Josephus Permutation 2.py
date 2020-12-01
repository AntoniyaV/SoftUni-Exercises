elements = input().split()
k = int(input())

pos = k - 1
index = 0
result = []

while len(elements) > 0:
    index = (pos + index) % len(elements)
    result.append(elements[index])
    elements.pop(index)

result = ",".join(result)
print(f"[{result}]")