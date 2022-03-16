#Question Link: https://takeuforward.org/data-structure/search-in-a-sorted-2d-matrix/
#Solution Link (Python3): https://leetcode.com/submissions/detail/659233436/

#For complete code snippet and question, please refer leetcode link (https://leetcode.com/problems/search-a-2d-matrix/)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = (m*n) - 1
        
        while(low<=high):
            mid = (low+high)//2
            if(matrix[mid//len(matrix[0])][mid % len(matrix[0])] == target):
                return True
            if(matrix[mid//len(matrix[0])][mid % len(matrix[0])] < target):
                low = mid + 1
            else:
                high = mid - 1
        return False
            
        
