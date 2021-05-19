# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = []
        depth = 0
        
        if (root!=None):
            root.val = 1
            q.append(root)

        
        while q:            
            v = q.pop(0)
            
            if v.val > depth:
                depth=v.val
                
            if v.left!=None:
                v.left.val=v.val+1
                q.append(v.left)
                
            if v.right!=None:
                v.right.val=v.val+1
                q.append(v.right)
                
        return depth

        