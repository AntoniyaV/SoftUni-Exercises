line_1_str = input()
line_2_str = input()
line_3_str = input()

line_1 = line_1_str.split()
line_1 = [int(i) for i in line_1]
line_2 = line_2_str.split()
line_2 = [int(j) for j in line_2]
line_3 = line_3_str.split()
line_3 = [int(k) for k in line_3]

if (line_1[0] == 1 and line_1[1] == 1 and line_1[2] == 1) \
        or (line_1[0] == 1 and line_2[0] == 1 and line_3[0] == 1) \
        or (line_1[0] == 1 and line_2[1] == 1 and line_3[2] == 1) \
        or (line_1[1] == 1 and line_2[1] == 1 and line_3[1] == 1) \
        or (line_1[2] == 1 and line_2[2] == 1 and line_3[2] == 1) \
        or (line_1[2] == 1 and line_2[1] == 1 and line_3[0] == 1) \
        or (line_2[0] == 1 and line_2[1] == 1 and line_2[2] == 1) \
        or (line_3[0] == 1 and line_3[1] == 1 and line_3[2] == 1):
    print("First player won")
elif (line_1[0] == 2 and line_1[1] == 2 and line_1[2] == 2) \
        or (line_1[0] == 2 and line_2[0] == 2 and line_3[0] == 2) \
        or (line_1[0] == 2 and line_2[1] == 2 and line_3[2] == 2) \
        or (line_1[1] == 2 and line_2[1] == 2 and line_3[1] == 2) \
        or (line_1[2] == 2 and line_2[2] == 2 and line_3[2] == 2) \
        or (line_1[2] == 2 and line_2[1] == 2 and line_3[0] == 2) \
        or (line_2[0] == 2 and line_2[1] == 2 and line_2[2] == 2) \
        or (line_3[0] == 2 and line_3[1] == 2 and line_3[2] == 2):
    print("Second player won")
else:
    print("Draw!")
