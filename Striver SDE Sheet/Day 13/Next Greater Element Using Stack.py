#Question Link: https://takeuforward.org/data-structure/next-greater-element-using-stack/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=9bea24675257dbf28566835a4b35e936&pid=701343&user=tiabhi1999

#For complete code snippet and question, please refer the GFG link (https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/)


class Solution:
    def nextLargerElement(self,arr,n):
        if n<1:
            return -1
        ans = [-1]*n
        s =[]
        for i in range(n-1, -1,-1):
            while(len(s)>0 and arr[s[-1]]<=arr[i]):
                s.pop()
            if len(s)>0:
                ans[i] = arr[s[-1]]
            s.append(i)
                
                
        return ans    
