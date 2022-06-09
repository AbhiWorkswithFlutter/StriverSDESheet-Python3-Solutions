#Question Link: https://practice.geeksforgeeks.org/problems/mirror-tree/1
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=38ddf665eac9e6dde83dc6c8de8f4b73&pid=700155&user=tiabhi1999

#Given a Binary Tree, convert it into its mirror.

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    
    def mirror(self,root):
        if root is None:
            return 
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left
