from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        stone_counter = Counter(stones)
        
        answer = 0
        for s in jewels:
            answer+=stone_counter[s]
        return answer
        