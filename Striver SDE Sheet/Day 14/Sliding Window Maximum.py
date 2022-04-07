#Question Link: https://takeuforward.org/data-structure/sliding-window-maximum/
#Solution Link (Python3): https://leetcode.com/submissions/detail/666312024/

#For complete code snippet and question, please refer the leetcode link (https://leetcode.com/problems/sliding-window-maximum/)


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a = deque([])
        res = []
        n = len(nums)
        for i in range(n):
            if len(a)>0 and a[0] == i-k:
                a.popleft()
            while(len(a)>0 and nums[a[-1]] < nums[i]):
                a.pop()

            a.append(i)
            if (i >= k - 1):
                res.append(nums[a[0]])
        return res
        
