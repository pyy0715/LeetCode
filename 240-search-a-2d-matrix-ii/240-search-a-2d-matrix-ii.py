class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        row, col = 0, len(matrix[0])-1
        
        
        while row<=n-1 and col>=0:
            if target==matrix[row][col]:
                return True
            
            elif target>matrix[row][col]:
                row+=1
                
            else:
                col-=1
                
        return False  
            
                
            