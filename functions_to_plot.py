# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

def func_0():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x \in \Re$"
    
    title = "$x-x^2$"
    
    return x, x-x**2, label, title

def func_1():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x \in \Re $"
    
    title = "$x^2*sinx$"
    
    return x, x**2*np.sin(x), label, title

def func_2():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x \in \Re$"
    
    title = "$x^2*cosx$"
    
    return x, x**2*np.cos(x), label, title

def func_3():
    
    x = np.arange(-10, 10, 0.1)
    
    x = np.setdiff1d(x, [0])
    
    y = np.piecewise(x, [(x < -0.01), ((x >= -0.01) & (x <= 0.01)), (x > 0.01)],
                    [lambda x: np.abs(x)/x, np.nan, lambda x: np.abs(x)/x])
    
    label = "$x \in\Re$ \ $\{0\}$"
    
    title = "$|x|/x$"
    
    return x, y, label, title

def func_4():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x \in (-\infty;-1) \cup (1;\infty)$"
    
    y = np.piecewise(x, [(x < -1.01), (x >= -1.01) & (x <= 1.01), (x > 1.01)],
                    [lambda x: np.log2(x**2-1), np.nan, lambda x: np.log2(x**2-1)])
    
    title = "$log_2(x^2-1)$"
    
    return x, y, label, title

def func_5():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x \in \Re$"
    
    title = "$(x-1)/(x^2+1)$"
    
    return x, (x-1)/(x**2+1), label, title

def func_6():
    
    label = "$x \in \Re$"
    
    title = "$(x^2-1)/(x^2+1)$"
    
    x = np.arange(-10, 10, 0.1)
    
    return x, (x**2-1)/(x**2+1), label, title

def func_7():
    
    x = np.arange(-10, 10, 0.1)
    
    x = np.setdiff1d(x, [-2, 2])
    
    label = "$x \in \Re$ \ $\{-2;2\}$"
    
    title = "$x^3/(x^2-4)$"
    
    y = np.piecewise(x, [(x < -2.01), (x >= -2.01) & (x <= -1.99), (x>-1.99) & (x < 1.99), (x>=1.99) & (x<=2.01), (x > 2.01)],
                    [lambda x: x**3/(x**2-4), np.nan, lambda x: x**3/(x**2-4),np.nan,  lambda x: x**3/(x**2-4)])
    
    
    return x, y, label, title

def func_8():
    
    label = "$x \in \Re$"
    
    title = "$2^{cosx}$"
    
    x = np.arange(-10, 10, 0.1)
    
    return x, 2**np.cos(x), label, title

def func_9():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x \in \Re$"
    
    title = "$2^x-2^{-x}$"
    
    return x, 2**x-2**(-x), label, title