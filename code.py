#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Q2
"""
Created on Thu Oct 21 23:16:33 2021

@author: 

  Q1
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp as si

def syst(t, y, sigma, r, beta):
    dx = sigma*(y[1] - y[0])
    dy = y[0] * (r - y[2]) - y[1]
    dz = y[0] * y[1] - beta * y[2]
    return (dx, dy, dz)

C0 = [1, 1, 1]
temps = [0, 100]
sigma = 10
beta = 8/3
r = 10

sol = si(lambda t, y: syst(t, y, sigma, r, beta), temps, C0, rtol=10**-9, atol=10**-9)

plt.figure()
plt.plot(sol.y[0,:],sol.y[1,:]);
plt.xlabel('$X$')
plt.ylabel('$Y$')

plt.figure()
plt.plot(sol.y[0,:],sol.y[2,:]);
plt.xlabel('$X$')
plt.ylabel('$Z$')



plt.figure()
plt.plot(sol.y[1,:],sol.y[2,:]);
plt.xlabel('$Y$')
plt.ylabel('$Z$')
