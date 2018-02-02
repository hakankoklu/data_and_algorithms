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


def length_of_longest_non_repeating_substring(s):
    """
    :type s: str
    :rtype: int
    """
    used_chars = {}
    head = max_len = 0
    for i, ch in enumerate(s):
        if ch in used_chars and head <= used_chars[ch]:
            head = used_chars[ch] + 1
        else:
            max_len = max(max_len, i - head + 1)
        used_chars[ch] = i
    return max_len


pals = set([''])
def is_pal(s):
    if len(s) <= 1:
        pals.add(s)
        return True
    if len(s) == 2 and s[0] == s[1]:
        pals.add(s)
        return True
    if s[0] == s[-1] and (s[1:-1] in pals or is_pal(s[1:-1])):
        pals.add(s)
        return True
    return False


def longest_palindromic_substring(s):
    """
    :type s: str
    :rtype: str
    """
    max_pal = ''
    for pal_len in range(1, len(s) + 1):
        for i in range(len(s) - pal_len + 1):
            if s[i:i + pal_len] != max_pal and is_pal(s[i:i + pal_len]):
                max_pal = s[i:i + pal_len]
    return max_pal


def plus_one(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits = [str(x) for x in digits]
    num = int(''.join(digits))
    num += 1
    return [int(x) for x in str(num)]


def is_power_of_two(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    if n == 1:
        return True
    while n % 2 == 0:
        n = n / 2
        if n == 1:
            return True
    return False


def is_power_of_three(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    while n % 3 == 0:
        n = n / 3
    return n == 1


def reverse_vowels(s):
    """
    :type s: str
    :rtype: str
    """
    vows = 'aeiouAEIOU'
    evows = []
    for ch in s:
        if ch in vows:
            evows.append(ch)
    new_chars = []
    for ch in s:
        if ch in vows:
            new_chars.append(evows.pop())
        else:
            new_chars.append(ch)
    return ''.join(new_chars)

GTARGET = 1
def guess(num):
    if num == GTARGET:
        return 0
    elif num < GTARGET:
        return 1
    else:
        return -1


def guess_number(n):
    """
    :type n: int
    :rtype: int
    """
    if guess(n) == 0:
        return n
    min_g = 1
    max_g = n
    g = (n + 1) // 2
    resp = guess(g)
    while resp != 0:
        if resp == 1:
            min_g = max(min_g, g)
            g = (g + max_g) // 2
        elif resp == -1:
            max_g = min(max_g, g)
            g = (g + min_g) // 2
        resp = guess(g)
    return g


def first_uniq_char(s):
    """
    :type s: str
    :rtype: int
    """
    chars = {}  # {ch: [count, ind]}
    for ind, ch in enumerate(s):
        if ch in chars:
            chars[ch][0] += 1
        else:
            chars[ch] = [1, ind]
    mind = len(s)
    for k, v in chars.items():
        if v[0] == 1 and v[1] < mind:
            mind = v[1]
    if mind == len(s):
        return -1
    return mind


def find_missing_numbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    arr = [0] * len(nums)
    for num in nums:
        arr[num - 1] = 1
    res = []
    for ind, num in enumerate(arr):
        if num == 0:
            res.append(ind + 1)
    return res


def island_perimeter(grid):
    per = 0
    for rind, row in enumerate(grid):
        for cind, col in enumerate(row):
            if col == 1:
                per += 4
                if rind - 1 >= 0 and grid[rind - 1][cind] == 1:
                    per -= 1
                if rind + 1 < len(grid) and grid[rind + 1][cind] == 1:
                    per -= 1
                if cind - 1 >= 0 and row[cind - 1] == 1:
                    per -= 1
                if cind + 1 < len(row) and row[cind + 1] == 1:
                    per -= 1
    return per


def judge_circle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    UD = 0
    LR = 0
    for ch in moves:
        if ch == 'U':
            UD += 1
        elif ch == 'D':
            UD -= 1
        elif ch == 'R':
            LR += 1
        elif ch == 'L':
            LR -= 1
    return (UD, LR) == (0, 0)
    # one liner:
    # return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


def anagram_mapping1(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    P = []
    for val in A:
        P.append(B.index(val))
    return P


def anagram_mapping2(A, B):
    Bmap = {}
    for ind, val in enumerate(B):
        Bmap[val] = ind
    P = []
    for val in A:
        P.append(Bmap[val])
    return P


def letter_combinations(digits):
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if not digits:
        return []
    if len(digits) == 1:
        return list(digit_map[digits[0]])
    sub_letters = letter_combinations(digits[1:])
    res = []
    for ch in digit_map[digits[0]]:
        for comb in sub_letters:
            res.append(ch + comb)
    return res


def generate_parenthesis(n):
    if n == 0:
        return []
    if n == 1:
        return ['()']
    prev = generate_parenthesis(n-1)
    new_set = set()
    for paren in prev:
        new_set.add('()' + paren)
        new_set.add(paren + '()')
        new_set.add('(' + paren + ')')
    return list(new_set)


def my_pow(x, n):
    if n == 0:
        return 1
    res = 1
    for i in range(n):
        res *= x
    return res


def my_pow_dp(x, n):
    pow_cache = {0: 1, 1: x}
    def my_pow_in(x, n):
        if n in pow_cache:
            return pow_cache[n]
        if n % 2 == 0:
            base = my_pow_in(x, n / 2)
            result = base  * base
            pow_cache[n] = result
            return result
        else:
            base = my_pow_in(x, n / 2)
            result = base  * base * x
            pow_cache[n] = result
            return result
    return my_pow_in(x, n)


def get_perms(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    perms = get_perms(nums[1:])
    res = []
    for perm in perms:
        for i in range(len(perm) + 1):
            new_perm = perm[:]
            new_perm.insert(i, nums[0])
            res.append(new_perm)
    return res


def next_permutation_full_brute(nums):
    unsorted_perms = get_perms(nums)
    all_perms_int = [int(''.join([str(x) for x in perm])) for perm in unsorted_perms]
    deduped = list(set(all_perms_int))
    deduped.sort()
    current = int(''.join([str(x) for x in nums]))
    c = deduped.index(current)
    if c == len(deduped) - 1:
        return deduped[0]
    return deduped[c + 1]


def next_permutation_in_place(nums):
    prev = nums[0]
    ordered = True
    for num in nums[1:]:
        if num > prev:
            ordered = False
            break
        prev = num
    if ordered:
        nums.reverse()
    else:
        prev = nums[-1]
        for ind in range(len(nums) - 2, -1, -1):
            if prev > nums[ind]:
                break
            prev = nums[ind]
        temp = nums[ind]
        target_ind = get_next_bigger_digit(nums, ind)
        nums[ind] = nums[target_ind]
        nums[target_ind] = temp
        sub = nums[ind+1:]
        sub.sort()
        nums[ind + 1:] = sub


def get_next_bigger_digit(nums, ind):
    target = nums[ind]
    res = 10
    res_ind = 0
    for i_ind, i in enumerate(nums[ind + 1:], ind + 1):
        if i > target and i < res:
            res = i
            res_ind = i_ind
    return res_ind


def spiral_order(matrix):
    if not matrix:
        return []
    start = [0, 0]
    direction = 'r'
    row_lims = [0, len(matrix) - 1]
    col_lims = [0, len(matrix[0]) - 1]
    total = (row_lims[1] + 1) * (col_lims[1] + 1)
    print(total)
    count = 0
    res = []
    while count < total:
        if direction == 'r':
            for i in range(col_lims[0], col_lims[1] + 1):
                res.append(matrix[row_lims[0]][i])
                count += 1
            row_lims[0] += 1
            direction = 'd'
        elif direction == 'd':
            for i in range(row_lims[0], row_lims[1] + 1):
                res.append(matrix[i][col_lims[1]])
                count += 1
            col_lims[1] -= 1
            direction = 'l'
        elif direction == 'l':
            for i in range(col_lims[1], col_lims[0] - 1, -1):
                res.append(matrix[row_lims[1]][i])
                count += 1
            row_lims[1] -= 1
            direction = 'u'
        elif direction == 'u':
            for i in range(row_lims[1], row_lims[0] - 1, -1):
                res.append(matrix[i][col_lims[0]])
                count += 1
            col_lims[0] += 1
            direction = 'r'
        print(res)
    return res


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x.start)
    if len(intervals) == 0:
        return []
    elif len(intervals) == 1:
        return intervals
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval.start <= result[-1].end:
            temp = Interval(result[-1].start, max(interval.end, result[-1].end))
            result[-1] = temp
        else:
            result.append(interval)
    return result


def word_break(s, word_list):
    matches = [x for x in word_list if s.startswith(x)]
    if not matches:
        return False
    if matches[0] == s:
        return True
    return any([word_break(s[len(x):], word_list) for x in matches])


def find_peak_element_n(nums):
    if len(nums) == 1:
        return 0
    for i in range(len(nums)):
        if i == 0 and nums[i] > nums[i + 1]:
            return i
        if i == (len(nums) - 1) and nums[i] > nums[i - 1]:
            return i
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i


def find_peak_element_logn(nums):
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1
    start = 0
    end = len(nums) - 1
    med = (start + end) // 2
    while True:
        if nums[med] > nums[med - 1] and nums[med] > nums[med + 1]:
            return med
        if nums[med + 1] > nums[med]:
            start = med
        elif nums[med - 1] > nums[med]:
            end = med
        med = (start + end) // 2


def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return '0'
    positive = (numerator == abs(numerator)) == (denominator == abs(denominator))
    numerator = abs(numerator)
    denominator = abs(denominator)
    digits = []
    nums = {numerator: 0}
    digits.append(numerator // denominator)
    remainder = numerator % denominator
    count = 0
    repeat = -1
    while remainder != 0:
        count += 1
        numerator = remainder * 10
        if numerator in nums:
            repeat = nums[numerator]
            break
        digits.append(numerator // denominator)
        remainder = numerator % denominator
        nums[numerator] = count
    if len(digits) == 1:
        if positive:
            return str(digits[0])
        return '-' + str(digits[0])
    if repeat == -1:
        if positive:
            return str(digits[0]) + '.' + ''.join([str(x) for x in digits[1:]])
        return '-' + str(digits[0]) + '.' + ''.join([str(x) for x in digits[1:]])
    repeat_str = '(' + ''.join([str(x) for x in digits[repeat:]]) + ')'
    if positive:
        return str(digits[0]) + '.' + ''.join([str(x) for x in digits[1:repeat]]) + repeat_str
    return '-' + str(digits[0]) + '.' + ''.join([str(x) for x in digits[1:repeat]]) + repeat_str


def hamming_distance(x, y):
    # xxory = x ^ y
    # bxor = bin(xxory)
    # return sum([int(x) for x in bxor[2:]])
    return bin(x^y).count('1')


def reverse_linked_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    n = head
    nodes = [n]
    while n.next:
        nodes.append(n.next)
        n = n.next
    head = nodes[-1]
    prev = head
    for node in reversed(nodes[:-1]):
        prev.next = node
        prev = node
    prev.next = None
    return head


def move_zeroes(nums):
    z_count = nums.count(0)
    if not z_count:
        return
    pt = 0
    for ind, num in enumerate(nums):
        if num != 0:
            nums[pt] = num
            pt += 1
    nums[pt:] = [0] * z_count



def count_nums(seq):
    if len(seq) == 1:
        return str(1) + str(seq[0])
    res = ''
    start = 0
    prev = seq[0]
    for i, s in enumerate(seq[1:], 1):
        if s != prev:
            res += str(i - start)
            res += str(prev)
            start = i
            prev = s
    res += str(i - start + 1)
    res += str(s)
    return res


def count_and_say(n):
    res = '1'
    for i in range(n-1):
        res = count_nums(res)
    return res


def max_profit(prices):
    if len(prices) <= 1:
        return 0
    profit = 0
    base = prices[0]
    for price in prices[1:]:
        profit = max(profit, price - base)
        base = min(base, price)
    return profit


def add_binary(a, b):
    c = str(int(a) + int(b))
    car = 0
    res = []
    for i in reversed(list(c)):
        digit = (int(i) + car) % 2
        car = (int(i) + car) // 2
        res.append(digit)
    if car:
        res.append(car)
    res.reverse()
    return ''.join([str(x) for x in res])


def str_str(haystack, needle):
    if haystack == needle or needle == '':
        return 0
    for i, hay in enumerate(haystacks):
        if i + len(needle) > len(haystack):
            break
        if hay == needle[0]:
            match = True
            for j, let in enumerate(needle):
                if let != haystack[i + j]:
                    match = False
                    break
            if match:
                return i
    return -1


def is_palindrome(s):
    if len(s) <= 1:
        return True
    s = s.lower()
    valids = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    lets = []
    for let in s:
        if let in valids:
            lets.append(let)
    if len(lets) <= 1:
        return True
    # return lets == list(reversed(lets))
    left = 0
    right = len(lets) - 1
    while left < right:
        if lets[left] != lets[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_linked(head):
    if not head or not head.next:
        return True
    length = 1
    top = head
    while top.next:
        length += 1
        top = top.next
    if length == 2:
        return head.val == head.next.val
    elif length == 3:
        return head.val == head.next.next.val
    prev = head
    future = prev.next
    prev.next = None
    for i in range(length // 2 - 1):
        temp = future.next
        future.next = prev
        prev = future
        future = temp
    if length % 2 == 1:
        future = future.next
    while prev:
        if prev.val != future.val:
            return False
        prev = prev.next
        future = future.next
    return True


def merge_sorted_arrays_inp(nums1, m, nums2, n):
    m = len(nums1)
    n = len(nums2)
    if not nums2:
        return
    for i in range(n):
        nums1.append(-10000000)
    c1 = m - 1
    c2 = n - 1
    for i in range(m+n-1, -1, -1):
        if nums1[c1] >= nums2[c2]:
            nums1[i] = nums1[c1]
            c1 -= 1
        else:
            nums1[i] = nums2[c2]
            c2 -= 1
        if c2 == -1:
            return
        if c1 == -1:
            nums1[:i] = nums2[:c2]
            return


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order(root):
    result = [root]
    if root.left:
        result.extend(pre_order(root.left))
    if root.right:
        result.extend(pre_order(root.right))
    return result


def lowest_common_ancestor_bt(root, p, q):
    path_to_root = []
    pre = pre_order(root)
    root_to_p = [p]
    pind = pre.index(p)
    for i in range(pind-1, -1, -1):
        if pre[i].left == p or pre[i].right == p:
            root_to_p.append(pre[i])
            p = pre[i]
    root_to_p.reverse()
    root_to_q = [q]
    qind = pre.index(q)
    for i in range(qind-1, -1, -1):
        if pre[i].left == q or pre[i].right == q:
            root_to_q.append(pre[i])
            q = pre[i]
    root_to_q.reverse()
    prev = root
    for p, q in zip(root_to_p, root_to_q):
        if p != q:
            return prev
        prev = p
    return prev


def lowest_common_ancestor_bst(root, p, q):
    if p == root or q == root:
        return root
    if (p.val < root.val) != (q.val < root.val):
        return root
    if p.val < root.val:
            root = root.left
    else:
        root = root.right
    return lowest_common_ancestor_bst(root, p, q)


def sqrt(x):
    # very shitty but I am tired, I should do this with binary
    if not x:
        return 0
    if x < 4:
        return 1
    if x < 9:
        return 2
    if x < 16:
        return 3
    digits = len(str(x))
    top = 10 ** (digits // 2)
    top = top * 3.5 if digits % 2 else top
    bottom = top // 3.5
    med = (bottom + top) // 2
    while bottom < top:
        if med * med == x:
            return int(med)
        if med * med < x:
            bottom = med
        else:
            top = med
        if med == (bottom + top) // 2:
            return int(med)
        med = (bottom + top) // 2


def convert_to_title(n):
    let_map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = []
    while n > 0:
        rem = n % 26
        if rem == 0:
            rem = 26
            n -= 26
        digits.append(rem)
        n = n // 26
    digits.reverse()
    return ''.join([let_map[x-1] for x in digits])


def isBadVersion(n):
    return True


def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    first = 0
    last = n - 1
    med = (first + last) // 2
    while first < last:
        if isBadVersion(med + 1):
            if med == 0:
                return 1
            if not isBadVersion(med):
                return med + 1
            last = med
        else:
            if first == med:
                first += 1
            else:
                first = med
        med = (first + last) // 2
    return med + 1


def repeated_string_match(A, B):
    rep = len(B) // len(A)
    for i in range(rep, rep + 3):
        if B in i * A:
            return i
    return -1


def get_repeated_perms(nums, length):
    result = {str(num) for num in nums}
    for i in range(length - 1):
        temp = set()
        for num in nums:
            for s in result:
                temp.add(s + str(num))
        result = temp
    return result


def is_valid(time):
    if int(time[0]) > 2:
        return False
    if int(time[0]) == 2 and int(time[1]) > 3:
        return False
    if int(time[3]) > 5:
        return False
    return True


def next_closest_time(time):
    nums = {int(x) for x in time if x.isdigit()}
    if len(nums) == 1:
        return time
    perms = get_repeated_perms(nums, 4)
    valid_perms = {x for x in perms if is_valid(str(x)[:2] + ':' + str(x)[2:])}
    perms_int = {int(perm) for perm in valid_perms}
    simple_time_int = int(time[:2] + time[3:])
    min_diff = 10000
    min_t = 0
    for perm in perms_int:
        if perm < simple_time_int:
            perm += 2400
        diff = perm - simple_time_int
        if diff < min_diff and diff != 0:
            min_diff = diff
            min_t = perm if perm < 2400 else perm - 2400
    min_t = str(min_t)
    if len(min_t) == 3:
        min_t = '0' + min_t
    if len(min_t) == 2:
        min_t = '00' + min_t
    if len(min_t) == 1:
        min_t = '000' + min_t
    if len(min_t) == 0:
        min_t = '0000'
    return min_t[:2] + ':' + min_t[2:]
    # this became horrible but don't have time to go back to clean up