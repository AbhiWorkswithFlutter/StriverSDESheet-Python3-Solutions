#Question Link: https://takeuforward.org/data-structure/bottom-view-of-a-binary-tree/
#Solution Link (Python3):



class Solution:
    def bottomView(self, root):
        
        d = {}
        ans = []
        
        def printBottomViewUtil(root,hd,level):
            nonlocal d
            if root is None:
                return
             
            if hd in d:
                if level >= d[hd][1]:
                    d[hd] = [root.data, level]
            else:
                d[hd] = [root.data, level]
                 
           
            printBottomViewUtil(root.left, hd - 1, level + 1)
            
            printBottomViewUtil(root.right, hd + 1, level + 1)
        printBottomViewUtil(root, 0, 0)
        for i in sorted(d.keys()):
            ans.append(d[i][0])
        return ans
