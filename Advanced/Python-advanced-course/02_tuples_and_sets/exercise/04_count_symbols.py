def sort_and_print_result(result):
    sorted_result = sorted(result.items(), key=lambda x: x[0])

    for result_pair in sorted_result:
        print(f"{result_pair[0]}: {result_pair[1]} time/s")


text = input()
symbol_occurrences = {}

for ch in text:
    if ch not in symbol_occurrences:
        symbol_occurrences[ch] = text.count(ch)

sort_and_print_result(symbol_occurrences)