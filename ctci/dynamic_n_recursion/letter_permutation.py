"""Write a method to compute all permutations of a string of unique characters"""


def letter_permutations(word):
    lst = list(word)
    first_letter = lst[0]
    if len(lst) == 1:
        return [first_letter]
    result = []
    rem = ''.join(lst[1:])
    for perm in letter_permutations(rem):
        for i in range(len(perm)):
            a = perm[:i] + first_letter + perm[i:]
            result.append(a)
        result.append(perm + first_letter)
    return result


if __name__ == '__main__':
    pp = letter_permutations('abcde')
    print(pp)
    print(len(pp))
