#Question Link: https://takeuforward.org/data-structure/palindrome-partitioning/
#Solution (Python3): https://leetcode.com/submissions/detail/669743107/

#For complete code snippet and question, please refer the leetcode link (https://leetcode.com/problems/palindrome-partitioning/)


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
    
        ans = []
        
        def isPalindrome(s, start, end):
            temp = s[start:end]
            return temp == temp[::-1]
        
        def helper(st,path):
            if st >= len(s):
                ans.append(path[:])
                return 
            for i in range(st, len(s)):
                if isPalindrome(s,st,i+1):
                    path.append(s[st:i+1])
                    helper(i+1,path)
                    path.pop()
        
        helper(0,[])
        return ans
