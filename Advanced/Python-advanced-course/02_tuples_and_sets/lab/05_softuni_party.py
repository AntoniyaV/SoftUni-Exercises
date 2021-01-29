def print_result(result):
    print(len(result))
    for x in result:
        print(x)


n = int(input())
guests = []

for _ in range(n):
    guests.append(input())

while True:
    guest = input()

    if guest == 'END':
        break

    if guest in guests:
        guests.remove(guest)

guests = sorted(guests)
print_result(guests)
