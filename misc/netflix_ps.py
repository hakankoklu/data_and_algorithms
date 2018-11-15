"""Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:
0 < i, i + 1 < j, j + 1 < k < n - 1

Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5.
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
 NJAIN@NETFLIX.COM
 """


def is_temp(arr):
    if len(arr) < 6:
        return False
    for i in range(1, len(arr) - 5):
        target_sum = sum(arr[0:i])
        temp_sum2 = 0
        for j in range(i + 1, len(arr) - 3):
            temp_sum2 += arr[j]
            if temp_sum2 > target_sum:
                break
            elif temp_sum2 == target_sum:
                temp_sum3 = 0
                for k in range(j + 1, len(arr) - 1):
                    temp_sum3 += arr[k]
                    if temp_sum3 == target_sum:
                        temp_sum4 = sum(arr[k + 1:])
                        if temp_sum4 == target_sum:
                            return True
                    elif temp_sum3 > target_sum:
                        break
    return False

arr = [1,2,1,2,1,2,1]
print(is_temp(arr))