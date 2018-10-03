"""
We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1. After V units of water fall at index K, how much water is at each index?

Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise at it's current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the terrain plus any water in that column.
We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.

Example 1:
Input: heights = [2,1,1,2,1,2,2], V = 4, K = 3
Output: [2,2,2,3,2,2,2]
Explanation:
#       #
#       #
##  # ###
#########
 0123456    <- index

The first drop of water lands at index K = 3:

#       #
#   w   #
##  # ###
#########
 0123456

When moving left or right, the water can only move to the same level or a lower level.
(By level, we mean the total height of the terrain plus any water in that column.)
Since moving left will eventually make it fall, it moves left.
(A droplet "made to fall" means go to a lower height than it was at previously.)

#       #
#       #
## w# ###
#########
 0123456

Since moving left will not make it fall, it stays in place.  The next droplet falls:

#       #
#   w   #
## w# ###
#########
 0123456

Since the new droplet moving left will eventually make it fall, it moves left.
Notice that the droplet still preferred to move left,
even though it could move right (and moving right makes it fall quicker.)

#       #
#  w    #
## w# ###
#########
 0123456

#       #
#       #
##ww# ###
#########
 0123456

After those steps, the third droplet falls.
Since moving left would not eventually make it fall, it tries to move right.
Since moving right would eventually make it fall, it moves right.

#       #
#   w   #
##ww# ###
#########
 0123456

#       #
#       #
##ww#w###
#########
 0123456

Finally, the fourth droplet falls.
Since moving left would not eventually make it fall, it tries to move right.
Since moving right would not eventually make it fall, it stays in place:

#       #
#   w   #
##ww#w###
#########
 0123456

The final answer is [2,2,2,3,2,2,2]:

    #
 #######
 #######
 0123456
"""


class Solution:

    def pourWater(self, heights, V, K):
        return self._pour_water(heights, V, K)

    def _pour_water(self, heights, v, k):
        if v == 0:
            return heights
        prev = heights[k]
        left_ind = k
        for i in range(k, -1, -1):
            if heights[i] < prev:
                prev = heights[i]
                left_ind = i
            elif heights[i] == prev:
                continue
            else:
                break

        prev = heights[k]
        right_ind = k
        for i in range(k, len(heights)):
            if heights[i] < prev:
                prev = heights[i]
                right_ind = i
            elif heights[i] == prev:
                continue
            else:
                break
        if heights[left_ind] < heights[k]:
            heights[left_ind] += 1
            return self._pour_water(heights, v - 1, k)
        elif heights[right_ind] < heights[k]:
            heights[right_ind] += 1
            return self._pour_water(heights, v - 1, k)
        else:
            heights[k] += 1
            return self._pour_water(heights, v - 1, k)


if __name__ == '__main__':
    s = Solution()
    tests = [
        ([2, 1, 1, 2, 1, 2, 2], 4, 3),
        ([1, 2, 3, 4], 2, 2),
        ([3, 1, 3], 5, 1),
        ([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 5, 5),
             ]
    for h, v, k in tests:
        print(s.pourWater(h, v, k))
