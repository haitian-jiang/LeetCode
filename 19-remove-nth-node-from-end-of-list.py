# medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 两遍扫描链表
class Solution:
    def calc_len(self, pointer: ListNode) -> int:
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.calc_len(head)
        forward_index = length - n # 从头数是第几项（从0开始数）
        if forward_index == 0: # 如果删掉的是头，返回头后面一个节点
            return head.next
        p = head
        forward_index -= 1 # 找删去节点的前面一个节点，让p指向它
        while forward_index > 0:
            p = p.next
            forward_index -= 1
        if n == 1: # 如果删去的节点是最后一个，直接把在p处截断（未释放删去节点的内存空间）
            p.next = None
        else: # 否则让p的下一个为删去节点的下一个
            p.next = p.next.next
        return head

# 一遍扫描链表
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p, q  = head, head # 通过双指针，构造处差距为n，再同步后移，后一个指针移到最后时前一个指针找到位置
        while n > 0: # 要构造p的后面第n个为q。这样使得q指向最后一个节点时，p指向删去节点的前一个
            q = q.next
            n -= 1
        if q == None: # 如果此时q已经为最后一个节点的next，即None，说明n与链表长度相同，要删除的是头节点
            return head.next
        while q.next: # 否则删除的不是头节点，则两者一起前进
            q = q.next
            p = p.next
        p.next = p.next.next
        return head