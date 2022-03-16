#Question Link: https://takeuforward.org/data-structure/find-middle-element-in-a-linked-list/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=d2f963b255abd1d61f196bb162168f7c&pid=700171&user=tiabhi1999

class Solution:
    
    def findMid(self, head):
        if head is None:
            return head
        if head.next is None:
            return head.data
        slow = fast = head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
        return slow.data
        
        




# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        print(ob.findMid(list1.head))
