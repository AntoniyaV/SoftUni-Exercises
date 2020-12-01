nums = input()
remove_nums = int(input())

list_nums = nums.split()
list_nums = [int(i) for i in list_nums]

for n in range(remove_nums):
    smallest = 9999999999
    for num in list_nums:
        if num < smallest:
            smallest = num
    list_nums.remove(smallest)

print(list_nums)