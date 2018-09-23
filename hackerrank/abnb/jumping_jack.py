import math


def jumping_jack(n, k):
    """
    n: step count
    k: bad stair
    """
    if k == 1:
        return int(n * (n + 1) / 2 - 1)
    sq = math.floor(math.sqrt(2 * k))
    if sq * (sq + 1) != 2 * k:
        return int(n * (n + 1) / 2)
    return int(n * (n + 1) / 2 - 1)


if __name__ == '__main__':
    print(jumping_jack(2, 2))
    print(jumping_jack(2, 1))
    print(jumping_jack(3, 3))
    print(jumping_jack(4, 6))