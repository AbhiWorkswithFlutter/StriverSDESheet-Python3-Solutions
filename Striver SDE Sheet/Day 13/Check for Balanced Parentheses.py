#Question Link: https://takeuforward.org/data-structure/check-for-balanced-parentheses/
#Solution Link (Python3): https://leetcode.com/submissions/detail/667193256/

#For complete code snippet and question, please refer the leetcode link (https://leetcode.com/problems/valid-parentheses/)


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s)%2 != 0:
            return False
        arr = []
        s = list(s)
        for i in s:
            if i == "(" or i == "{" or i == "[":
                arr.append(i)
            else:
                if len(arr) == 0:
                    return False
                x = arr[len(arr)-1]
                arr.pop()
                if (x == "(" and i == ")") or (x == "{" and i == "}") or (x == "[" and i == "]"):
                    continue
                else:
                    return False
        if len(arr) == 0:
            return True
        else:
            return False
        
