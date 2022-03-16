#Question Link: https://takeuforward.org/data-structure/add-two-numbers-represented-as-linked-lists/
#Solution Link (Python3): (leetcode) https://leetcode.com/submissions/detail/634880320/
#(GeeksforGeeks): https://practice.geeksforgeeks.org/viewSol.php?subId=2c843189df2c03e5ffa62658f28bb65e&pid=700043&user=tiabhi1999


#Refer leetcode question link for the complete code snippet (https://leetcode.com/problems/add-two-numbers/)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        temp = dummy
        s = 0
        carry = 0
        while(l1 is not None or l2 is not None or carry != 0):
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            s += carry
            carry = s//10
            node = ListNode(s%10)
            temp.next = node
            temp = temp.next
        return dummy.next
            
        
