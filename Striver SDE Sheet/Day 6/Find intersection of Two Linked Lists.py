#Question Link: https://takeuforward.org/data-structure/find-intersection-of-two-linked-lists/ 
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=c3dd41cbd0de6e2f1b5a9d891c95e866&pid=700163&user=tiabhi1999

#For complete code snippet refer the GFG question (https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1)
def intersetPoint(head1,head2):
    if head1 is None or head2 is None:
        return -1
    a = head1
    b = head2
    while(a != b):
        if a is None:
            a = head2
        else:
            a = a.next
        if b is None:
            b = head1
        else:
            b = b.next
    return a.data if a is not None else -1
