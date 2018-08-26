"题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"新建一个链表，用dummy来遍历链表里的节点"
class Solution:
    def Merge(self, pHead1, pHead2):
        dummy=ListNode(0)
        pHead=dummy
        while pHead1 and pHead2:
            if pHead1.val>pHead2.val:
                dummy.next=pHead2
                pHead2=pHead2.next
            else:
                dummy.next=pHead1
                pHead1=pHead1.next
            dummy=dummy.next
        if pHead1:
            dummy.next=pHead1
        if pHead2:
            dummy.next=pHead2
        return pHead.next




