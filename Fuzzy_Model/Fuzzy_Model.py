from .Rule import *
class FuzzyModel:
    def __init__(self,entries,results):
        self.entries = entries
        self.results = results
        self.rules = []
    
    def add_rule(self,antecedent,*consequences):
        self.rules.append(Rule(antecedent,*consequences))
    
    def print(self):
        print("Mis entradas son")
        for i in self.entries:
            print(i.name)
        print("Mis salidas son")
        for i in self.results:
            print(i.name)