<<<<<<< HEAD
from collections import deque

quantity = int(input())
people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    else:
        people.append(name)

while True:
    command = input()
    if command == 'End':
        print(f'{quantity} liters left')
        break

    if command.isdigit():
        if int(command) <= quantity:
            print(f'{people.popleft()} got water')
            quantity -= int(command)
        else:
            print(f'{people.popleft()} must wait')

    elif 'refill' in command:
        liters = int(command.split()[1])
        quantity += liters
=======
from collections import deque

quantity = int(input())
people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    else:
        people.append(name)

while True:
    command = input()
    if command == 'End':
        print(f'{quantity} liters left')
        break

    if command.isdigit():
        if int(command) <= quantity:
            print(f'{people.popleft()} got water')
            quantity -= int(command)
        else:
            print(f'{people.popleft()} must wait')

    elif 'refill' in command:
        liters = int(command.split()[1])
        quantity += liters
>>>>>>> c6ab6c831ddfde4b18aa1def9039f6cda9cb6b84
