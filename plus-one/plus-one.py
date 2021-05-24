class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = ''.join(map(str, digits))
        return list(str(int(out)+1))