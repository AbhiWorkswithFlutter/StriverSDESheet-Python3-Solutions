#Question Link: https://takeuforward.org/data-structure/count-reverse-pairs/
#Solution Link (Python3): https://leetcode.com/submissions/detail/661170366/

#For complete code snippet and question, please refer leetcode link (https://leetcode.com/problems/reverse-pairs/)

#For the below solution time complexity is O(NlogN) where n is the number of elements
#This solution is specific to Python language users

from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        lst = SortedList()
        s = 0
        for num in nums:
            i = lst.bisect_right(num * 2)
            s += len(lst) - i
            lst.add(num)
        return s
        
