def two_sum(nums, target):
    """
    :type strs: (list[int], int)
    :rtype: list[int]
    """
    seen = {}
    for ind, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], ind]
        seen[num] = ind


def reverse_integer(x):
    """
    :type strs: int
    :rtype: int
    """
    digits = []
    is_positive = True if x > 0 else False
    x = -1 * x if not is_positive else x
    while x != 0:
        digits.append(x % 10)
        x = x // 10
    exps = [len(digits) - 1 - ind for ind, _ in enumerate(digits)]
    exps = [10 ** i for i in exps]
    result = sum([a * b for a,b in zip(digits, exps)])
    result = -1 * result if not is_positive else result
    if result < -(2 ** 31) or result > (2 ** 31 - 1):
        return 0
    return result


def get_int_length(x):
    """For positive only"""
    """
    :type strs: int
    :rtype: int
    """
    if x < 0:
        raise ValueError("Negative numbers are not accepted!")
    count = 1
    while x // 10 ** count > 0:
        count += 1
    return count


def palindrome_integer(x):
    """Negatives cannot be palindrome, did not use str to keep O(1) space"""
    """
    :type strs: int
    :rtype: bool
    """
    if x < 0:
        return False
    tens = get_int_length(x) - 1
    if tens == 0:
        return True
    start = 0
    end = tens
    while start < end:
        front = (x // 10 ** (tens - start)) % 10
        back = (x // 10 ** (tens - end)) % 10
        if front != back:
            return False
        start += 1
        end -= 1
    return True


def roman_to_int(x):
    """
    :type strs: str
    :rtype: int
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    negs = {'I': {'V', 'X'}, 'X': {'L', 'C'}, 'C': {'D', 'M'}}
    res = 0
    for ind, ch in enumerate(x):
        val = roman_map[ch]
        if ch in negs and ind + 1 < len(x) and x[ind + 1] in negs[ch]:
            val *= -1
        res += val
    return res


def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    """Assume all the strs have a common prefix otherwise return empty string"""
    if not strs:
        return ''
    prefix = strs[0]
    for s in strs:
        ind = 0
        while ind < len(s) and ind < len(prefix) and s[ind] == prefix[ind]:
            ind += 1
        prefix = prefix[:ind]
    return prefix


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    co = 0
    r = ListNode(0)
    temp = r
    prev = r
    while not (l1 is None and l2 is None):
        d1 = l1.val if l1 else 0
        d2 = l2.val if l2 else 0
        total = d1 + d2 + co
        s = total % 10
        co = total // 10
        temp.val = s
        next_node = ListNode(0)
        temp.next = next_node
        prev = temp
        temp = next_node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    temp.val = co
    prev.next = None if not co else temp
    return r


def valid_parenthesis(s):
    """
    :type s: str
    :rtype: bool
    """
    parens = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs and (not parens or pairs[ch] != parens[-1]):
            return False
        elif ch in pairs and pairs[ch] == parens[-1]:
            parens.pop()
        else:
            parens.append(ch)
    if parens:
        return False
    return True


def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    prev = nums[0]
    prev_pt = 0
    for i, num in enumerate(nums[1:], 1):
        if num != prev:
            prev_pt += 1
            nums[prev_pt] = num
            prev = num
    return prev_pt + 1, nums