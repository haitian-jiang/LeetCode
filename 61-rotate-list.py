# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # 令倒数第k个节点为新节点，尾结点接上原来头结点，倒数第k+1个节点为新的尾节点，即完成旋转
    def calc_len(self, pointer: ListNode) -> int:
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = self.calc_len(head)
        if length == 0 or k%length == 0: # 空列表或旋转后不变。判断空列表放在前面利用短路算法，否则可能出现除零错误
            return head
        k %= length # 找到截断的地方，k超过长度的话相当于循环
        p = head
        forward_index = length - k - 1 # 找倒数第k+1个节点
        while forward_index > 0:
            p = p.next
            forward_index -= 1
        new_head = p.next # 倒数第k个节点为新头
        p.next = None # 倒数第k+1个节点设为尾节点
        p = new_head # 从新头开始向后寻找原来的尾节点，把它跟原来的头结点接上
        while p.next:
            p = p.next
        p.next = head
        return new_head