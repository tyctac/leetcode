# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dup = {}
        dummy.next = head
        p = head
        while p != None:
            if p.val in dup:
                dup[p.val] = 2
            else :
                dup[p.val] = 1
            p = p.next
        p = head
        q = dummy
        while p != None:
            if dup[p.val] == 2:
                q.next = p.next
                p = q.next
            else:
                p = p.next
                q = q.next
        return dummy.next