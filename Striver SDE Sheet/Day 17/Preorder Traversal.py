#Question Link: https://takeuforward.org/data-structure/preorder-traversal-of-binary-tree/
#Solution Link (Python3): https://leetcode.com/submissions/detail/700733357/

#Recursive solution



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        def helper(node):
            if node is None:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return res
            
        
