import sympy
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x=symbols("x")    # declares the normal variable x as a Sympy symbol
s = input("")
exp1 = exp(sympify(s))   #converts the string function input  by the user to mathematical form 
kval=[]
tval=[]
yval=[]

for y in np.arange(0,1,0.1):  #for varying value between 0 to 1 with 0.1 increament of the input argument of the function input by the user
    for k in np.arange(1,0.001,-0.01): # varying step size
        t= ((diff(exp1,x)).subs(x,y)) - ((exp1.subs(x,(y+k))-exp1.subs(x,y))/k)
        #print (t.evalf())   #increases load on interpreter 
        kval.append(k)       #looping using index create an error "out of range"
        tval.append(t.evalf())
    yval.append(y)
        
        
plt.plot(tval,kval)         #using matplotlib for plotting 2-d graphs
plt.show()
