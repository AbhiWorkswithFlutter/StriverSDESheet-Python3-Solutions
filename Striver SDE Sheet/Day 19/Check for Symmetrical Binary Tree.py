#Question Link: https://takeuforward.org/data-structure/check-for-symmetrical-binary-tree/
#Solution (Python3): https://leetcode.com/submissions/detail/718130088/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def helper(root1, root2):
            if(root1 == None or root2 == None):
                return root1 == root2
            return (root1.val == root2.val) and helper(root1.left, root2.right) and helper(root1.right, root2.left)
        
        return helper(root.left, root.right)
