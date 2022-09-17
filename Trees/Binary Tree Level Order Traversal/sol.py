# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        level = []
        q = deque([root])
        
        while q:
            level.append([])
            for _ in range(len(q)):
                node = q.popleft()
                level[-1].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return level