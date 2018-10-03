"""Given an array of integers eg [1,2,-3,1] find whether there is a sub-sequence that
sums to 0 and return it (eg 1,2,-3 or 2,-3,1) Checking every sub-sequence is O(n^2) which
is too inefficient"""

count = 0


def subsequence_zero(arr):
    cache = {}
    return _subsequence(arr, 0, cache)


def _subsequence(arr, t, cache={}):
    global count
    count += 1
    if not arr:
        return False
    if arr[0] == t:
        return True
    tp_arr = (tuple(arr), t)
    if tp_arr in cache:
        return cache[tp_arr]
    first = _subsequence(arr[1:], t - arr[0], cache)
    rest = _subsequence(arr[1:], t, cache)
    result = first or rest
    cache[tp_arr] = result
    return result


if __name__ == '__main__':
    # arr = [1, 2, -5, -4, 3, 7, -1]
    arr = [1, 2, -3, 1]
    z = subsequence_zero(arr)
    print(z)
    print(count)
