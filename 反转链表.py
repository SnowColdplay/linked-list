"题目：输入一个链表，反转链表后，输出新链表的表头。。"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    "反转：用两个指针，一个cur，一个pre，反转的过程，就是cur指向pre的过程，在循环的过程中，用next保存当前节点的下一个节点"
    def ReverseList(self, phead):
        cur=phead
        pre=None
        while cur:
            pnext=cur.next
            cur.next=pre

            pre=cur
            cur=pnext
        return pre

