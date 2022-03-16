#Question Link: https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/
# Refer the leetcode question for the complete code snippet (https://leetcode.com/problems/two-sum/)
#Solution Link (Python3): https://leetcode.com/submissions/detail/656733511/

class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(arr)):
            if target - arr[i] in d:
                return [d[target - arr[i]], i]
            else:
                d[arr[i]] = i
        return -1


