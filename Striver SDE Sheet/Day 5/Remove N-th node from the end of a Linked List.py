#Question Link: https://takeuforward.org/data-structure/remove-n-th-node-from-the-end-of-a-linked-list/
#Solution Link (Python3): https://leetcode.com/submissions/detail/656748126/


class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def removeKthNode(head, k):
    if k == 0:
        return head
    dummy = Node(-1)
    dummy.next = head
    f = dummy
    s = dummy
    for i in range(k):
        if f.next is None:
            return
        f = f.next
    while(f.next is not None):
        s = s.next
        f = f.next
    if s == dummy:
        return head.next
    
    s.next = s.next.next
    return head
    

def build_linkedList(arr):
    head = None
    for i in range(len(arr)):
        if arr[i] == -1:
            break

        new = Node(arr[i])

        if head is None:
            head = new
            tail = new

        else:
            tail.next = new
            tail = tail.next

    return head



t = int(input().strip())
for i in range(t):
    k = int(input().strip())
    arr = [int(i) for i in input().strip().split()]

    head = build_linkedList(arr)
    res_head = removeKthNode(head, k)

    while res_head is not None:
        print(res_head.data, end= " ")
        res_head = res_head.next
    print(-1)
