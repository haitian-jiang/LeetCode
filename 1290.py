# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node_list = []
        current = head
        while current.next:
            node_list.append(current.val)
            current = current.next
        node_list.append(current.val)  # the last node
        node_list = map(str, node_list)  # convert List[int] into List[str]
        return int(''.join(node_list), 2)
