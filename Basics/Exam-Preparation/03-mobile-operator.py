contract_period = input()
contract_type = input()
mobile_net = input()
months = int(input())

price_month = 0

if contract_type == 'Small':
    if contract_period == 'one':
        price_month = 9.98
    if contract_period == 'two':
        price_month = 8.58
elif contract_type == 'Middle':
    if contract_period == 'one':
        price_month = 18.99
    if contract_period == 'two':
        price_month = 17.09
elif contract_type == 'Large':
    if contract_period == 'one':
        price_month = 25.98
    if contract_period == 'two':
        price_month = 23.59
elif contract_type == 'ExtraLarge':
    if contract_period == 'one':
        price_month = 35.99
    if contract_period == 'two':
        price_month = 31.79

if mobile_net == 'yes':
    if price_month <= 10:
        price_month += 5.50
    elif price_month <= 30:
        price_month += 4.35
    elif price_month > 30:
        price_month += 3.85

total_price = price_month * months

if contract_period == 'two':
    discount = total_price * (3.75 / 100)
    total_price = total_price - discount

print(f'{total_price:.2f} lv.')