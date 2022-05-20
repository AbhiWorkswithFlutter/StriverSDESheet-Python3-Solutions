#Question Link: https://takeuforward.org/data-structure/check-if-the-binary-tree-is-balanced-binary-tree/
#Solution (Python3): https://leetcode.com/submissions/detail/702985232/





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return 0
            leftheight = helper(root.left)
            if leftheight == -1:
                return -1
            rightheight = helper(root.right)
            if rightheight == -1:
                return -1
            if abs(leftheight-rightheight) >1:
                return -1
            
            return max(leftheight,rightheight)+1
        ans = helper(root)
        
        return ans != -1
