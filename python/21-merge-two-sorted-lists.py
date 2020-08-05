# easy

'''2020-01-05'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: # 与题2不同，无需建立空头结点。
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1 == None and l2 ==None): # 若输入为两个空链表，返回一个空链表
            return None
        head = ListNode(0)
        pointer = head # pointer指向当前节点
        while(l1 and l2): # 由于l1和l2有序，一个链表都放入后另一个链表剩下的值肯定都更大
            new_node = ListNode(0) # 新节点存放下一次放的值
            if(l1.val < l2.val):
                pointer.val = l1.val
                pointer.next = new_node
                pointer = pointer.next
                l1 = l1.next
            else:
                pointer.val = l2.val
                pointer.next = new_node
                pointer = pointer.next
                l2 = l2.next
        # 下面的代码段一定会被执行，由于一次只放一个值，最终非空的链表中至少有一个值未放，这与题2不同
        # 也正因此，不需要考虑上面的循环最后一次创建的空节点的问题，因为该节点一定会被赋值。所以不需要空头结点。
        if(l1 == None):
            pointer.val = l2.val # 将l2当前的值放入循环中最后一次创建的空节点(若输入中有空链表，则此空节点为head)
            pointer.next = l2.next # 将l2剩下的节点直接拼到尾结点后面
        else:
            pointer.val = l1.val
            pointer.next = l1.next
        return head # 头结点被赋予了最初的最小值