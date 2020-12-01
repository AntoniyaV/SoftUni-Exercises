def ticket_checker(some_ticket, some_symbol):
    counter = 0
    for el in some_ticket:
        if el == some_symbol:
            counter += 1
        else:
            if counter >= 6:
                break
            else:
                counter = 0
    return counter


tickets = [t.strip() for t in input().split(",")]
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    left_side = ticket[:10]
    right_side = ticket[10:]
    is_winning = False

    for symbol in winning_symbols:
        if ticket.count(symbol) == 20:
            print(f"ticket \"{ticket}\" - 10{symbol} Jackpot!")
            is_winning = True
            break

        counter_left = ticket_checker(left_side, symbol)
        counter_right = ticket_checker(right_side, symbol)

        if counter_right >= 6 and counter_left >= 6:
            is_winning = True
            if counter_right > counter_left:
                print(f'ticket "{ticket}" - {counter_left}{symbol}')
            else:
                print(f'ticket "{ticket}" - {counter_right}{symbol}')
            break

    if not is_winning:
        print(f'ticket "{ticket}" - no match')
