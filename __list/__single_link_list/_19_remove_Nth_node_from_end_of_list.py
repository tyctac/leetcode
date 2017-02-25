# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n == 0:
            return head
        p = head
        i = 1
        while p != None:
            i += 1
            p = p.next
        if i-1 == n:
            return head.next
        n = n % i
        p = head
        i = 1
        while i <= n:
            p = p.next
            if p == None:
                return head
            i += 1
        q = head
        while p.next != None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head

a = ListNode(1)
b = ListNode(2)
a.next = b
so = Solution()
x = so.removeNthFromEnd(a,3)
print x