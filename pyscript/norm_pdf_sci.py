"""
normal probability density function in python
"""
from __future__ import division
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np

x = np.linspace(norm.ppf(0.01),norm.ppf(0.99),100)
plt.plot(x,norm.pdf(x),'r-',lw=2,alpha=0.6,label='norm pdf')
plt.title('Normal PDF')
plt.xlabel('x value')
plt.ylabel('Frequency of x value occuring')
plt.show()