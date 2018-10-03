'''
 This class will be given a list of words (such as might be tokenized
 * from a paragraph of text), and will provide a method that takes two
 * words and returns the shortest distance (in words) between those two
 * words in the provided text.
 * Example:
 *   finder = ["the", "quick", "brown", "fox", "quick"];
 *   assert(distance("fox", "the") == 3);
 *   assert(distance("quick", "fox") == 1);
 *
 * "quick" appears twice in the input. There are two possible distance values for "quick" and "fox":
 *     (3 - 1) = 2 and (4 - 3) = 1.
 * Since we have to return the shortest distance between the two words we return 1.


 quick = None, 4
 fox = None, 3
 dist = 1
 '''


def distance(arr, word1, word2):
    min_distance = 999999
    # Code
    indices1 = find_indices(arr, word1)
    indices2 = find_indices(arr, word2)
    if not indices1 or not indices2:
        return -1
    for i in indices1:
        for j in indices2:
            min_distance = min(abs(i - j), min_distance)
    return min_distance


def find_indices(arr, word):
    indices = []
    for ind, elm in enumerate(arr):
        if elm == word:
            indices.append(ind)
    return indices


def distance2(arr, word1, word2):
    min_dist = 999999999
    ind1 = None
    ind2 = None
    for ind, elm in enumerate(arr):
        if elm == word1:
            ind1 = ind
        if elm == word2:
            ind2 = ind
        if ind1 != None and ind2 != None:
            min_dist = min(abs(ind1 - ind2), min_dist)
    if ind1 is None or ind2 is None:
        return -1
    return min_dist


"""

N elements, N/2, N/2, O(N^2)

[      x   x     y     x     y     x     x     y    y]

{word1: [4, 6, 7],
word2: [1, 5]} O(N)

{(word1, word2): 4,
(word)}

1% spam

99% spam
99% not spam

99 1
0.99 0.99 

"""