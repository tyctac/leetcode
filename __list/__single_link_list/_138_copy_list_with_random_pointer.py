# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        pointer_back = []
        p = head
        dummy  = RandomListNode(-1)
        q = dummy
        while p != None:
            tmp = RandomListNode(p.label)
            pointer_back.append(p)
            tmp_point = p.next
            p.next = tmp
            q.next = tmp
            p = tmp_point
            q = q.next
        for p in pointer_back:
            if p.random == None:
                p.next.random = None
            else:
                tmp = RandomListNode(p.random.lable)
                p.next.random = tmp
        l = len(pointer_back)
        for i in range(l):
            if i == l-1:
                pointer_back[i].next = None
                break
            pointer_back[i].next = pointer_back[i+1]
        return dummy.next

so = Solution()
a = RandomListNode(-1)
a.next = None
a.random = None
print so.copyRandomList(a)