#Question Link: https://takeuforward.org/data-structure/search-element-in-a-rotated-sorted-array/
#Solution Link (Python3): https://leetcode.com/submissions/detail/667191462/

#For complete code snippet and question, please refer the leetcode link (https://leetcode.com/problems/search-in-rotated-sorted-array/)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while(low<=high):
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[low] <= nums[mid]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
                    
        
