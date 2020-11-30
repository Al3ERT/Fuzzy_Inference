from scipy import trapz
import numpy

def Mean_of_maximum(fset,a,b,step=1):
    maxi = 0
    maxs = []
    values = numpy.arange(a,b+step,step)
    if len(values)==0:
        return 0
    for val in values:
        fval = fset.mem_func(val)
        if fval>maxi:
            maxi = fval
            maxs = [val]
        elif fval == maxi:
            maxs.append(val)
    return sum(maxs)/len(maxs)

def Center_of_area(fset,a,b,step=1):
    nsum = 0
    dsum = 0
    values = numpy.arange(a,b+step,step)
    for val in values:
        fval = fset.mem_func(val)
        nsum += fval*val
        dsum += fval
    if dsum!=0:
        return nsum/dsum
    return 0

def Bisector_of_area(fset,a,b,step=1,rep=100):
    def integrate(a,b):
        fvals = [fset.mem_func(x) for x in numpy.arange(a,b+step,step)]
        return trapz(fvals,dx=step)
    middle = 0
    inf,sup = a,b    
    while inf < sup and rep > 0:
        middle = (inf+sup)/2
        low = integrate(a,middle)
        high = integrate(middle,b)
        if low > high:
            sup = middle
        elif high > low:
            inf = middle
        else:
            return middle
        rep = rep-1
    return middle
        

