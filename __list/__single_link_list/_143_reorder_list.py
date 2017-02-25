# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        i = 0
        fast = head
        slow = head
        if not head:
            return None
        fast = fast.next
        if fast == None:
            return head
        fast = fast.next
        slow = head.next
        while fast != None:
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            slow = slow.next
        dummy = ListNode(-1)
        dummy.next = slow
        p = slow.next
        while p != None:
            slow.next = p.next
            p.next = dummy.next
            dummy.next = p
            p = slow.next

        p = head
        q = dummy.next
        while p != slow:
            tmp1 = p.next
            tmp2 = q.next
            p.next = q
            q.next = tmp1
            p = tmp1
            q = tmp2
        slow.next = None
