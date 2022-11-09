# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
# BAD WAY TOO SLOW
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                left_depth, right_depth = 0, 0
                if node.left: 
                    left_depth = maxDepth(node.left)
                    q.append(node.left)
                if node.right: 
                    right_depth = maxDepth(node.right)
                    q.append(node.right)
                res = max(left_depth+right_depth, res)
                
        return res
            
        