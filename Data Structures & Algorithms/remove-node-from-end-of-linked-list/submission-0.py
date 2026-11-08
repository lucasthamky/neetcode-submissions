# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            count = count + 1
            current = current.next


        if n == count:
            return head.next

        current = head
        for x in range(count - n - 1):
            current = current.next

        current.next = current.next.next


        return head


        

            
