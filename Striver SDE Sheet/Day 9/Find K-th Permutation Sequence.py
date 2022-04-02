#Question Link: https://takeuforward.org/data-structure/find-k-th-permutation-sequence/
#Solution Link (Python3): https://leetcode.com/submissions/detail/666284916/

#For complete code snippet and question, please refer leetcode link (https://leetcode.com/problems/permutation-sequence/)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []
        for i in range(1,n):
            fact = fact * i
            numbers.append(i)
      
        numbers.append(n)
        ans = ""
        k = k - 1
        
        while(True):
            ans += str(numbers[int(k // fact)])
            numbers.pop(int(k // fact))
            if len(numbers) == 0:
                break
     
            k = k % fact;
            fact = fact / len(numbers)
      
        return ans

        
