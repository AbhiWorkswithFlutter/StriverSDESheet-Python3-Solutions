#Question Link: https://takeuforward.org/data-structure/rotate-a-linked-list/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=fa470daedeb0feb477bdf03741263909&pid=700023&user=tiabhi1999


#This solution is for the left rotation(For the question mentioned on gfg) (https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1/)
#Rotate right is similar to this, you just have to play with the value of k. You can refer YT or other resources for the intution.


class Solution:
    
   
    def rotate(self, head, k):
        temp = head
        count = 1
        while(temp.next is not None):
            temp = temp.next
            
        temp.next = head
        temp = head
        
        for i in range(k-1):
            temp = temp.next
            
        head = temp.next
        temp.next = None
        return head
        
        

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
