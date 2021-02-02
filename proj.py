import sympy
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x=symbols("x")
s = input("")
exp1 = exp(sympify(s))
kval=[]
tval=[]
yval=[]

for y in np.arange(0,1,0.1):
    for k in np.arange(1,0.001,-0.01):
        t= ((diff(exp1,x)).subs(x,y)) - ((exp1.subs(x,(y+k))-exp1.subs(x,y))/k)
        #print (t.evalf())
        kval.append(k)
        tval.append(t.evalf())
    yval.append(y)
        
        
plt.plot(tval,kval)
plt.show()
