class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        arr = []
        for i in range(len(columnTitle)):
            arr.append(ord(columnTitle[i])-64)
        
        n = len(arr)
        out = 0
        for idx, x in enumerate(arr):
            temp = 26 ** (n-idx-1)
            out += temp*x
        return out
            
            
            
            
            
            
        