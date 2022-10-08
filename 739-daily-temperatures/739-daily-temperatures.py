from collections import deque

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        
        stack = []
        
        for i,cur in enumerate(temperatures):
            while stack and cur>temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i-last
            stack.append(i)
            
                
        return answer