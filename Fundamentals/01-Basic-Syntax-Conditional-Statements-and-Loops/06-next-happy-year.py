year = int(input())

counter = 0
new_year = ''

while new_year == '':
    year += 1
    str_year = str(year)
    for i in str_year:
        counter = str_year.count(i)
        if counter == 1:
            new_year += i
        else:
            new_year = ''
            break

print(new_year)


# year = (input())
#
# happy_year = False
#
# while not happy_year:
#     year = int(year) + 1
#     year = str(year)
#
#     if year[0] != year[1] and year[0] != year[2] and year[0] != year[3]:
#         if year[1] != year[2] and year[1] != year[3]:
#             if year[2] != year[3]:
#                 happy_year = True
#
# print(year)


#     first_num = False
#     sec_num = False
#     third_num = False
#
#     if year[0] != year[1] and year[0] != year[2] and year[0] != year[3]:
#         first_num = True
#     if year[1] != year[2] and year[1] != year[3]:
#         sec_num = True
#     if year[2] != year[3]:
#         third_num = True
#
#     happy_year = first_num and sec_num and third_num
#
#     if not happy_year:
#         year = int(year)
#         year += 1
#         year = str(year)
#
# print(year)

