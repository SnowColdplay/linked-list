class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        dummy=ListNode(-1)
        dummy.next=pHead

        " 用两个指针，pre和cur来遍历，如果遇到重复节点，pre跳过重复节点"
        pre=dummy
        cur=pHead

        while cur and cur.next:
            if cur.val!=cur.next.val:
                pre=pre.next
                cur=cur.next
            else:
                val=cur.val
                "注意判断cur是否存在 while cur"
                while cur and cur.val==val:
                    cur=cur.next
                pre.next=cur
        return dummy.next
