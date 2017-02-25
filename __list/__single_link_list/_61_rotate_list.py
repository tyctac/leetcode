# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        p = head
        i = 1
        while p != None:
            i += 1
            p = p.next
        k = k % i
        p = head
        i = 1
        while i <= k:
            p = p.next
            if p == None:
                return head
            i += 1
        q = head
        while p.next != None:
            p = p.next
            q = q.next
        p.next = head
        head = q.next
        q.next = None
        return head

a = ListNode(1)
b = ListNode(2)
a.next = b
so = Solution()
x = so.rotateRight(a,3)
print x