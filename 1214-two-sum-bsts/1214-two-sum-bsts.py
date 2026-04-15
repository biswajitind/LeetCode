# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        rSet = set()

        def _traverse(node, data):
            if node != None:
                data.add(node.val)
                _traverse(node.left, data)
                _traverse(node.right, data)
            return(False)
        
        def _dfs(node, data):
            if node != None:
                if target - node.val in data:
                    return(True)
                if _dfs(node.left, data):
                    return(True)
                if _dfs(node.right, data):
                    return(True)
            return(False)

        _traverse(root2, rSet)
        print(rSet)
        if _dfs(root1, rSet):
            return(True)
        return False