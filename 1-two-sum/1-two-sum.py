from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num2idx = defaultdict(list)
        for idx, n in enumerate(nums):
            num2idx[n].append(idx)
        
        start = 0
        end = len(nums)-1
        nums.sort()
        
        while start<end:
            if nums[start]+nums[end]>target:
                end-=1
            elif nums[start]+nums[end]<target:
                start+=1
            else:
                break

        first = nums[start]
        second = nums[end]
        
        if first==second:
             return [num2idx[first][0], num2idx[second][1]]
        else:
            return [num2idx[first][0], num2idx[second][0]]

                
            
            
            
            
            
            
        