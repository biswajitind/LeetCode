# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        rSet = set()

        # Add the values to a set ( from root1)
        def _populate_set(node, data):
            if node:
                data.add(node.val)
                _populate_set(node.left, data)
                _populate_set(node.right, data)

        def _dfs(node):
            
            if node:
                #print(rSet, node.val)
                if (target - node.val) in rSet:
                    return(True)
                if (_dfs(node.left)):
                    return(True)
                if (_dfs(node.right)):
                    return(True)
            return(False)

        
        _populate_set(root1, rSet)
        print(rSet)
        if _dfs(root2):
            return(True)

        return(False)