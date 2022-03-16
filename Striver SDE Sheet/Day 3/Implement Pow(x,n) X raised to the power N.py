#Question Link: https://takeuforward.org/data-structure/implement-powxn-x-raised-to-the-power-n/
#Solution Link (Python2): https://leetcode.com/submissions/detail/659845591/

#For the complete question and code snippet, please refer leetcode link (https://leetcode.com/problems/powx-n/)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if(n == 0): 
            return 1
        
        temp = self.myPow(x, int(n / 2))

        if (n % 2 == 0):
            return temp ** 2
        else:
            if(n > 0): 
                return x * temp * temp
            else: 
                return (temp ** 2 ) / x
        
