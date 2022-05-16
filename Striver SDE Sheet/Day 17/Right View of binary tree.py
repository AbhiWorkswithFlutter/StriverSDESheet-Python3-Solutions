#Question Link: https://takeuforward.org/data-structure/right-left-view-of-binary-tree/
#Solution Link (Python3) (Right View): https://practice.geeksforgeeks.org/viewSol.php?subId=d8301a1b5e333198d35589a5b58df3b3&pid=700153&user=tiabhi1999





'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    
    def rightView(self,root):
        ans = []
        
        if root is None:
            return []
        
        def helper(root, lvl):
            if root is None:
                return 
            if len(ans) == lvl:
                ans.append(root.data)
            helper(root.right, lvl+1)
            helper(root.left, lvl+1)
            
        helper(root, 0)
        
        return ans
