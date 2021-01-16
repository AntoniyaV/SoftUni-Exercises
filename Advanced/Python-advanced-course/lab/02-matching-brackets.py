expression = input()
indices = []

for i in range(len(expression)):
    if expression[i] == "(":
        indices.append(i)
    elif expression[i] == ")":
        start = indices.pop()
        print(expression[start:i + 1])
