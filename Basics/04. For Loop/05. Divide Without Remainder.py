n = int(input())

sum_p1 = 0
sum_p2 = 0
sum_p3 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        sum_p1 += 1
    if num % 3 == 0:
        sum_p2 += 1
    if num % 4 == 0:
        sum_p3 += 1

p1 = sum_p1 / n * 100
p2 = sum_p2 / n * 100
p3 = sum_p3 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")