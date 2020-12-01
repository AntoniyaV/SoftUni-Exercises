word = input()
word_lower = word.lower()

water_counter = word_lower.count("water")
sand_counter = word_lower.count("sand")
fish_counter = word_lower.count("fish")
sun_counter = word_lower.count("sun")
word_count = water_counter + sand_counter + fish_counter + sun_counter

print(word_count)
