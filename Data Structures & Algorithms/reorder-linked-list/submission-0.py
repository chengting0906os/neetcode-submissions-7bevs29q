# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into two parts
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = slow.next
        slow.next = None

        # reverse second part
        prev = None
        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt
        list2 = prev
        # combine
        
        while list2:
            temp1 = list1.next
            list1.next = list2
            list1 = temp1
            temp2 = list2.next
            list2.next = temp1
            list2 = temp2
            
            




             

