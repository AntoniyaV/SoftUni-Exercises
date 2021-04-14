from collections import deque


def is_time_enough(customer_time, taxi_time):
    return customer_time <= taxi_time


customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis.pop()

    if is_time_enough(customer, taxi):
        total_time += customer
        customers.popleft()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")