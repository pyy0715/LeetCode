from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        
        length = [0]
        stack = [s[0]]
        s_list = deque(list(s)[1:])
        
        while s_list:
            temp = s_list.popleft()
            
            if temp not in stack:
                stack.append(temp)
            else:
                length.append(len(stack))
                k = stack.index(temp)
                stack = stack[k+1:] + [temp]
                
        length.append(len(stack))
        return max(length)