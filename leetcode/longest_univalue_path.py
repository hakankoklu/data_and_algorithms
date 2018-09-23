"""Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000."""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def deserialize(s):
    return _deserialize(s.split())


def _deserialize(arr):
    if len(arr) == 0:
        return None
    root_value = arr.pop(0)
    if root_value == 'N':
        return None
    root = Node(root_value)
    root.left = _deserialize(arr)
    root.right = _deserialize(arr)
    return root


class Solution:
    def longest_univalue_path(self, t):
        if t:
            return self._longest_univalue_path(t)[0] - 1
        return 0

    def _longest_univalue_path(self, t):
        # base case
        if t is None:
            return 0, 0
        # recursion
        left_longest_length, left_longest_root_length = self._longest_univalue_path(t.left)
        right_longest_length, right_longest_root_length = self._longest_univalue_path(t.right)
        longest_length = 0
        if t.left and t.left.value == t.value:
            left_longest_root_length = left_longest_root_length + 1
        else:
            left_longest_root_length = 1
        if t.right and t.right.value == t.value:
            right_longest_root_length = right_longest_root_length + 1
        else:
            right_longest_root_length = 1
        longest_root_length = max(left_longest_root_length, right_longest_root_length)
        longest_length = max(longest_length, longest_root_length, left_longest_length, right_longest_length)
        if t.left and t.right and t.left.value == t.right.value == t.value:
            longest_length = max(longest_length, left_longest_root_length + right_longest_root_length - 1)
        return longest_length, longest_root_length


if __name__ == '__main__':
    # s = '5 4 N N 5 N N'
    # s = '5 4 1 N N 1 N N 5 N 5 N N'
    s = '1 4 4 N N 4 N N 5 5 N N 5 N 5 N N'
    t = deserialize(s)
    print(Solution().longest_univalue_path(t))