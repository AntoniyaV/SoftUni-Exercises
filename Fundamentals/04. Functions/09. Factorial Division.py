def factorial_divisor(number_1, number_2):
    factorial_1 = 1
    factorial_2 = 1

    for n_1 in range(2, number_1 + 1):
        factorial_1 *= n_1

    for n_2 in range(2, number_2 + 1):
        factorial_2 *= n_2

    result = factorial_1 / factorial_2
    return result


num_1 = int(input())
num_2 = int(input())
print(f"{factorial_divisor(num_1, num_2):.2f}")