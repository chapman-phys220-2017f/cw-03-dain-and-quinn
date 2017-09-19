#!/usr/bin/env python3

"""Gaussian Module Unit Tests"""

import nose
import math
import gaussian

def test_g():
    """Tests g with following trials:
        - g(0) ?= 1.0/sqrt(2pi)
    """
    # Pre-computed correct value of g(0)
    actual = 1.0/math.sqrt(2*math.pi)
    # Testing implementation
    trial = gaussian.g(0)
    # Debug messages like this are only printed if the test fails
    print("Testing g(0): ",actual," ?= ",trial)
    # an assert command is the actual test
    # for floats, be sure to use assert_almost_equal instead (here to 4 digits)
    nose.tools.assert_almost_equal(actual, trial, 4)

def test_interval():
    """Tests interval() with the following trials:
        - interval(x**2,0,10,1) ?= [0,1,4,9,16,25,36,49,64,81,100]
    """
    def f(x):
        return x**2
    actual = [0,1,4,9,16,25,36,49,64,81,100]
    trial = gaussian.interval(f,0,10,1)
    print("Testing interval(x**2,0,10,1): ",actual," ?= ",trial)
    nose.tools.assert_almost_equal(actual,trial,4)

def test_integrate():
    """Tests integrate() with the follwing trails:
        - i = integrate([0,1,4,9,16,25,36,49,64,81,100],1) ?= 335
    """
    actual = 335
    trial = gaussian.integrate([0,1,4,9,16,25,36,49,64,81,100],1)
    print("Testing integrate([0,1,4,9,16,25,36,49,64,81,100],1): ",actual," ?= ",trial)
    nose.tools.assert_almost_equal(actual,trial,4)

def test_gauss_norm():
    """Tests how accurately interval and integrate functions work on g when dx is samll.
        - integrate(interval(g,0,4,.05),.05)
    """
    actual = 0.49996821729336 #using online trapazoidal rule calcuator
    trial = gaussian.integrate(gaussian.interval(gaussian.g,0,4,.05),.05)
    print("Testing integrate(interval(g,0,4,.05),.05): ",actual," ?= ",trial)
    nose.tools.assert_almost_equal(actual,trial,4)
