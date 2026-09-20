# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        q = deque()
        result = []

        if root:
            q.append(root)        

        while len(q):
            levelList = []
            for i in range(len(q)):
                node = q.popleft()
                levelList.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(levelList.copy())
                

        return(result)





        