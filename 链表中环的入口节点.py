"题目：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):

        fast=pHead
        slow=pHead

        "找到相遇点"
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break

        "把fast放到起点，slow在相遇点，两者以同等速度前进，相遇点就是环的入口"
        fast=pHead

        "注意边界情况"
        if not fast or not fast.next:
            return None
        
        while fast:
            if fast==slow:
                return fast
            fast=fast.next
            slow=slow.next

