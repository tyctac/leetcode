# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverse(self,dummy,k):
        p = dummy
        i = 0
        while i < k:
            p = p.next
            i += 1
            if p == None:
                return
        left_one = p.next
        q = dummy.next.next
        p = dummy.next
        while q != left_one:
            p.next = q.next
            q.next = dummy.next
            dummy.next = q
            q = p.next
        self.reverse(p,k)



    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        self.reverse(dummy,k)
        return dummy.next

a = ListNode(1)
b = ListNode(2)
a.next = b
so = Solution()
x = so.reverseKGroup(a,2)
print x