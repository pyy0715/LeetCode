import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.sub('[^a-zA-Z\s]', ' ', paragraph)
        arr = paragraph.lower().split()
  
        for k,v in sorted(Counter(arr).items(), key=lambda x: x[-1], reverse=True):

            if k not in banned:
                return k
        
            
        