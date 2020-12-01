def tribonacci_sequence(number):
    for_summary = [1]

    for n in range(1, number):
        sum_n = 0
        if n < 4:
            sum_n = sum(for_summary)
        else:
            sum_n = for_summary[-1] + for_summary[-2] + for_summary[-3]

        for_summary.append(sum_n)

    result = [str(i) for i in for_summary]
    result = " ".join(result)
    return result


num = int(input())
print(tribonacci_sequence(num))
