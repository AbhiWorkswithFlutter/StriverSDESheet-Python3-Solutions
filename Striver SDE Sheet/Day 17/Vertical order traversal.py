#Question Link: https://takeuforward.org/data-structure/vertical-order-traversal-of-binary-tree/
#Solution (Python3): https://leetcode.com/submissions/detail/690418585/




# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        d = {}
        ans = []
        
        def helper(root, x_dist, y_dist):
            if root is None:
                return
            
            if x_dist in d:
                d[x_dist].append((y_dist,root.val))
            else:
                d[x_dist] = [(y_dist, root.val)]
            
            helper(root.left, x_dist-1, y_dist+1)
            helper(root.right, x_dist+1, y_dist+1)
        
        helper(root, 0, 0)
        
        for i in sorted(d.keys()):
            column = [j[1] for j in sorted(d[i])]
            ans.append(column)
            
        return ans
