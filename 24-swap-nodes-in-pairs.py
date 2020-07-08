# medium

'''2020-02-10'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None: # 传进来空指针(链表长度为0)
            return head

        new_head = head.next #链表长度≥2时返回的新头
        if new_head == None: # 链表长度为1
            return head

        headnn = new_head.next
        if headnn == None: # 链表长度为2
            new_head.next = head #翻转
            head.next = None
            return new_head

        mid = head.next # 翻转的两个节点中的后一个，head为前一个，headnn为未翻转链表中的头
        while headnn and headnn.next: # headnn：长度为偶数时当headnn为空，不可再更新变量，若为空，短路算法不执行headnn.next，不会报错；
            mid.next = head # 翻转       headnn.next：长度为奇数时当headnn.next为空，不可再更新变量，此时headnn一定不为空
            head.next = headnn.next # 由于后面还要翻转，所以最终是当前的headnn.next在前，head在后

            head = headnn # 更新变量
            mid = head.next
            headnn = mid.next

        mid.next = head # 翻转(由于无法再更新变量所以放在循环外)
        head.next = headnn
        return new_head