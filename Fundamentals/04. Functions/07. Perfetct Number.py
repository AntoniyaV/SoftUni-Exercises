import math


def perfect_number_finder(number):
    sum_divisors = 1

    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            sum_divisors += n + int(number / n)

    if number == sum_divisors:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(perfect_number_finder(num))
