num_people = int(input())
capacity = int(input())

import math
courses = math.ceil(num_people / capacity)

print(courses)