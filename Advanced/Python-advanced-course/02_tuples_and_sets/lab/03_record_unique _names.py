def print_result(result):
    for x in result:
        print(x)


n = int(input())
list_of_names = []

for _ in range(n):
    list_of_names.append(input())

unique_names = set(list_of_names)
print_result(unique_names)
