#Question Link : https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/

#Solution link(Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=005f7afe6786389a6c463128e326fa20&pid=701215&user=tiabhi1999



class Solution:

    def maxSubArraySum(self,a,size):
        currmax = 0
        mfs = sum(a)
        
        for i in range(len(a)):
            currmax = currmax + a[i]
            if(currmax<a[i]):
                currmax = a[i]
            if(mfs< currmax):
                mfs = currmax
        
        return mfs
            
        



 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
