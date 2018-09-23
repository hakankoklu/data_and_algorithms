"""A magic index in an array A[0 ... n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct
integers, write a method to find a magic index, if one exists, in array A.

FOLLOW UP: What if the values are not distinct?"""

def magic_index(lst):
    low, high = 0, len(lst)
    while low < high:
        mid = (low + high) // 2
        if lst[mid] == mid:
            return mid
        elif lst[mid] > mid:
            high = mid
        else:
            low = mid + 1
    return -1


arr = [int(x) for x in input().split()]
# print(magic_index(arr))