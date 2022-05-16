#Question Link: https://takeuforward.org/data-structure/top-view-of-a-binary-tree/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=91994dacadc81261d0d62420f5e3a703&pid=700490&user=tiabhi1999



# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    def topView(self,root):
        if not root:
            return []
            
        dic = {}
        ans = []
        m = float("inf")
        
        temp = deque([(root,0)])
        
        while temp:
            n = temp.popleft()
            if n[1] not in dic:
                dic[n[1]] = n[0].data
                m = min(m,n[1])
            if n[0].left:
                temp.append((n[0].left,n[1]-1))
            if n[0].right:
                temp.append((n[0].right,n[1]+1))
        while m in dic:
            ans.append(dic[m])
            m+=1
        return ans
