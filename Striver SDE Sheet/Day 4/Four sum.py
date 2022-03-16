#Question Link: https://takeuforward.org/data-structure/4-sum-find-quads-that-add-up-to-a-target-value/
#Solution Link (Python3): https://leetcode.com/submissions/detail/661138741/

#For the complete question and code snippet, please refer leetcode link(https://leetcode.com/problems/4sum/)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums)-1

                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r: 
                            l += 1
        return res
        
