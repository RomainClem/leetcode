from collections import deque

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(preorder[0])
        new_head = head
        stack = deque()
        left = True
        if len(inorder) <= 1 : return head 
        
        i, j = 0, 0
        while i < len(inorder):
            if left:
                head.left = TreeNode(preorder[i])
                new_head = head.left
                stack.appendleft(head.left)
                
            else:
                stack.popleft()
                new_head = stack[0]
                new_head.right = TreeNode(preorder[i])
                left = True
            
            if inorder[i] == preorder[0]:
                ...
            if inorder[j] == new_head.val: 
                left = False
                j+=1
                
            i+=1 