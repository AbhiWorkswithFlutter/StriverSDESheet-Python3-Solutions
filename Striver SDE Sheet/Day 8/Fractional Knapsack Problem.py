#Question Link: https://takeuforward.org/data-structure/fractional-knapsack-problem-greedy-approach/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=05e09acc984333ecb672d8168ef5d475&pid=701365&user=tiabhi1999 

#For complete code snippet and question, please refer GFG link (https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#)

'''
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
'''

class Solution:    
    def fractionalknapsack(self, W,Items,n):
        arr =[] 
       
        for i in range(n):
            #calculating ratio
            temp = Items[i].value / Items[i].weight
            arr.append((temp, Items[i].value, Items[i].weight ))
      
        arr.sort(reverse=True)
        res = 0
       
        for i in range(n):
            val, wt = arr[i][1], arr[i][2]
            if W > wt:
                W -= wt
                res += val
            else:
                fract = W/wt
                res = res + fract * val
                W = 0
                break
        return res
            
      
        
