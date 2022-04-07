#Question Link: https://takeuforward.org/data-structure/implement-min-stack-o2n-and-on-space-complexity/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=2dbd3a9fbc5366e23fb41752cf1dd64e&pid=700278&user=tiabhi1999

#For complete code snippet and question, please refer GFG link (https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1/)



class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if len(self.s) == 0:
            self.s.append(x)
            self.minEle = x
            return
        elif x < self.minEle:
            self.s.append((2*x)-self.minEle)
            self.minEle = x
            return
        else:
            self.s.append(x)
            return
            
        
        #CODE HERE

    def pop(self):
        #CODE HERE
        if len(self.s)<1:
            return -1
        x = self.s[-1]
        self.s.pop()
        if x < self.minEle:
            temp = self.minEle
            self.minEle = (2*self.minEle)-x
            return temp
        return x
        
    def getMin(self):
        if len(self.s)<1:
            return -1
        else:
            return self.minEle
