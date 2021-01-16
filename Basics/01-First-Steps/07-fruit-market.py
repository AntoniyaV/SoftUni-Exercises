strawberries_lv = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())
raspberries_lv = strawberries_lv/2
oranges_lv = raspberries_lv - (raspberries_lv * 0.4)
bananas_lv = raspberries_lv - (raspberries_lv * 0.8)
sum = strawberries_lv * strawberries_kg + bananas_lv * bananas_kg + oranges_lv * oranges_kg + raspberries_lv * raspberries_kg
print(sum)