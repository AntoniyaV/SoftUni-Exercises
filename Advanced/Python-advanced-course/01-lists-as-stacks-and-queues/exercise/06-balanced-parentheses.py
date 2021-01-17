brackets = input()

opening_bracket = []
matching_brackets = {'(': ')', '[': ']', '{': '}'}
is_balanced = True

for bracket in brackets:
    if bracket in '({[':
        opening_bracket.append(bracket)

    else:
        if not opening_bracket:
            is_balanced = False
            print('NO')
            break

        opening = opening_bracket.pop()
        if not matching_brackets[opening] == bracket:
            is_balanced = False
            print('NO')
            break

if is_balanced:
    print('YES')
