#Question Link: https://takeuforward.org/data-structure/trapping-rainwater/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=e5b9be14df4cc54279a539eddfcea6f4&pid=701211&user=tiabhi1999


import math

class Solution:
    def trappingWater(self, arr,n):
        leftmax, rightmax, res, i , j = 0,0,0,0, n-1
        
        while(i<j):
            if arr[i]<=arr[j]:
                leftmax = max(leftmax, arr[i])
                res += leftmax - arr[i]
                i+=1
            elif arr[i]>arr[j]:
                rightmax = max(rightmax, arr[j])
                res += rightmax - arr[j]
                j-=1
        return res

        


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
