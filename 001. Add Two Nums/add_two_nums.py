#!python3

"""
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l_header = None
        carry_out = 0
        while True:
            res = l1.val + l2.val + carry_out
            if res > 9:
                carry_out = 1
                l_tmp = ListNode(res - 10)

            else:
                carry_out = 0
                l_tmp = ListNode(res)

            if l_header is None:
                l_header = l_tmp
                l_res = l_tmp
            else:
                l_res.next = l_tmp
                l_res = l_res.next

            if l1.next is None and l2.next is None and carry_out == 0:
                return l_header
            else:
                if l1.next is None:
                    l1.val = 0
                else:
                    l1 = l1.next
                if l2.next is None:
                    l2.val = 0
                else:
                    l2 = l2.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = Solution().addTwoNumbers(l1, l2)

    l1 = ListNode(5)
    l2 = ListNode(5)
    res = Solution().addTwoNumbers(l1, l2)


