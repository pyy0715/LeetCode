from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        deq = deque([])
        ans = []
        
        for i,v in enumerate(nums):
            if deq and i-deq[0]==k:
                deq.popleft()
                
            while deq and nums[deq[-1]]<=nums[i]:
                deq.pop()
                
            deq.append(i)
            
            if i+1>=k:
                ans.append(nums[deq[0]])
        return ans
                