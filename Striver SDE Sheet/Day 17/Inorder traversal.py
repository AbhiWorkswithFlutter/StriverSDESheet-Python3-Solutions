#Question Link: https://takeuforward.org/data-structure/inorder-traversal-of-binary-tree/
#Solution Link (Python3): https://leetcode.com/submissions/detail/606034029/

#Recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderutil(self, root, a):
        if root is None:
            return
        self.inorderutil(root.left,a)
        a.append(root.val)
        self.inorderutil(root.right,a)
        return a
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.inorderutil(root, [])
