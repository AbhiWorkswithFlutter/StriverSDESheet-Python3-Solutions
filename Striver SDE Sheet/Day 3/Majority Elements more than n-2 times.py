#Questions Link: https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=472b91725053a58a29f6a1fa9086a58d&pid=701220&user=tiabhi1999

class Solution:
    def majorityElement(self, A, N):
        count = 0
        ele = -1
        c = 0
        
        for i in A:
            if count == 0:
                ele = i
            if i == ele:
                count+=1
            else:
                count -= 1
        for i in A:
            if i == ele:
                c+=1
        return ele if c> (N//2) else -1
 



import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
