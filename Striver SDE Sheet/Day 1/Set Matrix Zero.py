#Question Link: https://takeuforward.org/data-structure/set-matrix-zero/
#Solution Link (Python3): https://leetcode.com/submissions/detail/659026546/


#For the complete code snippet, please refer the leetcode question (https://leetcode.com/problems/set-matrix-zeroes/)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][c] = float("inf")
                
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == float("inf"):
                    for i in range(cols):
                        if matrix[r][i] == float("inf"): 
                            continue
                        matrix[r][i] = 0
                    for i in range(rows):
                        if matrix[i][c] == float("inf"): 
                            continue
                        matrix[i][c] = 0
                        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == float("inf"):
                    matrix[r][c] = 0
