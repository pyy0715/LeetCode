from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'(':1, ')':-1,
                        '[':2, ']':-2,
                        '{':3, '}':-3,
                       }
        arr = deque(list(s))
        
        if arr[0] not in ['(', '[', '{']:
            return False
        
        stack = []
        
        while arr:
            temp = arr.popleft()
            
            if temp in ['(', '[', '{']:
                stack.append(temp)
            else:
                try:
                    que = stack.pop()
                except:
                    return False
                if bracket_dict[que]+bracket_dict[temp] != 0:
                    return False
        return False if stack else True