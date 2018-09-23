def prefix_suffix_sim(s):
    total = 0
    for i in range(len(s)):
        total += check_similarity(s, s[i:])
    return total


def check_similarity(s1, s2):
    count = 0
    for l1, l2 in zip(s1, s2):
        if l1 == l2:
            count += 1
        else:
            return count
    return count


if __name__ == '__main__':
    print(prefix_suffix_sim('aa'))
    print(prefix_suffix_sim('ababa'))
    print(prefix_suffix_sim('ababaa'))
