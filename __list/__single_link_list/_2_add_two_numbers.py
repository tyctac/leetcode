# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def reverse(self,l):
        if l == None:
            return l
        ret = ListNode(-1)
        a = l
        current_head = l
        while a.next != None:
            b = a.next
            a.next = b.next
            b.next = current_head
            current_head = b
            c = a.next
            if a.next == None:
                break
            if c.next == None:
                a.next = None
                c.next = current_head
                current_head = c
        return current_head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1 = self.reverse(l1)
        # l2 = self.reverse(l2)
        p = l1
        q = l2
        carry = 0
        head = ListNode(-1)
        rear = head
        x = 0
        y = 0
        while p != None or q != None:
            if p != None:
                x = p.val
            if q != None:
                y = q.val
            s = x + y + carry
            tmp = ListNode(s % 10)
            x = 0
            y = 0
            carry = s / 10
            rear.next = tmp
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        if carry == 1:
            tmp = ListNode(1)
            tmp.next = head.next
            return tmp
        return head.next

so = Solution()
a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
e = ListNode(5)
f = ListNode(6)
g = ListNode(4)
a.next = b
b.next = c
e.next = f
f.next = g
x = so.addTwoNumbers(a,e)
print x