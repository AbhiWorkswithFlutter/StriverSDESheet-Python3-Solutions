#Question Link: https://takeuforward.org/data-structure/boundary-traversal-of-a-binary-tree/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=64da2de9db327f1e829a657017ba1195&pid=700204&user=tiabhi1999






'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        if root is None:
            return []
            
        ans = [root.data]
        
        def left(root):
            if root is None:
                return
            if root is not None:
                if root.left:
                    ans.append(root.data)
                    left(root.left)
                elif root.right:
                    ans.append(root.data)
                    left(root.right)
            
            
        def right(root):
            if root is None:
                return
            if root is not None:
                if root.right:
                    right(root.right)
                    ans.append(root.data)
                    
                elif root.left:
                    right(root.left)
                    ans.append(root.data)
            
            
        def leaf(root):
            if root is None:
                return
            leaf(root.left)
            if root.left is None and root.right is None:
                ans.append(root.data)
            leaf(root.right)
            
            
        if root.left is None and root.right is None:
            return ans
        
        left(root.left)
        leaf(root)
        right(root.right)
        
        
        return ans
