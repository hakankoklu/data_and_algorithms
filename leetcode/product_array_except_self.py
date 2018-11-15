

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self._product(nums)

    def _product(self, nums):
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            if zero_count > 1:
                return [0] * len(nums)
        pro = 1
        for num in nums:
            if num != 0:
                pro *= num
        result = []
        for num in nums:
            if zero_count == 1:
                if num != 0:
                    result.append(0)
                else:
                    result.append(pro)
            else:
                result.append(pro // num)
        return result


if __name__ == '__main__':
    s = Solution()
    tests = [
        [1,2,3,4],
        [1,2,0,5,6],
        [1,0,0,4,5,100],
    ]
    for test in tests:
        print(s.productExceptSelf(test))