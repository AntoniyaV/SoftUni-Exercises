from math import sqrt


def line_calculator(x_first, y_first, x_second, y_second):
    x_sum = abs(x_first) + abs(x_second)
    y_sum = abs(y_first) + abs(y_second)
    result = sqrt(x_sum ** 2 + y_sum ** 2)
    return result


def closest_to_center_point(point_x, point_y):
    result = sqrt(abs(point_x) ** 2 + abs(point_y) ** 2)
    return result


line1_x1 = float(input())
line1_y1 = float(input())
line1_x2 = float(input())
line1_y2 = float(input())

line2_x1 = float(input())
line2_y1 = float(input())
line2_x2 = float(input())
line2_y2 = float(input())

line_1 = line_calculator(line1_x1, line1_y1, line1_x2, line1_y2)
line_2 = line_calculator(line2_x1, line2_y1, line2_x2, line2_y2)

if line_1 >= line_2:
    first_result = closest_to_center_point(line1_x1, line1_y1)
    second_result = closest_to_center_point(line1_x2, line1_y2)

    if first_result <= second_result:
        print(f"({int(line1_x1)}, {int(line1_y1)})({int(line1_x2)}, {int(line1_y2)})")
    else:
        print(f"({int(line1_x2)}, {int(line1_y2)})({int(line1_x1)}, {int(line1_y1)})")

else:
    first_result = closest_to_center_point(line2_x1, line2_y1)
    second_result = closest_to_center_point(line2_x2, line2_y2)

    if first_result <= second_result:
        print(f"({int(line2_x1)}, {int(line2_y1)})({int(line2_x2)}, {int(line2_y2)})")
    else:
        print(f"({int(line2_x2)}, {int(line2_y2)})({int(line2_x1)}, {int(line2_y1)})")