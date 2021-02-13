def round_numbers(*args):
    return [round(n) for n in args]


nums = [float(x) for x in input().split()]
rounded_nums = round_numbers(*nums)
print(rounded_nums)