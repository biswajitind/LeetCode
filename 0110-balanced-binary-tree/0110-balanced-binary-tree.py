# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # For unbalanced, height() will return -1
        def height(tnode):
            if tnode:
                hleft = height(tnode.left)
                if hleft == -1:
                    return(-1)
                hright = height(tnode.right)
                if hright == -1:
                    return(-1)
                
                if abs(hleft - hright) > 1:
                    return(-1)
                else:
                    return(1 + max(hleft, hright))
            else:
                return(0)

        if height(root) == -1:
            return(False)

        return(True)                



