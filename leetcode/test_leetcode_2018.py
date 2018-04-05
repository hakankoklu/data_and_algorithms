import pytest
from data_and_algorithms.leetcode.leetcode_2018 import *

def get_linked_list(val_arr):
    if not val_arr:
        return None
    head = ListNode(val_arr[0])
    top = head
    for i in val_arr[1:]:
        top.next = ListNode(i)
        top = top.next
    return head


@pytest.mark.parametrize(
    'input, result',
    [
        ('pa', False),
        ('pald', False),
        ('palind', False),
        ('p', True),
        ('', True),
        ('lapal', True),
    ])
def test_is_palindrome_linked(input, result):
    assert is_palindrome_linked(get_linked_list(input)) == result


@pytest.mark.parametrize(
    'arr1, arr2, result',
    [
        ([], [], []),
        ([1], [], [1]),
        ([], [1], [1]),
        ([1], [2], [1,2]),
        ([1,3,5,7,8,11], [2,4,6,9,13], [1,2,3,4,5,6,7,8,9,11,13]),
    ])
def test_merge_sorted_arrays_inp(arr1, arr2, result):
    merge_sorted_arrays_inp(arr1, 1, arr2, 1)
    assert arr1 == result


def test_lowest_common_ancestor_bt():
    r = TreeNode(1)
    rl = TreeNode(2)
    r.left = rl
    assert lowest_common_ancestor_bt(r, r, rl) == r
    rr = TreeNode(3)
    r.right = rr
    assert lowest_common_ancestor_bt(r, r, rr) == r
    assert lowest_common_ancestor_bt(r, rl, rr) == r
    rll = TreeNode(4)
    rlll = TreeNode(5)
    rlr = TreeNode(6)
    rl.left = rll
    rll.left = rlll
    rl.right = rlr
    assert lowest_common_ancestor_bt(r, rlll, rlr) == rl


def test_pre_order():
    r = TreeNode(1)
    rl = TreeNode(2)
    rr = TreeNode(3)
    rll = TreeNode(4)
    rlll = TreeNode(5)
    rlr = TreeNode(6)
    rrl = TreeNode(7)
    rrr = TreeNode(8)
    r.left = rl
    r.right = rr
    rl.left = rll
    rl.right = rlr
    rll.left = rlll
    rr.left = rrl
    rr.right = rrr
    result = pre_order(r)
    expected = [1,2,4,5,6,3,7,8]
    for ind, n in enumerate(result):
        n.val = expected[ind]


def test_lowest_common_ancestor_bst():
    r = TreeNode(5)
    rl = TreeNode(3)
    r.left = rl
    print([x.val for x in pre_order(r)])
    assert lowest_common_ancestor_bst(r, r, rl) == r
    rr = TreeNode(6)
    r.right = rr
    print([x.val for x in pre_order(r)])
    assert lowest_common_ancestor_bst(r, r, rr) == r
    assert lowest_common_ancestor_bst(r, rl, rr) == r
    rll = TreeNode(2)
    rlll = TreeNode(1)
    rlr = TreeNode(4)
    rl.left = rll
    rll.left = rlll
    rl.right = rlr
    print([x.val for x in pre_order(r)])
    assert lowest_common_ancestor_bst(r, rlll, rlr) == rl


@pytest.mark.parametrize(
    'n, res',
    [
        (3, 'C'),
        (26, 'Z'),
        (27, 'AA'),
        (52, 'AZ'),
        (701, 'ZY')
    ])
def test_convert_to_title(n, res):
    assert convert_to_title(n) == res

@pytest.mark.parametrize(
    'time, result',
    [
        ('34:56', False),
        ('19:39', True),
        ('18:67', False),
        ('27:56', False),
        ('01:45', True)
    ])
def test_is_valid(time, result):
    assert is_valid(time) == result


def test_get_root_path():
    r = TreeNode(1)
    pre = pre_order(r)
    assert get_root_path(pre, r) == [r]
    rl = TreeNode(2)
    rr = TreeNode(3)
    r.left = rl
    r.right = rr
    pre = pre_order(r)
    assert get_root_path(pre, rl) == [rl, r]
    assert get_path(pre, r, rl) == [r, rl] or get_path(pre, r, rl) == [rl, r]
    assert get_path(pre, rr, rl) == [rr, r, rl] or get_path(pre, rr, rl) == [rl, r, rr]
    rll = TreeNode(4)
    rl.left = rll
    pre = pre_order(r)
    assert get_root_path(pre, rll) == [rll, rl, r]