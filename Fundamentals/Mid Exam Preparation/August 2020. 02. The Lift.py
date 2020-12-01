people_waiting = int(input())
places_on_lift = input().split()
places_on_lift = [int(i) for i in places_on_lift]

for i in range(len(places_on_lift)):
    if places_on_lift[i] == 4:
        continue

    places_to_fill = 4 - places_on_lift[i]

    if people_waiting >= places_to_fill:
        places_on_lift[i] += places_to_fill
        people_waiting -= places_to_fill
    else:
        places_on_lift[i] += people_waiting
        people_waiting -= people_waiting

if people_waiting == 0 and not all(n == 4 for n in places_on_lift):
    print("The lift has empty spots!")

elif people_waiting > 0 and all(n == 4 for n in places_on_lift):
    print(f"There isn't enough space! {people_waiting} people in a queue!")

places_str = list(map(lambda x: str(x), places_on_lift))
print(' '.join(places_str))
