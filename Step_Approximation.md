# <ins>This script takes a function as a string and converts it to mathematical forms using Sympy, at a particular value of 'y' , the difference between the values of  derivative at y of the function f(x) calculated by analytical(using diff function of Sympy and using step-approximation of first principle )is calculated and plotted for different sizes of the step varying from 1 to 0.05 with a decrement of 0.005 in each loop . 
import sympy
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x=symbols("x")
s = input("")
exp1 = exp(sympify(s))
kval=[]
tval=[]
y=2
for k in np.arange(1,0.05,-0.01):
    t= ((diff(exp1,x)).subs(x,y)) - ((exp1.subs(x,(y+k))-exp1.subs(x,y))/k)
    print (t.evalf())
    kval.append(k)
    tval.append(t.evalf())
plt.plot(tval,kval)
plt.show()
