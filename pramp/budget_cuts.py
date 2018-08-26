def find_grants_cap(grantsArray, newBudget):
    total = sum(grantsArray)
    if newBudget >= total:
        return max(grantsArray)
    cap = round(1.0 * newBudget / len(grantsArray), 2)
    while True:
        new_total = sum([min(x, cap) for x in grantsArray])
        if new_total == newBudget:
            if int(cap) == cap:
                return int(cap)
            return cap
        elif new_total < newBudget:
            diff = newBudget - new_total
            cap += 1.0 * diff / len(grantsArray)
            cap = round(cap, 2)
        elif new_total > newBudget:
            diff = newBudget - new_total
            cap -= 1.0 * diff / len(grantsArray)
            cap = round(cap, 2)


def find_grants_cap2(grants_array, new_budget):
    grants_array.sort()
    min_total = len(grants_array) * grants_array[0]
    if min_total > new_budget:
        return new_budget / len(grants_array)
    return grants_array[0] + find_grants_cap(grants_array[1:], new_budget - min_total)


def main():
    gra = [2,100,50,120,1000]
    budget = 190
    print(find_grants_cap(gra, budget))


if __name__ == '__main__':
    main()
