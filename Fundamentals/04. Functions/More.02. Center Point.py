from math import sqrt


def closest_to_center_point(point_x, point_y):
    result = sqrt(abs(point_x) ** 2 + abs(point_y) ** 2)
    return result


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_result = closest_to_center_point(x1, y1)
second_result = closest_to_center_point(x2, y2)

if first_result <= second_result:
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")