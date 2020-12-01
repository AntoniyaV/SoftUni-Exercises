number_1 = int(input())
number_2 = int(input())

for num in range(number_1, number_2 + 1):
    num_str = str(num)
    even_sum = 0
    odd_sum = 0

    for i, digit in enumerate(num_str):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(num, end=' ')