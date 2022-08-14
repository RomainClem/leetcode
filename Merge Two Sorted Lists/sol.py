import re
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2: return list1
        if not list1: return list2
        
        head, curr1, curr2 = list2, list2, list1
        if list1.val <= list2.val: head, curr1, curr2 = list1, list1, list2 
        
        while curr1 and curr2:
            if not (curr1.next and curr1.next.val < curr2.val):
                temp2 = curr2.next 
                curr2.next = curr1.next
                curr1.next = curr2
                curr2 = temp2
            curr1 = curr1.next
        
        return head
    
list1 = ListNode(1)
next = ListNode(2)
list1.next = next
next.next = ListNode(4)

list2 = ListNode(1)
next = ListNode(3)
list2.next = next
next.next = ListNode(4)

head = Solution().mergeTwoLists(list1, list2)

while head:
    print(head.val)
    head = head.next