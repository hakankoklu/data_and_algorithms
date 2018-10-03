"""
Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
Output: [1,2,3,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,2,3,4,5,6].
"""


class Vector2D:

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.vec = [x for x in self.vec if x]

    def next(self):
        """
        :rtype: int
        """
        res = self.vec[0].pop(0)
        if not self.vec[0]:
            self.vec.pop(0)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.vec)


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    inp = [
        [1, 2],
        [3],
        [4, 5, 6]
    ]
    i, v = Vector2D(inp), []
    while i.hasNext():
        v.append(i.next())
    print(v)
