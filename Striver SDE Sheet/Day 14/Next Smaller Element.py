#Question Link: https://www.geeksforgeeks.org/next-smaller-element/
#Soultion Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=0a07060a408d396acef58249cfac84e0&pid=706073&user=tiabhi1999

#For complete code snippet and question please refer the GFG link (https://practice.geeksforgeeks.org/problems/fab3dbbdce746976ba35c7b9b24afde40eae5a04/1/#)


class Solution:
    def help_classmate(self, arr, n):
        s = []
        res = [-1]*n
        for i in range(n-1,-1,-1):
            while(len(s)>0 and arr[s[-1]]>= arr[i]):
                s.pop()
            if len(s)>0:
                res[i] = arr[s[-1]]
            s.append(i)
        return res
       
#Input
if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()


        	
    
