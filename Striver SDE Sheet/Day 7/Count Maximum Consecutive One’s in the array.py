#Question Link: https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/
#Solution Link (Python3): https://leetcode.com/submissions/detail/657420187/

#For complete code snippet, refer the leetcode question (https://leetcode.com/problems/max-consecutive-ones/)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            maxcount = max(maxcount, count)
        return maxcount
        
