def check_complete_cycle(arr):
    if len(arr) == 1:
        return True
    start = 0
    current = 0
    for i in range(len(arr)):
        current = move(arr, current, arr[current])
        if current == next:
            return False
    return start == current


def move(arr, start, steps):
    end = start + steps
    return end % len(arr)


if __name__ == '__main__':
    tests = [
        [1, 1, 1, 1],
        [2, 2, -1],
        [5, -4, -1],
        [2],
        [2, 4, 1],
        [2, 3, -2, 1]
    ]
    for test in tests:
        print(check_complete_cycle(test))
