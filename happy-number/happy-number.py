class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        save_sum = []
        while True:
            sum = 0
            
            for num in str(n):
                sum += int(num) * int(num)
                
            if sum == 1:
                return True
            else:
                n = str(sum)
            
            if int(n) in save_sum:
                return False
            else:
                save_sum.append(int(n))
        return False
        