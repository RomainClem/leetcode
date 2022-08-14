# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l, temp = [], head
        while temp:
            l.append(temp)
            temp = temp.next

        mid = len(l) // 2
        for i in range(mid):  
            l[i].next = l[-(i+1)]
            l[-(i+1)].next = l[i+1]
            
        l[mid].next = None
        