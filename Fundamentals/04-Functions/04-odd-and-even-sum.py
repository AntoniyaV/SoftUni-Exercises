def odd_and_even_sum(n):
    odd_sum = 0
    even_sum = 0

    for dgt in str(n):
        digit = int(dgt)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    result = "Odd sum = " + str(odd_sum) + ", " + "Even sum = " + str(even_sum)
    return result


number = int(input())
print(odd_and_even_sum(number))