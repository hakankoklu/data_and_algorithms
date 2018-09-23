"""Given 3 arrays a, b, c return a string of 'yes', 'no' for if ai, bi and ci can form a triangle"""


def triangle_or_not(a, b, c):
    return [is_triangle(x, y, z) for x, y, z in zip(a, b, c)]


def is_triangle(x, y, z):
    if x + y <= z or x + z <= y or y + z <= x:
        return 'No'
    return 'Yes'


if __name__ == '__main__':
    a = [7, 10, 7]
    b = [2, 3, 4]
    c = [2, 7, 4]
    print(triangle_or_not(a, b, c))
