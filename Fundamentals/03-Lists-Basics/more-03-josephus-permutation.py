elements = input().split()
k = int(input())

result = []

while len(elements) > k - 1:
    result.append(elements[k - 1])

    for i in range(k - 1):
        elements.append(elements[i])
    del elements[:k]

elements *= k
for index in range(k - 1, len(elements) + 1, k):
    result.append(elements[index])

result = ",".join(result)
print(f"[{result}]")