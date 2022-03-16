#Question Link: https://takeuforward.org/data-structure/merge-two-sorted-linked-lists/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=87db8936190b7bd3924598ae2f6079d8&pid=700176&user=tiabhi1999

def sortedMerge(head1, head2):
    if head1 is None and head2 is None:
        return
    if head1 is None and head2 is not None:
        return head2
    if head1 is not None and head2 is None:
        return head1
    
    if head2.data < head1.data:
        temp = head1
        head1 = head2
        head2 = temp
    ans = head1
    while(head1 is not None and head2 is not None):
        temp = None
        while(head1 is not None and head1.data <= head2.data):
            temp = head1
            head1 = head1.next
        temp.next = head2
        t = head1
        head1 = head2
        head2 = t
    
    
        
    
    
    return ans    
 


# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))
