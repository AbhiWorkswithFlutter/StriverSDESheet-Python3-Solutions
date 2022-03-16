#Question Link: https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1#
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=f712fd35cf08c53fd4b578a827e487ed&pid=700186&user=tiabhi1999

#For the complete code snippet and question, please refer the above links,

class Solution:
    
    def copyList(self, head):
        dummy = Node(-1)
        dummy.next = head
        curr = head
        
        while curr:
            temp = Node(curr.data)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        curr = head 
        while curr is not None:
            if curr.arb is not None:
                curr.next.arb = curr.arb.next
            curr = curr.next.next
        
        curr = dummy
        oldnode = head
        while oldnode:
            curr.next = oldnode.next
            curr = oldnode
            oldnode = curr.next
            
        return dummy.next
