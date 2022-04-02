#Question Link: https://takeuforward.org/data-structure/subset-ii-print-all-the-unique-subsets/
#Solution (Python3): https://leetcode.com/submissions/detail/672098161/

#For complete code snippet and question, please refer the leetcode link (https://leetcode.com/problems/subsets-ii/)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(list(nums))
        def helper(index, nums, ds, ans):
            ans.append(ds.copy())
            
            for i in range(index,len(nums)):
                if i != index and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                helper(i+1, nums, ds, ans)
                ds.pop()
                
        helper(0, nums, [], ans)
        return ans
                
        
