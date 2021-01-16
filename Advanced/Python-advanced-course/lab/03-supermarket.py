<<<<<<< HEAD
from collections import deque

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'
queue = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{len(queue)} people remaining.')
        break
    elif command == PAID_COMMAND:
        for i in range(len(queue)):
            print(queue.popleft())
    else:
=======
from collections import deque

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'
queue = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{len(queue)} people remaining.')
        break
    elif command == PAID_COMMAND:
        for i in range(len(queue)):
            print(queue.popleft())
    else:
>>>>>>> c6ab6c831ddfde4b18aa1def9039f6cda9cb6b84
        queue.append(command)