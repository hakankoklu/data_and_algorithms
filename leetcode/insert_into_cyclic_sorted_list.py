class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        # empty list
        if not head:
            return Node(insertVal, None)
        # list with 1 node
        if not head.next:
            head.next = Node(insertVal, head)
            return head
        current = head
        nxt = current.next
        min_l = float("inf")
        max_l = -float("inf")
        min_node = None
        max_node = None
        found = True
        while not (current.val <= insertVal <= nxt.val):
            if current.val < min_l:
                min_l = current.val
                min_node = current
            if current.val > max_l:
                max_l = current.val
                max_node = current
            current, nxt = nxt, nxt.next
            if current == head:
                found = False
                break
        if found:
            node = Node(insertVal, nxt)
            current.next = node
        else:
            if min_node != max_node:
                node = Node(insertVal, min_node)
                max_node.next = node
            else:
                node = Node(insertVal, head.next)
                head.next = node
        return head


def make_list(arr):
    if not arr:
        return None
    head = Node(arr[0], None)
    current = head
    for num in arr[1:]:
        node = Node(num, None)
        current.next = node
        current = node
    current.next = head
    return head


if __name__ == '__main__':
    arr = [3, 3, 3]
    ll = make_list(arr)
    n = ll
    s = Solution()
    r = s.insert(n, 0)
    print(r)