#Question Link: https://takeuforward.org/data-structure/calculate-the-diameter-of-a-binary-tree/
#Solution (Python3): https://leetcode.com/submissions/detail/703395351/





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ma = 0
        def helper(root):
            nonlocal ma
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            ma = max(ma, left+right)
            return max(left,right)+1
        helper(root)
        return ma
        
        
