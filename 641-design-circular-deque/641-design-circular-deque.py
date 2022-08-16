from collections import deque

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.idx = 0
        self.arr = deque([])
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.idx>=self.size:
            return False
        else:
            self.arr.appendleft(value)
            self.idx+=1
            return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.idx>=self.size:
            return False
        else:
            self.arr.append(value)
            self.idx+=1
            return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.arr:
            self.arr.popleft()
            self.idx-=1
            return True
        else:
            return False
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.arr:
            self.arr.pop()
            self.idx-=1
            return True
        else:
            return False
    
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.arr[0]
        else:
            return -1
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.arr[self.idx-1]
        else:
            return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.arr:
            return False
        else:
            return True
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.size==self.idx:
            return True
        else:
            return False
            
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()