import random
import math

class NaiveHash:

    def __init__(self, size):
        self.hash_size = int(size*0.75)
        self.table = [0]*self.hash_size
    
    def hash_function(self, word):
        prime = 2147483647
        a = random.randint(0, prime)
        b = random.randint(0, prime)
        word = int(''.join([format(ord(char), 'b') for char in word]))
        return ((a*word + b)%prime)%self.hash_size
    
    def add_word(self, word):
        idx = self.hash_function(word)
        self.table[idx] += 1
    
    def get_count(self, word):
        return self.table[self.hash_function(word)]
    
    
