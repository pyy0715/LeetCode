class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        
        output = 1
        cnt = 0
        
        for i in range(1, n+1):
            output = output * i 
            
        arr = list(str(output))
        for j in arr[::-1]:
            if j=='0':
                cnt+=1
            else:
                return cnt
        
                
                
                