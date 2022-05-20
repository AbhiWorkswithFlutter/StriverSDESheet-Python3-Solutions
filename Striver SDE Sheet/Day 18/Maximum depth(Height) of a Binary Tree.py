#Question Link: https://takeuforward.org/data-structure/maximum-depth-of-a-binary-tree/
#Solution (Python3): https://leetcode.com/submissions/detail/702984028/




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftheight = self.maxDepth(root.left)
        rightheight = self.maxDepth(root.right)
        
        return max(leftheight,rightheight)+1
        
        
        
