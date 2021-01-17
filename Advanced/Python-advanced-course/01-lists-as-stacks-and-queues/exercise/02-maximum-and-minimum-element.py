<<<<<<< HEAD
n = int(input())
stack = []

for _ in range(n):
    command = input()
    query_type = int(command.split()[0])

    if query_type == 1:
        element = int(command.split()[1])
        stack.append(element)

    elif query_type == 2 and stack:
        stack.pop()

    elif query_type == 3 and stack:
        print(max(stack))

    elif query_type == 4 and stack:
        print(min(stack))

popped_stack = []
for i in range(len(stack)):
    popped_stack.append(str(stack.pop()))

=======
n = int(input())
stack = []

for _ in range(n):
    command = input()
    query_type = int(command.split()[0])

    if query_type == 1:
        element = int(command.split()[1])
        stack.append(element)

    elif query_type == 2 and stack:
        stack.pop()

    elif query_type == 3 and stack:
        print(max(stack))

    elif query_type == 4 and stack:
        print(min(stack))

popped_stack = []
for i in range(len(stack)):
    popped_stack.append(str(stack.pop()))

>>>>>>> c6ab6c831ddfde4b18aa1def9039f6cda9cb6b84
print(', '.join(popped_stack))