# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        
        def _dfs(node, target, res):
            if node == None:
                return()
            else:
                if node.left == None and node.right == None:
                    if node.val == target:
                        res.append(node.val)
                        self.result.append(res)
                    return
                else:
                    res.append(node.val)
                    if node.left:
                        _dfs(node.left, target - node.val, res[:])
                    if node.right:
                        _dfs(node.right, target - node.val, res[:])

        _dfs(root, targetSum, [])
        return(self.result)
