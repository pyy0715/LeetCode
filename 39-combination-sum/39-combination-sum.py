class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def dfs(csum, index, path):
            if csum<0:
                return
            
            if csum==0:
                ans.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
                
        dfs(target, 0, [])
        return ans
                    
                