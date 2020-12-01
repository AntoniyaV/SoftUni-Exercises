def positive_or_negative_product(list_of_nums):
    result = ""
    positive_nums = list(filter(lambda x: x > 0, list_of_nums))

    if 0 in list_of_nums:
        result = "zero"
    elif len(positive_nums) == len(list_of_nums) or len(positive_nums) == 1:
        result = "positive"
    else:
        result = "negative"

    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

nums = [num_1, num_2, num_3]

print(positive_or_negative_product(nums))

