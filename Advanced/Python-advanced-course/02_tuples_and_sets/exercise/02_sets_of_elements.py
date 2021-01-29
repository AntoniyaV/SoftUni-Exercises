def print_result(result):
    for x in result:
        print(x)


n, m = input().split()
first_set = set()
second_set = set()


for _ in range(int(n)):
    first_set.add(int(input()))

for _ in range(int(m)):
    second_set.add(int(input()))

elements_in_both_sets = first_set & second_set
print_result(elements_in_both_sets)
