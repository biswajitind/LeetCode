# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, cur_sum):
            if not node:
                return(False)
            
            # Leaf node.
            if node.left == None and node.right == None:
                if cur_sum + node.val == targetSum:
                    return(True)
                else:
                    return(False)
            else:
                l = dfs(node.left, cur_sum + node.val)
                r = dfs(node.right, cur_sum + node.val)
                return(l or r)
            
        return(dfs(root, 0))