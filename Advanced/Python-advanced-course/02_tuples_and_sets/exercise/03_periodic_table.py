def print_result(result):
    for x in result:
        print(x)


n = int(input())
compounds = []

for _ in range(n):
    compounds += input().split()

unique_compounds = set(compounds)
print_result(unique_compounds)
