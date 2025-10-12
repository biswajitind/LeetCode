# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Recursion
        # def _inorderTraversal(root):

        #     # Base case.
        #     if not root:
        #         return(0)

        #     _inorderTraversal(root.left)
        #     result.append(root.val)
        #     _inorderTraversal(root.right)
        
        # _inorderTraversal(root)


        # Iterative
        stack = []
        cur = root

        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            if stack:
                p = stack.pop()
                result.append(p.val)
                cur = p.right
            else:
                break

        return(result)

            
