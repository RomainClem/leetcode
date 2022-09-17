def traverse_list(l):
    out = str(l.val)
    node = l
    while True:
        if node.next == None:
            return out
        else:
            node = node.next
            out = str(node.val) + out

def reverse_list(l):
    head = ListNode()
    head.val = int(l[-1])
    next_node = head
    while True:
        if len(l) == 1:
            return head
        else:
            del l[-1]
            next_node.next = ListNode()
            next_node = next_node.next
            next_node.val = int(l[-1])

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_int = traverse_list(l1)
        l2_int = traverse_list(l2)
        
        addition = int(l1_int) + int(l2_int)
        return reverse_list(list(str(addition)))