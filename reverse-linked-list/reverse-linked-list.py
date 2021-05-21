# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_node = None
        while head:
            temp = head.next
            head.next = new_node
            new_node = head
            head = temp
        return new_node
            
        