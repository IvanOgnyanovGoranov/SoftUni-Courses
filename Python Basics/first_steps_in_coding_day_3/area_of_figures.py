from math import pi

figure = input()

if figure == "square":
    square_number = float(input())
    figure_result = square_number * square_number
    print(f"{figure_result:.3f}")
elif figure == "rectangle":
    area1 = float(input())
    area2 = float(input())
    rectangle_result = area2 * area1
    print(f"{rectangle_result:.3f}")
elif figure == "circle":
    circle_number = float(input())
    circle_face = (circle_number * circle_number) * pi
    print(f"{circle_face:.3f}")
elif figure == "triangle":
    triangle_area1 = float(input())
    triangle_area2 = float(input())
    triangle_result = triangle_area2 * triangle_area1 / 2
    print(f"{triangle_result:.3f}")

# from math import pi
#
# figure = input()
# area = 0
#
# if figure == "square":
#     a = float(input())
#     area = a * a
#
# elif figure == "rectangle":
#     a = float(input())
#     b = float(input())
#     area = a * b
# ....
# print(f"{area:.3f}")
