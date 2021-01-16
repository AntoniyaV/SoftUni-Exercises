text = input()
no_reps = ""

for i in range(len(text)):
    if i + 1 in range(len(text)):
        if text[i] == text[i + 1]:
            continue

    no_reps += text[i]

print(no_reps)