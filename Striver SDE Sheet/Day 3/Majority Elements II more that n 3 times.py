#Question Link: https://takeuforward.org/data-structure/majority-elementsn-3-times-find-the-elements-that-appears-more-than-n-3-times-in-the-array/
#Solution Link (Python3): https://leetcode.com/submissions/detail/659343847/

#For complete code snippet and question, please refer leetcode question link (https://leetcode.com/problems/majority-element-ii/)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, c1 = -1, 0
        num2, c2 = -1, 0
        n = len(nums)
        
        for i in nums:
            if i == num1:
                c1 += 1
            elif i == num2:
                c2 += 1
            elif c1 == 0:
                num1 = i
                c1 += 1
            elif c2 == 0:
                num2 = i
                c2 += 1
            else:
                c1-=1
                c2-=1
        res = []
        c1 = c2 = 0
        for i in nums:
            if i == num1:
                c1+=1
            elif i == num2:
                c2+=1
                
        if c1 > n//3:
            res.append(num1)
        if c2 > n//3:
            res.append(num2)
        
        return res
            
                
