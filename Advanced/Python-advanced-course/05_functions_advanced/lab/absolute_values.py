def get_absolute_values(*args):
    return [abs(n) for n in args]


nums = [float(x) for x in input().split()]
absolute_values = get_absolute_values(*nums)
print(absolute_values)