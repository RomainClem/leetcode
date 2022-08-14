# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from socket import has_dualstack_ipv6
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        while head.next:
            if head.val == "loop": return False
            temp = head.next
            head.val = "loop"
            head = temp
        
        return True