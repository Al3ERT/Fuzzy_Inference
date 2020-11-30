class Predicate:
    def __call__(self,*args,**kwargs):
        pass
    
    def __neg__(self):
        return ComplementPredicate(self,other)

    def __and__(self,other):
        return AndPredicate(self,other)
    
    def __or__(self,other):
        return OrPredicate(self,other)

class ComplementPredicate(Predicate):
    def __init__(self, predicate:Predicate):
        self.predicate = predicate
    
    def __call__(self,*args,**kwargs):
        return 1-self.predicate(*args,**kwargs)
    
    def __str__(self):
        return f'¬({self.predicate})'

class AndPredicate(Predicate):
    def __init__(self, first:Predicate, second:Predicate):
        self.first = first
        self.second = second
    
    def __str__(self):
        return f'({self.first}) and ({self.second})'

    def __call__(self,*args,**kwargs):
        return min(self.first(*args,**kwargs),self.second(*args,**kwargs))
    

class OrPredicate(Predicate):
    def __init__(self, first:Predicate, second:Predicate):
        self.first = first
        self.second = second
    
    def __str__(self):
        return f'({self.first}) or ({self.second})'

    def __call__(self,*args,**kwargs):
        return max(self.first(*args,**kwargs),self.second(*args,**kwargs))