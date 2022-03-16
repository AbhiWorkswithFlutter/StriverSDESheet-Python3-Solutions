#Question Link: https://takeuforward.org/data-structure/length-of-longest-substring-without-any-repeating-character/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=1ea77aad41d1bff3bbba9cc8544b5b03&pid=703205&user=tiabhi1999


class Solution:

    def longestSubstrDistinctChars(self, s):
        if len(s)<1:
            return 0
        start = 0
        end = 0
        maxlen = 0
        d = {}
        while(end<len(s)):
            if s[end] in d and d[s[end]]>=start:
                start = d[s[end]]+1
            maxlen = max(maxlen, end - start +1)
            d[s[end]] = end
            end += 1
        return maxlen
       



if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)
