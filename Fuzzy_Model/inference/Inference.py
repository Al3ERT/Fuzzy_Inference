from ..Fuzzy_Model import *
from ..Fuzzy_Set import *

def build_default(func,default,minim):
    def MinDefault(*args,**kwargs):
        return min(func(*args,**kwargs),default)
    def MulDefault(*args,**kwargs):
        return func(*args,**kwargs)*default
    if minim:
        return MinDefault
    return MulDefault

def build_fcomparer(minim,*functions):
    def Min(*args,**kwargs):
        return min((function(*args,**kwargs) for function in functions),default=0)
    def Max(*args,**kwargs):
        return max((function(*args,**kwargs) for function in functions),default=0)
    if minim:
        return Min
    return Max

def Mamdani(model,*vals, **nums):
    results = {c.name: [] for c in model.results}
    values = nums
    if not values:
        values = {a.name: num for a, num in zip(model.entries,vals)}
    for rule in model.rules:
        default = rule.antecedent(**values)
        for cons in rule.consequences:
            results[cons.universe].append(build_default(cons.mem_func,default,True))
    retu = []
    for result in model.results:
        fset = FuzzySet("Mamdani",build_fcomparer(False,*results[result.name]),result.name)
        retu.append(fset)
    return retu

def Larsen(model,*vals, **nums):
    results = {c.name: [] for c in model.results}
    values = nums
    if not values:
        values = {a.name: num for a, num in zip(model.entries,vals)}
    for rule in model.rules:
        default = rule.antecedent(**values)
        for cons in rule.consequences:
            results[cons.universe].append(build_default(cons.mem_func,default,False))
    retu = []
    for result in model.results:
        fset = FuzzySet("Larsen",build_fcomparer(False,*results[result.name]),result.name)
        retu.append(fset)
    return retu

    