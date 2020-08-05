# easy

'''2020-07-06'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_length(self, head: ListNode) -> int:
        length = 0
        current = head
        while current.next:
            length += 1
            current = current.next
        length += 1  # last node
        return length

    def middleNode(self, head: ListNode) -> ListNode:
        length = self.get_length(head)
        pos = length // 2
        current = head
        for i in range(pos):
            current = current.next
        return current
