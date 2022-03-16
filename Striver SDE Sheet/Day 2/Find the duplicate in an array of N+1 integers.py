#Question Link: https://takeuforward.org/data-structure/find-the-duplicate-in-an-array-of-n1-integers/
#Solution Link (Python3): https://leetcode.com/submissions/detail/609846570/

#for complete code snippet please refer the leetcode question link (https://leetcode.com/problems/find-the-duplicate-number/)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 
            
        slow = nums[0]
        fast = nums[0]
        
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]
            
            
        return slow
