def expressions_and_results(numbers, result=0, expression=""):
    if not numbers:
        return [(expression, result)]

    plus_sign_result = expressions_and_results(numbers[1:], result+numbers[0], f'{expression}+{numbers[0]}')
    minus_sign_result = expressions_and_results(numbers[1:], result-numbers[0], f'{expression}-{numbers[0]}')
    return plus_sign_result + minus_sign_result


def print_result(result):
    return [print(f"{el[0]}={el[1]}") for el in result]


nums_list = [int(x) for x in input().split(', ')]
results = expressions_and_results(nums_list)
print_result(results)
