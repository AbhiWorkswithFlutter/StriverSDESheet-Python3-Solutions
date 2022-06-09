#Question Link: https://takeuforward.org/data-structure/maximum-sum-path-in-binary-tree/
#Solution (Python3): https://leetcode.com/submissions/detail/718125097/



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxi = float("-inf")
        def helper(root):
            nonlocal maxi
            if root is None:
                return 0
        
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            maxi = max(maxi, left+right+root.val)
            return max(left,right) + root.val
        
        helper(root)
        
        return maxi
