n = int(input())
capacity = 255

capacity_left = 255

for i in range(n):
    liters_to_pour = int(input())
    if capacity_left < liters_to_pour:
        print("Insufficient capacity!")
    else:
        capacity_left -= liters_to_pour

print(capacity - capacity_left)