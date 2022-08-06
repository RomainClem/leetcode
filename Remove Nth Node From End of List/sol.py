class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        self.getNode(head, n)
        return head       
    
    def getNode(self, head: Optional[ListNode], n: int):  
        
        if head.next: 
            new_n = self.getNode(head.next, n)
            
            if new_n == 0:    
                next_head = head.next
                head.next = next_head.next
                return new_n -1
                
            else:
                return new_n - 1
            
        if n != 0:
            return n-1
        