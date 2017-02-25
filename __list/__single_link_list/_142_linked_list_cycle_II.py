# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        flag = False
        while fast != None:
            fast = fast.next
            if fast == None:
                flag =  False
                break
            fast = fast.next
            slow = slow.next
            if fast == slow:
                flag = True
                break
        if flag == False:
            return None
        p = head
        while p != fast:
            p = p.next
            fast = fast.next
        return p