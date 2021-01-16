chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

total_menu = chicken_menu * 10.35 + fish_menu * 12.40 + veg_menu * 8.15
dessert = total_menu * 0.2
total = total_menu + dessert + 2.50

print(f'Total: {total:.2f}')