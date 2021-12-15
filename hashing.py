import random

class Hash:
    def __init__(self):
        self.mask = {}
    
    def hash_function(self, index):
        if self.mask.get(index) == None:
            random.seed(index)
            self.mask[index] = random.getrandbits(32)
        
        def hashUtil(word):
            return hash(word + str(index))^self.mask[index]
        
        return hashUtil
