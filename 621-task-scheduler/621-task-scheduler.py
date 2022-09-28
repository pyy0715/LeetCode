from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, val in counter.most_common(n + 1):
                if val>0:
                    sub_count += 1
                    result += 1
                    counter[task]-=1
                    
            if sum(counter.values())==0:
                break

            result += n - sub_count + 1

        return result
            
            
                
            
        
        