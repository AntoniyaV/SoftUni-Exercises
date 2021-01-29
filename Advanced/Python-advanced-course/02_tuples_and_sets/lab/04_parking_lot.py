def print_result(result):
    if not result:
        print('Parking Lot is Empty')
    else:
        for x in result:
            print(x)


n = int(input())
cars = set()

for _ in range(n):
    direction, number = input().split(', ')

    if direction == 'IN':
        cars.add(number)
    else:
        cars.remove(number)

print_result(cars)
