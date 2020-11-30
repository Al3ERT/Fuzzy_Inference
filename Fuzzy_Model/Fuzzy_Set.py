from .Predicate import *
from .fuzzify import *
from matplotlib import pyplot
class FuzzySet(Predicate):
    def __init__(self,name:str, membership_function:MembershipFunction,universe:str = ""):
        self.universe = universe
        self.name = name
        self.mem_func = membership_function
    
    def __call__(self,**values):
        if self.universe in values:
            return self.mem_func(values[self.universe])
        return 0

    def plot(self,domain):
        x = list(domain)
        y = [self.mem_func(i) for i in x]
        pyplot.figure()
        pyplot.plot(x,y,"ro")
        pyplot.suptitle(self.name)
        pyplot.show()
    
