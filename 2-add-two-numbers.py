# medium
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0 # 存放进位
        head = ListNode(0) # 空头结点
        pointer = head # pointer指向当前节点
        while(l1 and l2): # 先加l1和l2共有的数位，当l1或l2有一个数位全部算完即跳出循环
            new_node = ListNode(0)  # 创建新节点，放本次循环中加得的数。若不采用空头结点，则每次加完数存好后建立下一个结点，最终会有循环结束是创建的空节点。
            pointer.next = new_node # 将新节点连接至现有链表的尾结点
            pointer = pointer.next  # 更新当前节点至新节点
            value = l1.val + l2.val + temp 
            pointer.val = value % 10 # 赋值并更新
            temp = value // 10
            l1 = l1.next # 更新节点
            l2 = l2.next
        if (l1 == None and l2): # 若l1算完，续将l2剩下部分加至结果，但还要考虑进位，如1999+1，所以重复上面计算过程
            while(l2):
                new_node = ListNode(0)
                pointer.next = new_node
                pointer = pointer.next
                value = l2.val + temp
                pointer.val = value % 10
                temp = value // 10
                l2 = l2.next
        if (l2 == None and l1):
            while(l1):
                new_node = ListNode(0)
                pointer.next = new_node
                pointer = pointer.next
                value = l1.val + temp
                pointer.val = value % 10
                temp = value // 10
                l1 = l1.next
        if(l1 == None and l2 == None): # 都算完后考虑首位是否有进位
            if(temp):
                new_node = ListNode(1)
                pointer.next = new_node
                return head.next #头结点为空，结果从头结点下一个开始
            else:
                return head.next
        return head.next