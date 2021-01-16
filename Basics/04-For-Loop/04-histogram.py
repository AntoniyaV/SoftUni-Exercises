n = int(input())

sum_p1 = 0
sum_p2 = 0
sum_p3 = 0
sum_p4 = 0
sum_p5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        sum_p1 += 1
    elif 200 <= num < 400:
        sum_p2 += 1
    elif 400 <= num < 600:
        sum_p3 += 1
    elif 600 <= num < 800:
        sum_p4 += 1
    elif num >= 800:
        sum_p5 += 1

print(f"{sum_p1 / n * 100:.2f}%")
print(f"{sum_p2 / n * 100:.2f}%")
print(f"{sum_p3 / n * 100:.2f}%")
print(f"{sum_p4 / n * 100:.2f}%")
print(f"{sum_p5 / n * 100:.2f}%")