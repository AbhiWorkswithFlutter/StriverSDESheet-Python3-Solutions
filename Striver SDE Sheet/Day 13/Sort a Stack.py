#Question Link: https://practice.geeksforgeeks.org/problems/sort-a-stack/1#
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=2c760d9210e4db196f63ecbee818af8f&pid=700469&user=tiabhi1999

class Solution:
    
    def sorted(self, s):
        if len(s)==0:
            return 
        x = s.pop()
        
        self.sorted(s) 
        self.helper(s, x)
        
        
    def helper(self, s, x):
        
        if len(s)==0 or s[-1]<x:
            s.append(x)
            return
            
        n = s.pop()
        
        self.helper(s, x)
        s.append(n)
