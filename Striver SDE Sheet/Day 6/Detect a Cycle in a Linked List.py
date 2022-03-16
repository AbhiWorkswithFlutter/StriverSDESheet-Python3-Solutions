#Question Link: https://takeuforward.org/data-structure/detect-a-cycle-in-a-linked-list/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=deabcc3e7f8757f1247137ad08b9ac8f&pid=700099&user=tiabhi1999

#Please refer the GFG question for complete code snippet (https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1)

class Solution:
    def detectLoop(self, head):
        if head is None or head.next is None:
            return False
        slow = fast = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
