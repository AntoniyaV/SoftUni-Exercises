prime_sum = 0
non_prime_sum = 0

number_str = input()
while number_str != "stop":
    number = int(number_str)
    is_prime = True

    if number < 0:
        print("Number is negative.")
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False

        if is_prime:
            prime_sum += number
        else:
            non_prime_sum += number

    number_str = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")