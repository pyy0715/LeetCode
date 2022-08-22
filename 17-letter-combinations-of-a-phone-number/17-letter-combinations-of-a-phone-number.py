from collections import defaultdict

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_dict = {'2': list('abc'), 
                      '3': list('def'),
                      '4': list('ghi'),
                      '5': list('jkl'),
                      '6': list('mno'),
                      '7': list('pqrs'),
                      '8': list('tuv'),
                      '9': list('wxyz')
                     }
        
        result = []
        if not digits:
            return result
        
        def dfs(index, s):
            if len(s)==len(digits):
                result.append(s)
                return 
            
            for i in range(index, len(digits)):
                for j in digit_dict[digits[i]]:
                    dfs(i+1, s+j)
                    
        dfs(0, "")
        return result
        
        
            
                
            
            
            
        