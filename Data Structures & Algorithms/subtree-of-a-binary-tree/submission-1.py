# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t or t.val != s.val:
            return False
        return self.sameTree(s.right, t.right) and self.sameTree(s.left, t.left)