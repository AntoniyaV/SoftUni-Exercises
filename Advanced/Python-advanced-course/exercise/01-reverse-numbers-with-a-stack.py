numbers = input().split()
stack_nums = []

for i in range(len(numbers)):
    stack_nums.append(numbers.pop())

print(' '.join(stack_nums))