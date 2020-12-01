painting_nums = input().split()
painting_nums = [int(n) for n in painting_nums]
instructions = input()


def existing_painting(num, paintings):
    return True if num in paintings else False


while not instructions == "END":

    if "Change" in instructions:
        number = int(instructions.split()[1])
        if existing_painting(number, painting_nums):
            changed_num = int(instructions.split()[2])
            index = painting_nums.index(number)
            painting_nums[index] = changed_num

    elif "Hide" in instructions:
        number = int(instructions.split()[1])
        if existing_painting(number, painting_nums):
            painting_nums.remove(number)

    elif "Switch" in instructions:
        number = int(instructions.split()[1])
        number2 = int(instructions.split()[2])
        if existing_painting(number, painting_nums) and existing_painting(number2, painting_nums):
            index1 = painting_nums.index(number)
            index2 = painting_nums.index(number2)
            painting_nums[index1], painting_nums[index2] = number2, number

    elif "Insert" in instructions:
        place = int(instructions.split()[1]) + 1
        number = int(instructions.split()[2])
        if 0 <= place < len(painting_nums):
            painting_nums.insert(place, number)

    elif "Reverse" in instructions:
        painting_nums.reverse()

    instructions = input()

final_paintings = [str(p) for p in painting_nums]
print(' '.join(final_paintings))