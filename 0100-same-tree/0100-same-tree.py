# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Lets do DFS in both trees at the same time while comparing the nodes at every step.

        def _dfs(tp, tq):

            if tp == None and tq == None:
                return(True)

            if tp and tq and tp.val == tq.val:
                return( _dfs(tp.left, tq.left) and _dfs(tp.right, tq.right))
            else:
                return(False)
        
        return(_dfs(p, q))
        
            

            


        
