#Question Link: https://takeuforward.org/data-structure/right-left-view-of-binary-tree/
#Solution Link (Python3) (Left View): https://practice.geeksforgeeks.org/viewSol.php?subId=76165397cf2ccec998e630b4673bbcf6&pid=700174&user=tiabhi1999





'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def LeftView(root):
    ans = []
    
    if root is None:
        return []
    
    def helper(root, lvl):
        if root is None:
            return 
        if len(ans) == lvl:
            ans.append(root.data)
        helper(root.left, lvl+1)
        helper(root.right, lvl+1)
    helper(root, 0)
    
    return ans



