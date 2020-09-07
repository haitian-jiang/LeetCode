# easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''2020-09-07'''
class Solution:  # O(N) of time and space
    def hasCycle(self, head: ListNode) -> bool:
        id_list = [id(head)]
        curr = head
        while curr and curr.next:  # in case the head is None
            if id(curr.next) in id_list:
                return True
            curr = curr.next
            id_list.append(id(curr))
        return False

'''2020-09-07'''
class Solution:  # O(1) of space
    def hasCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while slow and fast:
            if not slow.next or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False