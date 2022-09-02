class Trie(object):

    def __init__(self):
        self.bow = set()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.bow.add(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.bow:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for i in self.bow:
            if i.startswith(prefix):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)