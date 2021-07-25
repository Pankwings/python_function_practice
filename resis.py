import math as m

def res_par(r,c,f):
    return((r*(1/2*m.pi*f*c))/(r+(1/2*m.pi*f*c)))
r = 2
c = 2
f = 1
result = res_par(r,c,f)
print(result)
