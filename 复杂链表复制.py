class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        "第一步：A-B-C变成 A-A'-B-B'-C-C'"
        dummy=pHead
        while dummy:
            dummynext=dummy.next
            copynode=RandomListNode(dummy.label)
            dummy.next=copynode
            copynode.next=dummynext

            dummy=dummynext

        "第二步:将random加上"
        dummy=pHead
        while dummy:
            copynode=dummy.next
            dummyrandom = dummy.random
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy=copynode.next

        "第三步:将A-A'-B-B'断开为A-B 和 A'-B'"
        dummy=pHead
        copyHead=dummy.next
        while dummy:
            copynode=dummy.next
            dummynext=copynode.next

            dummy.next=dummynext
            "这里一定要判断是不是到了结尾"
            if dummynext:
                copynode.next=dummynext.next
            else:
                copynode.next=None

            dummy=dummy.next
        return copyHead




