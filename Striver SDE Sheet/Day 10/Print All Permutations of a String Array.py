#Question Link: https://takeuforward.org/data-structure/print-all-permutations-of-a-string-array/
#Solution (Python3): (Approach 2) https://leetcode.com/submissions/detail/671338908/

#Approach 1 (with extra space) (https://leetcode.com/submissions/detail/671328740/)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(ds,ans,d, nums):
            if len(ds) == len(nums):
                ans.append(ds.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in d or d[nums[i]] == False:
                    ds.append(nums[i])
                    d[nums[i]] = True
                    helper(ds,ans,d,nums)
                    ds.pop()
                    d[nums[i]] = False
   
        helper([],ans,{},nums)
        return ans

#Approach 2 (Without extra space by swapping)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(index, nums):
            if index == len(nums):
                ans.append(nums.copy())
                return
            
            for i in range(index,len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                helper(index+1, nums)
                nums[index], nums[i] = nums[i], nums[index]
   
        helper(0,nums)
        return ans
