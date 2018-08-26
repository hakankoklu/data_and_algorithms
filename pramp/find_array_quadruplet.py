import itertools


def find_array_quadruplet(arr, s):
    if len(arr) < 4:
        return []
    arr.sort()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            two_sum = arr[i] + arr[j]
            if two_sum >= s:
                return []
            remaining = s - two_sum
            left = j + 1
            right = len(arr) - 1
            while left < right:
                if arr[left] + arr[right] == remaining:
                    return [arr[i], arr[j], arr[left], arr[right]]
                elif arr[left] + arr[right] > remaining:
                    right -= 1
                elif arr[left] + arr[right] < remaining:
                    left += 1
    return []


def find_array_quadruplet2(arr, s):
    if len(arr) < 4:
        return 0
    arr_hash = {}
    for num in arr:
        if num in arr_hash:
            arr_hash[num] += 1
        else:
            arr_hash[num] = 1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                three_sum = arr[i] + arr[j] + arr[k]
                if three_sum > s:
                    continue
                remaining = s - three_sum
                if remaining in arr_hash:
                    result = sorted([arr[i], arr[j], arr[k], remaining])
                    rem_count = sum([int(x == remaining) for x in result])
                    if arr_hash[remaining] >= rem_count:
                        return result
    return []


def main():
    arr = [2, 7, 4, 0, 9, 5, 1, 3]
    s = 20
    print(find_array_quadruplet(arr, s))
    print(find_array_quadruplet2(arr, s))


if __name__ == '__main__':
    main()
