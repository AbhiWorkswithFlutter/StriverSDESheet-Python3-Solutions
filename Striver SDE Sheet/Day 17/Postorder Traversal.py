#Question Link: https://takeuforward.org/data-structure/post-order-traversal-of-binary-tree/ 
#Solution Link (Python) : https://leetcode.com/submissions/detail/700736289/

#Recursive Solution




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        
        def helper(node):
            if node is None:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        
        return res
