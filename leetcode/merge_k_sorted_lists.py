"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(arr):
    result = ListNode(arr[0])
    current = result
    for i in arr[1:]:
        temp = ListNode(i)
        current.next = temp
        current = current.next
    return result


class Solution:

    # def mergeKLists(self, lists):
    #     if len(lists) == 1:
    #         return lists[0]
    #     merged_lists = []
    #     for i in range(len(lists) // 2):
    #         l = self.merge_2_lists(lists[2 * i], lists[2 * i + 1])
    #         merged_lists.append(l)
    #     if len(lists) % 2 == 1:
    #         merged_lists.append(lists[-1])
    #     return self.mergeKLists(merged_lists)

    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(len(lists) // 2):
                l = self.merge_2_lists(lists[2 * i], lists[2 * i + 1])
                merged_lists.append(l)
            if len(lists) % 2 == 1:
                merged_lists.append(lists[-1])
            lists = merged_lists[:]
        return lists[0]

    def merge_2_lists(self, list1, list2):
        ptr1 = list1
        ptr2 = list2
        if ptr1 is None or ptr2 is None:
            if ptr1 is None:
                return ptr2
            return ptr1
        if ptr1.val < ptr2.val:
            result = ListNode(ptr1.val)
            ptr1 = ptr1.next
        else:
            result = ListNode(ptr2.val)
            ptr2 = ptr2.next
        current = result
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                temp_node =ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                temp_node = ListNode(ptr2.val)
                ptr2 = ptr2.next
            current.next = temp_node
            current = current.next
        if ptr1:
            current.next = ptr1
        else:
            current.next = ptr2
        return result


if __name__ == '__main__':
    l1 = make_list([1, 4, 5])
    l2 = make_list([1, 3, 4])
    l3 = make_list([2, 6])
    lists = [l1, l2, l3]
    ml = Solution().mergeKLists(lists)
    print(ml)
