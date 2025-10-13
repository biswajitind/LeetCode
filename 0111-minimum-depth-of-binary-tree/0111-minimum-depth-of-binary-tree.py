# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min_depth = float("inf")
        
        def helper(tnode, depth):
            if not tnode:
                return(self.min_depth)

            if tnode.left == None and tnode.right == None:
                self.min_depth = min(self.min_depth, depth + 1)
            else:
                helper(tnode.left, depth + 1)
                helper(tnode.right, depth + 1)
        
        helper(root, 0)
        return(self.min_depth)