old_version = input().split(".")
new_version = str(int("".join(old_version)) + 1)

result = ""
count = 0

for symbol in new_version:
    count += 1
    if count == len(new_version):
        result += symbol
        break
    result += symbol + "."

print(result)



# old_version = input().split(".")
# old_version = list(map(lambda n: int(n), old_version))
#
# new_version = old_version.copy()
#
# if old_version[-1] == 9:
#     new_version[-1] = 0
#
#     if new_version[-2] == 9:
#         new_version[-2] = 0
#         new_version[-3] +=1
#     else:
#         new_version[-2] += 1
# else:
#     new_version[-1] += 1
#
# new_version = list(map(lambda el: str(el), new_version))
# print(".".join(new_version))