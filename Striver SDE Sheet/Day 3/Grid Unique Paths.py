#Question Link: https://takeuforward.org/data-structure/grid-unique-paths-count-paths-from-left-top-to-the-right-bottom-of-a-matrix/
#Solution Link (Python3): https://leetcode.com/submissions/detail/660019373

#For the complete code snippet and question please refer leetcode link (https://leetcode.com/problems/unique-paths/)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num = n + m - 2
        r = m - 1
        ans = 1
	    
        for i in range(1,r+1):
	        ans = (ans * (num - r + i)) // i
            
        return ans
        
