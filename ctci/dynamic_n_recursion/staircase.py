"""A child is running up a staircase with n steps, and can hop either one step, two steps or three steps at a
time. Implement a method to count how many possible ways to child can run up the stairs."""


def staircase(n):
    ways = [0, 1, 2, 4]
    if n <= 3:
        return ways[n]
    ways += [0] * (n - 3)
    for step in range(4, n + 1):
        ways[step] = ways[n - 1] + ways[n - 2] + ways[n - 3]
    return ways[-1]

steps = int(input())
print(staircase(steps))