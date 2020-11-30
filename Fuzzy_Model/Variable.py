from .Fuzzy_Set import *

class Variable:
    def __init__(self, name:str, *subsets):
        self.name = name
        self.subsets = {x.name: x  for x in subsets}
    
    def __getitem__(self,name):
        return FuzzySet(name,self.subsets[name].mem_func,self.name)

    def __eq__(self,other):
        return self.name == other.name