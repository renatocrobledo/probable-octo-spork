'''
    Giving a internal angle of a regular polygon calculate the number of sides
    (a regular polygon is a polygon with same quantity of )

'''


def calculate_sides():
    internal_angle = int(input())
    return str(int(360 / (180 - internal_angle)))