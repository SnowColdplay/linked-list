"题目：输入一个链表，输出该链表中倒数第k个结点。"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"思路：用两个指针，前后指针相差为k，则当后指针到达尾部时，前指针正好是倒数第k个节点"
class Solution:
    def FindKthToTail(self, head, k):
        "边界条件"
        if not head or not k:
            return None
        first,last=head,head
        for i in range(k-1):
            "边界条件"
            if not first.next:
                return None
            first=first.next
        while first.next:
            first=first.next
            last=last.next
        return last


