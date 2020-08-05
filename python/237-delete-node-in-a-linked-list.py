# easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''2020-07-16'''
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next and node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
