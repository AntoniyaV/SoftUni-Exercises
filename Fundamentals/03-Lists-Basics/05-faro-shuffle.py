cards_list = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle = len(cards_list) // 2
    for pos in range(1, len(cards_list), 2):
        cards_list.insert(pos, cards_list[-middle])
        cards_list.pop(-middle)
        middle -= 1

print(cards_list)