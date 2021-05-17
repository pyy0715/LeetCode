class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        result = [[area, 1]]
        temp = area
        
        for i in range(1, area):
            if area % i == 0:
                j = area//i
                if 0<=j-i<=temp:
                    temp=j-i
                    result.append([j,i])
            
        return result[-1]
        