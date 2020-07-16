# medium

'''2020-07-16'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even_head = even = head.next
        while odd.next.next and even.next.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        if even.next:  # 共有奇数个节点
            odd.next = odd.next.next
            odd = odd.next
        odd.next = even_head
        even.next = None
        return head
