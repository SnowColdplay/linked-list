"输入两个链表，找出它们的第一个公共结点。"
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"两条相交的链表呈Y型。可以从两条链表尾部同时出发，最后一个相同的结点就是链表的第一个相同的结点。利用stack,后进先出。"

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        stack1=[]
        stack2=[]
        has=0
        while pHead1:
            stack1.append(pHead1)
            pHead1=pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2=pHead2.next

        while pHead1 and pHead2:
            top1=pHead1.pop()
            top2=pHead2.pop()

            if top1==top2:
                has=has+1
                first=top1
            else:
                break

        if has==0:
            return None
        return first


