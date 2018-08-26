def shifted_arr_search(shiftArr, num):
    left = 0
    right = len(shiftArr) - 1
    while True:
        mid = (left + right) // 2
        if shiftArr[mid] > shiftArr[mid + 1]:
            break
        elif shiftArr[mid] < shiftArr[0]:
            right = mid
        elif shiftArr[mid] > shiftArr[0]:
            left = mid
    max_ind = mid
    if num >= shiftArr[0]:
        left = 0
        right = max_ind
    else:
        left = max_ind + 1
        right = len(shiftArr)
    while True:
        mid = (left + right) // 2
        if shiftArr[mid] == num:
            break
        elif shiftArr[mid] > num:
            right = mid
        else:
            left = mid
        if left + 1 == right and shiftArr[left] != num and shiftArr[right] != num:
            return -1
    org_ind = mid - (max_ind + 1)
    if org_ind >= 0:
        return org_ind
    else:
        return org_ind + len(shiftArr)


def main():
    shifted_arr_search([9, 12, 17, 2, 4, 5], 4)


if __name__ == '__main__':
    main()
