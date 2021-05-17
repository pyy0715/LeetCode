class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans, vals = set(), set()
        for x in A: 
            vals = {x | xx for xx in vals} | {x}
            ans |= vals
        return len(ans)
            
         