# hard
import queue
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''2020-10-30'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = queue.PriorityQueue()
        for i in range(len(lists)):
            if lists[i] is None:  # if lists = [None], q is empty, return head.next = None
                continue
            q.put((lists[i].val, i, lists[i]))  # i to distinguish node with same val
        head = tail = ListNode()  # dumb node
        while not q.empty():
            item = q.get()
            new_node = item[2]
            list_index = item[1]
            next_node = new_node.next
            tail.next = new_node
            tail = tail.next
            if next_node is not None:
                q.put((next_node.val, list_index, next_node))
        return head.next
