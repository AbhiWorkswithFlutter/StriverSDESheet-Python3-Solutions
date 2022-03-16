#Question Link:
#Solution Link (Python3): https://leetcode.com/submissions/detail/659327811/

#For complete question and code snippet, please visit leetcode question link (https://leetcode.com/problems/rotate-image/)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
       
            
