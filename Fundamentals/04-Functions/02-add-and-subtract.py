def sum_numbers(a, b):
    d = a + b
    return d


def retract(a, b, c):
    d = sum_numbers(a, b)
    result = d - c
    return result


def add_and_subtract(a, b, c):
    return retract(a, b, c)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))


# def add_and_subtract(num_1, num_2, num_3):
#
#     def sum_numbers():
#         return num_1 + num_2
#
#     def subtract():
#         result = sum_numbers()
#         return result - num_3
#
#     return subtract()
#
#
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# print(add_and_subtract(number_1, number_2, number_3))
