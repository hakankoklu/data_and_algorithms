flip() = > True or False


# Returns 1,2,3,4,5 or 6, evenly distributed
def roll_die():
    (first, second, third) = int(flip()), int(flip()), int(flip())
    result = str(first) + str(second) + str(third)
    if result == ‘000’:
        return 1
    elif result == ‘001’:
        return 2
    elif result == ‘010’:
        return 3
    elif result == ‘011’:
        return 4
    elif result == ‘100’:
        return 5
    elif result == ‘110’:
        return 6
    else:
        return roll_die()


# update on 2018-7-27

def roll_die():
    result = int(flip()), int(flip()), int(flip())
    if result == (0, 0, 0):
        return 1
    elif result == (0, 0, 1):
        return 2
    elif result == (0, 1, 0):
        return 3
    elif result == (0, 1, 1):
        return 4
    elif result == (1, 0, 0):
        return 5
    elif result == (1, 1, 0):
        return 6
    else:
        return roll_die()


-------------

image = [[1, 2], [3, 4]]
transpose(image) = [[1, 3], [2, 4]]
clockwise90(image) = [[3, 1], [4, 2]]
fliplr(transpose(image))


def transpose(image):
    for row_ind, row in enumerate(image):
        for col_ind in range(row_ind, len(image)):
            temp = image[row_ind][col_ind]
        image[row_ind][col_ind] = image[col_ind][row_ind]


image[col_ind][row_ind] = temp
return image


def fliplr(image):
    for row in image:
        row.reverse()
    return image


def clockwise(image):
    return fliplr(transpose(image))


# update on 2018-7-27

def clockwise90(image):
    side = len(image)
    half = side // 2
    in_half = half if side % 2 == 0 else half + 1
    for i in range(half):
        for j in range(in_half):
            temp = image[i][j]
            image[i][j] = image[side - 1 - j][i]
            image[side - 1 - j][i] = image[side - 1 - i][side - 1 - j]
            image[side - 1 - i][side - 1 - j] = image[j][side - 1 - i]
            image[j][side - 1 - i] = temp
