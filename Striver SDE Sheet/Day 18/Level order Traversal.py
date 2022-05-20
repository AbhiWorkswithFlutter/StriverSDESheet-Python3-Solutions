#Question Link: https://takeuforward.org/data-structure/level-order-traversal-of-a-binary-tree/
#Solution Link (Python3): https://leetcode.com/submissions/detail/605959789/




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        nextlevel = []
        level = []
        result = []
        
        while(queue != []):
            
            for root in queue:
                level.append(root.val)
                if root.left:
                    nextlevel.append(root.left)
                if root.right:
                    nextlevel.append(root.right)
            result.append(level)
            level = []
            queue = nextlevel
            nextlevel = []
        return result
        
        
