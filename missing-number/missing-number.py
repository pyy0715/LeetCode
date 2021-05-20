class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        for i in sorted(nums):
            if i==start:
                start+=1
            else:
                return start
        return start
            
            
        