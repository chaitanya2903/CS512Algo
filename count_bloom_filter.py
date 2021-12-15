from hashing import Hash
import math

class CBF:

    def __init__(self, ninputs, fpp):
        self.ninputs = ninputs 
        self.fpp = fpp
        self.size = int(-1*round (self.ninputs * math.log (self.fpp)/(math.log(2) ** 2)))
        self.bloom = [0]*self.size
        self.nhash = int(round((self.size/self.ninputs) * math.log(2)))
        h = Hash()
        self.hash_functions = [h.hash_function(_) for _ in range(self.nhash)]
    
    def add_word(self, word):
        for _ in range(self.nhash):
            idx = self.hash_functions[_](word)%self.size
            self.bloom[idx] += 1
    
    def get_count(self, word):
        idx = self.hash_functions[0](word)%self.size
        return self.bloom[idx]
    
    
