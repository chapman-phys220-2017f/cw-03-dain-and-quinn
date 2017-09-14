#!/usr/bin/env python3

import math
def g(x):
    return ((1/(2*math.pi)**.5)**(-(x**2)/2))

def interval(f,a,b,dx):
    n = (b-a)/dx
    return [f(a+i*dx) for i in range(n)]

def integrate(i,dx):
    total = 0
    for e in range(len(i)):
        if (e>=1 and e<len(i)):
            total+=(2*i[e])
        elif (e==0 or e==len(i)):
            total+=i[e]
        else: total+=0
    return (dx*total/2)


