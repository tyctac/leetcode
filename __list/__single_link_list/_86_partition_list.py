# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        r1 = dum1 = ListNode(-1)
        r2 = dum2 = ListNode(-1)
        p = head
        while p != None:
            if p.val < x:
                r1.next = p
                r1 = r1.next
            else:
                r2.next = p
                r2 = r2.next
            p = p.next

        r1.next = dum2.next
        return dum1.next

a = ListNode(2)
b = ListNode(1)
a.next = b
so = Solution()
x = so.partition(a,2)
print x