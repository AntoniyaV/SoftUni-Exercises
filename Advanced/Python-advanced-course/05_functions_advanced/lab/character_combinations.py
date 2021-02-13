def character_permutations(chars, index=0):
    if index == len(chars):
        print(''.join(chars))
        return

    for i in range(index, len(chars)):
        chars[index], chars[i] = chars[i], chars[index]
        character_permutations(chars, index + 1)
        chars[index], chars[i] = chars[i], chars[index]


text = list(input())
character_permutations(text)
