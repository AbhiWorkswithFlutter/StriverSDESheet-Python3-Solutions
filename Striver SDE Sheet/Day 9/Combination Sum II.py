#Question Link: https://takeuforward.org/data-structure/combination-sum-ii-find-all-unique-combinations/
#Solution (Python3): https://leetcode.com/submissions/detail/672090971/

#For complete code snippet and question, please refer the leetcode link (https://leetcode.com/problems/combination-sum-ii/)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(list(candidates))
        
        def helper(ans, ds, target, index,candidates):
            if target == 0:
                ans.append(ds.copy())
                return
            
            for i in range(index,len(candidates)):
                if candidates[i] > target:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                
                ds.append(candidates[i])
                helper(ans, ds, target-candidates[i], i+1, candidates)
                ds.pop()
                
        helper(ans, [], target, 0,candidates)
        return ans
    
