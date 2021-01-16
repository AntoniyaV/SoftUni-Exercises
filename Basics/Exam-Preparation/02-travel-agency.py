tickets_num = int(input())
client_budget = int(input())
ticket_price = int(input())

total_tickets_price = tickets_num * ticket_price

if total_tickets_price > client_budget:
    print(f"The budget of {client_budget}$ is not enough. Your client can't buy {tickets_num} tickets with this budget!" )
else:
    print(f"You can sell your client {tickets_num} tickets for the price of {total_tickets_price}$!")
    print(f"Your client should become a change of {client_budget - total_tickets_price}$!")