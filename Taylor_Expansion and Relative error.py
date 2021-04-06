import sympy
from sympy import *
import numpy as np
x=symbols("x")
s = input()
l=10
exp1 = (sympify(s))
expf = Function('expf')
expf=0
exp2=exp1
print(exp2)

for n in np.arange(1,l,1):
    k=n        
    for k in np.arange(n,0,-1):
        exp2 = diff(exp2)/k
    ta=exp2*(x**n)
    expf=ta+expf
    exp2=exp1

#print(expf)
p1=plot(expf)
p1.show

import matplotlib.pyplot as plt

errval=[]
yval=[]
for y in np.arange(-10,10,0.1):
    err = (exp1.subs(x,y)-expf.subs(x,y))/exp1.subs(x,y)
    yval.append(y)
    errval.append(err)
    
p2 = plt.plot(yval,errval)
p2.show()
