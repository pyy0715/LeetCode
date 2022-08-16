# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = result = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
            
        while heap:
            node = heapq.heappop(heap)
            
            result.next = node[-1]
            
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, result.next))
            
        return root.next
            
        
        
        