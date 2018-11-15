"""
Given a list of integers, return all possible permutations (duplicate permutations are needed)
[1, 2, 3] return -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
[1, 2, 2] return -> [[1, 2, 2], [1, 2, 2], [2, 1, 2], [2, 2, 1], [2, 1, 2], [2, 2, 1]]

[1,2,3] [2, 3], [3, 2]
1, 2, 3   2, 1, 3   2, 3, 1
"""

# 1. filter out duplicates
"""
2.Given 6 integers ranging from 0 to 9, return the earliest time in 24 hours format that you can create from arranging them. If there is no valid combination, return ‘INVALID’. Duplicate integers are allowed in the list and every element should be used and only used once. 
For example, given [2, 2, 3, 4, 5, 6], return a string: ’22:34:56’. Given [1, 1, 1, 7, 8, 9], return a string: ’17:18:19’
"""


def get_perms(arr):
    if len(arr) <= 1:
        return [arr]
    perms = get_perms(arr[1:])
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            res = []
            res.extend(perm[:i])
            res.append(arr[0])
            res.extend(perm[i:])
            result.append(res)
    return result


def get_perms_non_dup(arr):
    all_perms = get_perms(arr)
    s = set()
    for perm in all_perms:
        s.add(tuple(perm))
    return list(s)


def get_earliest_time(arr):
    options = get_perms_non_dup(arr)
    options.sort()
    for option in options:
        if is_valid(option):
            return format_time(option)
    return 'INVALID'


def is_valid(option):
    option = [str(x) for x in option]
    hour = int(''.join(option[:2]))
    minute = int(''.join(option[2:4]))
    second = int(''.join(option[4:]))
    if hour < 24 and minute < 60 and second < 60:
        return True
    return False


def format_time(option):
    option = [str(x) for x in option]
    hour = ''.join(option[:2])
    minute = ''.join(option[2:4])
    second = ''.join(option[4:])
    return ':'.join([hour, minute, second])


# print(get_perms([1, 2, 3]))
# print(get_perms([1, 2, 2]))
# print(get_perms_non_dup([1, 2, 2]))

tests = [[2, 2, 3, 4, 5, 6], [2, 2, 2, 3, 8, 9], [4, 4, 4, 7, 8, 9]]
for test in tests:
    print(get_earliest_time(test))