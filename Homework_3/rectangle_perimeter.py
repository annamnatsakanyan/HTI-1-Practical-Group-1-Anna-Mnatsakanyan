import math


def segment_length(x1, y1, x2, y2):
    side = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return side


def rectangle_premier(coordinate):
    premier = 2*(segment_length(coordinate[0], coordinate[1], coordinate[2], coordinate[3]) + segment_length(
        coordinate[2], coordinate[3], coordinate[4], coordinate[5]))
    return premier


coordinates = [float(elem) for elem in input("enter the coordinates: ").split()]
print(rectangle_premier(coordinates))
