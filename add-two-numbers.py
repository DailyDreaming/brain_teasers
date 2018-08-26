# https://leetcode.com/problems/add-two-numbers/description/
class ListNode(object):
    """Definition for singly-linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        myself = self
        num = str(myself.val)
        while myself.next:
            num += ' -> ' + str(myself.next.val)
            myself = myself.next
        return '(' + num + ')'


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.encodeNumber(self.decodeNumber(l1) + self.decodeNumber(l2))

    def decodeNumber(self, node):
        number = node.val
        i = 10
        while node.next:
            node = node.next
            number += node.val * i
            i *= 10
        return number

    def encodeNumber(self, num):
        assert isinstance(num, int)
        iter_number = str(num)
        node = None
        for i in iter_number:
            if node:
                new_node = ListNode(int(i))
                new_node.next = node
                node = new_node
            else:
                node = ListNode(int(i))
        return node
