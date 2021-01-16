import re
text = input()

pattern = r'(#|@)(?P<word_one>[a-zA-Z]{3,})\1{2}(?P<word_two>[a-zA-Z]{3,})\1'

if re.search(pattern, text) is None:
    print("No word pairs found!")
    print("No mirror words!")

else:
    matched_pairs = re.finditer(pattern, text)
    mirror_pairs = []

    for match in matched_pairs:
        word_one = match.group('word_one')
        word_two = match.group('word_two')

        if word_one == word_two[::-1]:
            mirror_pairs.append(f"{word_one} <=> {word_two}")

    print(f"{len([*re.finditer(pattern, text)])} word pairs found!")

    if not mirror_pairs:
        print("No mirror words!")

    else:
        print("The mirror words are:")
        print(', '.join(mirror_pairs))