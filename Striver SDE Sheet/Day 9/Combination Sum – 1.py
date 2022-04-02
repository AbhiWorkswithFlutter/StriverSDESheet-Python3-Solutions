#Question Link: https://takeuforward.org/data-structure/combination-sum-1/
#Solution (Python3): https://leetcode.com/submissions/detail/669864003/

#For complete code snippet and question, please refer the leetcode link (https://leetcode.com/problems/combination-sum/)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
      
        
        def helper(index, target, ds, ans, candidates):
            if index == len(candidates):
                if target == 0:
                    ans.append(ds.copy())
                return
         
            if candidates[index] <= target:
                ds.append(candidates[index])
                helper(index, target-candidates[index], ds, ans, candidates)
                ds.pop()
                
            helper(index+1, target, ds, ans, candidates)
         
        
        helper(0, target, [], ans, candidates)
        
        return ans
