def find_negative_numbers(numbers):
    return list(filter(lambda x: x < 0, numbers))


def find_positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))


def print_result(sum_neg, sum_pos):
    print(sum_neg)
    print(sum_pos)
    if abs(sum_neg) > sum_pos:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = [int(x) for x in input().split()]
negative_sum = sum(find_negative_numbers(nums))
positive_sum = sum(find_positive_numbers(nums))
print_result(negative_sum, positive_sum)
