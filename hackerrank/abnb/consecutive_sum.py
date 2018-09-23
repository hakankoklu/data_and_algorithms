"""Given an integer, find the number of ways to represent it as a sum of two or more consecutive positive integers"""


def consecutive_sum(num):
    print('Solving for: ', num)
    low = 1
    high = 2
    ways = 0
    s = 3
    while low < ((num // 2) + 1):
        if s == num:
            print(low, high)
            s -= low
            ways += 1
            low += 1
        elif s < num:
            high += 1
            s += high
        else:
            s -= low
            low += 1
    return ways


if __name__ == '__main__':
    print(consecutive_sum(15))
    print(consecutive_sum(250))
