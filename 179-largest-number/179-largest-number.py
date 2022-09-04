
class Solution(object):
    @staticmethod
    def to_swap(n1, n2):
        return str(n1)+str(n2)<str(n2)+str(n1)
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        i = 1
        while i < len(nums):
            cur = i
            while cur>0 and self.to_swap(nums[cur-1], nums[cur]):
                nums[cur], nums[cur-1] = nums[cur-1], nums[cur]
                cur-=1
            i+=1
        return str(int(''.join(map(str, nums))))

        