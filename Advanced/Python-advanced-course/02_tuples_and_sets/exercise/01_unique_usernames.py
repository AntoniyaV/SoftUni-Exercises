def print_result(result):
    for x in result:
        print(x)


n = int(input())
names = set()

for _ in range(n):
    names.add(input())

print_result(names)
