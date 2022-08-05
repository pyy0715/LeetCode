class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [None]*k
        self.max_len = k
        self.front = 0
        self.rear = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.queue[self.rear] is None:
            self.queue[self.rear]=value
            self.rear = (self.rear + 1) % self.max_len
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.queue[self.front] is None:
            return False
        else:
            self.queue[self.front]=None
            self.front = (self.front + 1) % self.max_len
            return True
        

    def Front(self):
        """
        :rtype: int
        """
        return -1 if self.queue[self.front] is None else self.queue[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        return -1 if self.queue[self.rear-1] is None else self.queue[self.rear-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.queue[self.front] is None
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.front==self.rear and self.queue[self.front] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()