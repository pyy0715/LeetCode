class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(index, path):
            if index>len(nums):
                return
            else:
                res.append(path)
            
            
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
                
        dfs(0, [])
        return res
        
        