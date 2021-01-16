numbers = [int(n) for n in input().split()]
avg_value = sum(numbers) / len(numbers)

greater_than_avg = [num for num in numbers if num > avg_value]
greater_than_avg.sort(reverse=True)

if not greater_than_avg:
    print("No")

elif len(greater_than_avg) < 5:
    print(' '.join([str(n) for n in greater_than_avg]))

else:
    top_5 = [greater_than_avg[i] for i in range(5)]
    print(' '.join([str(n) for n in top_5]))