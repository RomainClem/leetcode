# Definition for singly-linked list.
from asyncio.windows_events import NULL
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    new_head = None
    next_head = None
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        self.get_head(head)
        self.next_head.next = None
        return self.new_head
    
    def get_head(self, head):
        if head.next: self.get_head(head.next)
        if self.new_head == None: 
            self.new_head = head
            self.next_head = head
        else: 
            self.next_head.next = head
            self.next_head = head