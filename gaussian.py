#!/usr/bin/env python3

import math
def g(x):
    return ((1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2))

def interval(f,a,b,dx):
    """f must be previously defined.  Gives the y-values of f over interval (a,b) with distance dx between each point"""
    n = int((b-a)/dx)    
    return [f(a+i*dx) for i in range(n+1)]

def integrate(i,dx):
    """Takes the y values from interval then uses the trapazoidal rule to approximate the area beneath the curve"""
    total = 0
    for e in range(len(i)):
        total = total + 2*i[e]
    total = total- (i[0]+i[-1])
    return (dx*total/2)


