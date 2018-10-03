"""Given an infinite number of quarters, dimes, nickels and pennies, write code to calculate the number of ways of
representing n cents."""


def change_ways(n):
    ways = [set([(0, 0, 0, 0)])]
    coins = [1, 5, 10, 25]
    if n <= 0:
        return 1
    for i in range(1, n + 1):
        new_ways = set()
        ways.append(new_ways)
        for ind, coin in enumerate(coins):
            if i - coin < 0:
                continue
            subways = ways[i - coin]
            for subway in subways:
                sub_lst = list(subway)
                sub_lst[ind] += 1
                sub_tp = tuple(sub_lst)
                new_ways.add(sub_tp)
    print(ways[n])
    return len(ways[n])


change = int(input())
print(change_ways(change))
