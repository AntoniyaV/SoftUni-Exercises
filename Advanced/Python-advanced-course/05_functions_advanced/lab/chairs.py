def combine_names(names, n, current_combination=[]):
    if len(current_combination) == n:
        print(', '.join(current_combination))
        return

    for i in range(len(names)):
        name = names[i]
        current_combination.append(name)
        combine_names(names[i + 1:], n)
        current_combination.pop()


names = input().split(', ')
num_chairs = int(input())
combine_names(names, num_chairs)
