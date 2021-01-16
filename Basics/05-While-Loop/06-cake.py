cake_width = int(input())
cake_length = int(input())

total_pieces = cake_width * cake_length
pieces_left = total_pieces

pieces = input()

while pieces != "STOP":
    pieces_num = int(pieces)
    pieces_left -= pieces_num
    if pieces_left <= 0:
        break
    pieces = input()

if pieces_left > 0:
    print(f"{pieces_left} pieces are left.")
else:
    print(f"No more cake left! You need {abs(pieces_left)} pieces more.")