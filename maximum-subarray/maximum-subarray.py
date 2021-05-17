class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = []
        output = 0
        
        for i in nums:
            if i < 0:
                output+=i
            else:
                output = max(output+i, i)
                
            result.append(output)
            
        return max(max(result), max(nums))