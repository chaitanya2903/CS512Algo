import hashlib
from hashing import Hash

class CountMinSketch:

    def __init__(self, m, d):
        if not m or not d:
            raise ValueError("m and d have to be non-zero")
        self.m = m
        self.d = d
        self.sketch = [[0]*self.m for _ in range(self.d)]
        self.h = Hash()
        self.hash_functions = [self.h.hash_function(_) for _ in range(self.d)]
        
        


    def add_word(self, word):
        for _ in range(self.d):
            idx = self.hash_functions[_](word)%self.m
            self.sketch[_][idx] += 1
    
    def get_count(self, word):
        return min([self.sketch[_][self.hash_functions[_](word)%self.m] for _ in range(self.d)])
    
    def display_sketch(self):
        print(self.sketch)
    
    

        


