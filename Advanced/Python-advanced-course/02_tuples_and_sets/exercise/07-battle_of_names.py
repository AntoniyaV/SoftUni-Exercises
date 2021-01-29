def calculate_line_number(letters, line):
    sum_ascii = 0
    for letter in letters:
        sum_ascii += ord(letter)
    return sum_ascii // line


def is_even(number):
    return number % 2 == 0


n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    line_number = calculate_line_number(name, i)

    if is_even(line_number):
        even_set.add(line_number)
    else:
        odd_set.add(line_number)

odd_sum = sum(odd_set)
even_sum = sum(even_set)
result = set()

if odd_sum == even_sum:
    result = odd_set.union(even_set)

elif odd_sum > even_sum:
    result = odd_set.difference(even_set)

else:
    result = odd_set.symmetric_difference(even_set)

print(', '.join([str(x) for x in result]))