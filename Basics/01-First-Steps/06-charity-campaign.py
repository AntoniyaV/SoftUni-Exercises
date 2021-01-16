days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
db = days * bakers
sum = (db * cakes * 45) + (db * waffles * 5.80) + (db * pancakes * 3.20)
final_sum = sum - (sum/8)
print(final_sum)