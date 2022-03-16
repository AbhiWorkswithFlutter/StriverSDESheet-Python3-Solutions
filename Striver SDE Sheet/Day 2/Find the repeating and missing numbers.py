#Question Link: https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=c0471a295c6457b084fba3b70a96a3af&pid=702678&user=tiabhi1999




class Solution:
    def findTwoElement( self,arr, n):
        s = (n* (n+1))//2
        p = (n * (n +1) *(2*n +1) )//6
        
        for i in range(n):
            s -= arr[i]
            p -= arr[i]*arr[i]
            
        missingNum = (s + p/s)//2

        repeatingNum = missingNum - s
        
        return [int(repeatingNum), int(missingNum)]
    
    



if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1

