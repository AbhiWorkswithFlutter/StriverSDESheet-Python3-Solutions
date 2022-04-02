#Question Link: https://takeuforward.org/data-structure/subset-sum-sum-of-all-subsets/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=924fa39c0e8af723ad3b6befbe109454&pid=704723&user=tiabhi1999

#For complete code snippet and question, please refer the GFG link (https://practice.geeksforgeeks.org/problems/subset-sums2234/1#)


class Solution:
    def subsetSums(self, arr, N):
        res = []
        
        def helper(index, s, arr, N):
            if index == N:
                res.append(s)
                return
            
            helper(index+1, s+arr[index], arr, N)
            
            helper(index+1, s, arr, N)
            
            return
        
        helper(0, 0, arr, N)
        
        return res
