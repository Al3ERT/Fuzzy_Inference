import math

class MembershipFunction:
    def __init__(self,*args):
        pass

class Gamma(MembershipFunction):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __call__ (self,value):
        if value <= self.x:
            return 0
        if self.x <= value and value<=self.y:
            return (value-self.x)/(self.y-self.x)
        return 1

class LFunction(Gamma):
    def __call__ (self,value):
        return 1 - super().__call__(value)

class Triangular(MembershipFunction):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __call__ (self,value):
        if value <= self.x:
            return 0
        if value <= self.y:
            return (value-self.x)/(self.y-self.x)
        if value <= self.z:
            return (self.z-value)/(self.z-self.y)
        return 0

class Trapezoidal(MembershipFunction):
    def __init__(self,w,x,y,z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
    
    def __call__(self,value):
        if value <= self.w: 
            return 0
        if value <= self.x:
            return (value-self.w)/(self.x-self.w)
        if value <= self.y:
            return 1
        if value <= self.z:
            return (self.z-value)/(self.z-self.y)
        return 0

class SFunction(MembershipFunction):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __call__(self,value):
        if value <= self.x:
            return 0
        if value <= (self.x+self.y)/2:
            return 2*((value-self.x)/(self.y-self.x))**2
        if value < self.y:
            return 1 - 2*((value-self.y)/(self.y-self.x))**2
        return 1

class ZFunction(SFunction):
    def __call__(self,value):
        return 1 - super().__call__(value)

class Gaussian(MembershipFunction):
    def __init__(self,w,x,y,z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.sfunc = SFunction(w,x)
        self.zfunc = ZFunction(y,z)
    
    def __call__(self,value):
        if value<=self.x:
            return self.sfunc(value)
        if value >= self.y:
            return self.zfunc(value)
        return 1

class Bell(MembershipFunction):
    def __init__(self,m,v):
        self.m = m
        self.v = v
    
    def __call__(self,value):
        return math.e**(-(value-self.m)**2/(2*self.v))