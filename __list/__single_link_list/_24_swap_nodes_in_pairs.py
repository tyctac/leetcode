# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = dummy.next
        if q == None:
            return None
        r = q.next
        if r == None:
            return dummy.next
        while q != None:
            if q == None:
                return dummy.next
            r = q.next
            if r == None:
                return dummy.next
            p.next = r
            p = q
            r.next = q
            q = p.next
        return dummy.next
