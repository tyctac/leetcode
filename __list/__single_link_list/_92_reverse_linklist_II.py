# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        i = 0
        while i != m-1 : # no problem
            p = p.next
            if p == None:
                return dummy.next
            i += 1
        j = i
        tmphead = p
        q = tmphead.next
        if q == None:
            return dummy.next
        while j < n:
            if q.next == None:
                if tmphead.next == q:
                    break
                else:
                    p.next = q.next
                    q.next = tmphead.next
                    tmphead.next = q
                    break
            else:
                if tmphead.next != q:
                    p.next = q.next
                    q.next = tmphead.next
                    tmphead.next = q
                    q = p.next
                    j += 1
                else:
                    j += 1
                    p = p.next
                    q = p.next

        return dummy.next

