#Question Link: https://takeuforward.org/data-structure/count-inversions-in-an-array/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=706a2a42fcf40af334fb95df6886976e&pid=701226&user=tiabhi1999

#For complete code snippet and question please refer the GFg question link (https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1/#)

class Solution:   
    def mergeSort(self,arr, temp, left, right):
       
       res = 0
       
       if left < right:
           
           mid = (left + right)//2
           
           res += self.mergeSort(arr, temp,left, mid)
           
           res += self.mergeSort(arr, temp, mid + 1, right)
           
           res += self.merge(arr, temp, left, mid, right)
           
       return res
   
   
    def merge(self,arr, res_arr, left, mid, right):
        
        i = left     
        j = mid + 1 
        k = left     
        inversions = 0
      
        while i <= mid and j <= right:
           
            if arr[i] <= arr[j]:
                res_arr[k] = arr[i]
                k += 1
                i += 1
            else:
              
                res_arr[k] = arr[j]
                inversions += (mid-i + 1)
                k += 1
                j += 1
       
        while i <= mid:
            res_arr[k] = arr[i]
            k += 1
            i += 1
      
        while j <= right:
            res_arr[k] = arr[j]
            k += 1
            j += 1
           
        for i in range(left, right + 1):
            arr[i] = res_arr[i]
           
        return inversions
       
       
    def inversionCount(self, arr, n):
        
        return self.mergeSort(arr, [0]*n,0, n-1)

        

