num_cars = int(input())

cars = {}

for n in range(num_cars):
    car_brand, mileage, start_fuel = input().split("|")
    cars[car_brand] = [int(mileage), int(start_fuel)]

command = input()

while not command == "Stop":
    action, car = command.split(" : ")[0], command.split(" : ")[1]

    if action == "Drive":
        distance, fuel = int(command.split(" : ")[2]), int(command.split(" : ")[3])

        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car][0] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")

    elif action == "Refuel":
        fuel = int(command.split(" : ")[2])
        cars[car][1] += fuel

        if cars[car][1] > 75:
            fuel -= cars[car][1] - 75
            cars[car][1] = 75

        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        kilometers = int(command.split(" : ")[2])
        cars[car][0] -= kilometers

        if cars[car][0] < 10000:
            cars[car][0] = 10000

        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

sorted_cars = dict(sorted(cars.items(), key=lambda x: (-x[1][0], x[0])))

for car_name, car_info in sorted_cars.items():
    print(f"{car_name} -> Mileage: {car_info[0]} kms, Fuel in the tank: {car_info[1]} lt.")