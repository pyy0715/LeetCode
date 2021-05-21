class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = list(set(nums1).intersection(set(nums2)))
        result = []
        for i in arr:
            temp = min(nums1.count(i), nums2.count(i))
            result+=[i]*temp
        return result
            