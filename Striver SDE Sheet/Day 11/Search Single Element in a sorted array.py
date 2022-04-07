#Question Link: https://takeuforward.org/data-structure/search-single-element-in-a-sorted-array/
#Solution (Python3): https://leetcode.com/submissions/detail/667573399/

#For complete code snippet and question, please refer the Leetcode link (https://leetcode.com/problems/single-element-in-a-sorted-array/)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 2
        
        if nums[low] != nums[low+1]:
            return nums[0]
        
        if nums[high] != nums[-1]:
            return nums[-1]
        
        while(low <= high):
            mid = (low + high) // 2
                
            if(mid % 2 == 0):
                if(nums[mid] != nums[mid + 1]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (nums[mid] == nums[mid + 1]):
                    high = mid - 1
                else:
                    low = mid + 1
         
        return nums[low]
        
