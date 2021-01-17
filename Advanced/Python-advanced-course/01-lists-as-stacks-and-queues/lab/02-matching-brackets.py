<<<<<<< HEAD
expression = input()
indices = []

for i in range(len(expression)):
    if expression[i] == "(":
        indices.append(i)
    elif expression[i] == ")":
        start = indices.pop()
        print(expression[start:i + 1])
=======
expression = input()
indices = []

for i in range(len(expression)):
    if expression[i] == "(":
        indices.append(i)
    elif expression[i] == ")":
        start = indices.pop()
        print(expression[start:i + 1])
>>>>>>> c6ab6c831ddfde4b18aa1def9039f6cda9cb6b84
