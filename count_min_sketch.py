from hash_table import Hash
import math 

class CountMinSketch:

    def __init__(self, eps, delta):
        self.m = int(1 / eps)
        self.d = int(math.log(1/delta, 2))
        self.sketch = [[0]*self.m for _ in range(self.d)]
        self.h = Hash()
        self.hash_functions = [self.h.hash_function(_) for _ in range(self.d)]
    
    def get_depth(self):
        return self.d

    def get_width(self):
        return self.m
        


    def add_word(self, word):
        for _ in range(self.d):
            idx = self.hash_functions[_](word)%self.m
            self.sketch[_][idx] += 1
    
    def get_count(self, word):
        count = min([self.sketch[_][self.hash_functions[_](word)%self.m] for _ in range(self.d)])
        return count
    
    def display_sketch(self):
        print(self.sketch)
    
    

        


