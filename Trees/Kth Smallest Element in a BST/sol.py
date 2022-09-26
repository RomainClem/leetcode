# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        dif = 0
        if not root.right and not root.left: return root.val
        while len(q) - dif <= k:
            if q[-1].left: q.append(q[-1].left)
            elif q[-1].right: q.append(q[-1].right)
            else: 
                n = q.pop()
                if q[-1].left == n: q[-1].left = None
                else: q[-1].right = None
                dif+=1
                
        return q[-(k-dif)].val
        