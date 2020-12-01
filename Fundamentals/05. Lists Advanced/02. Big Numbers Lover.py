numbers = input().split()

numbers.sort(reverse=True)
biggest = "".join(numbers)

print(biggest)