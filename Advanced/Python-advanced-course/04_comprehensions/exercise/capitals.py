def countries_capitals(pairs):
    return {pair[0]: pair[1] for pair in pairs}


def print_result(result):
    return [print(f'{country} -> {capital}') for country, capital in result.items()]


countries = input().split(', ')
capitals = input().split(', ')

combined = zip(countries, capitals)
countries_and_capitals = countries_capitals(combined)
print_result(countries_and_capitals)
