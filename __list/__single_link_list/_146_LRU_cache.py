class ListNode(object):
    def __init__(self, k,v):
        self.val = v
        self.key = k
        self.next = None
        self.forward = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.list_node_dic = {}
        self.dummy = ListNode(-1)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.list_node_dic:
            return -1
        p = self.list_node_dic[key]
        if self.dummy.next == p:
            return p.value
        fwd = p.forward
        nxt = p.next
        fwd.next = next
        nxt.forward = fwd
        p.forward = self.dummy
        p.next = self.dummy.next
        self.dummy.next = p
        return p.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        current_size = len(self.list_node_dic)
        if current_size == 0:
            first_node = ListNode(key,value)
            self.dummy.next = first_node
            self.dummy.forward = first_node
            first_node.forward = self.dummy
            first_node.next = self.dummy
            self.list_node_dic[key] = first_node

        if current_size < self.capacity:
            if key not in self.list_node_dic:
                tmp = self.next
                first_node = ListNode(key,value)
                self.dummy.next = first_node
                first_node.forward = self.dummy
                first_node.next = tmp
                tmp.forward = first_node
                self.list_node_dic[key] = first_node
            else:
                p = self.list_node_dic[key]
                p.val = value
                fwd = p.forward
                nxt = p.next
                fwd.next = nxt
                nxt.forward = fwd
                p.next = self.dummy.next
                p.forward = self.dummy
                self.dummy.next = p
        else:
            to_delete = self.dummy.forward
            to_delete.next = self.dummy
            self.dummy.forward = to_delete
            self.list_node_dic.pop(to_delete.key)
            new_p = ListNode(key,value)
            new_p.next = self.dummy.next
            self.dummy.next = new_p
            new_p.forward = self.dummy
            new_p.next.forward = new_p
            self.list_node_dic[key] = new_p






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)