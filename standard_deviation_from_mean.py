"""
find the standard normal distribution 
of the value of the prizes on 39 episodes of golden balls

what can approximately be taken from this
is we could find the percentage chance of individuals winning 
these (standardized) amounts, if we look at the integral value between
two intervals on the graph
"""

import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import mlab

df = pd.read_csv('golden_balls_final.csv')
prize_values = df['prize_value_gbp']
finalist_1_gender = df['finalist_1_gender']
finalist_2_gender = df['finalist_2_gender']
split_or_steal_1 = df['split_or_steal_finalist_1']
split_or_steal_2 = df['split_or_steal_finalist_2']

def normal_pdf(x,mu=0,sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

mean_prize = np.mean(prize_values)
st_dev_prize = np.std(prize_values)

#standardizing is also useful for working with data which is in different units
#effectively what we are doing is making everything 'x' standard deviations away from the mean
standardized_prizes = []
for prize in prize_values:
    standardized_prizes.append((prize - mean_prize) / st_dev_prize)

#absolute mess, unable to see the curve
#plt.plot(standardized_prizes,[normal_pdf(x) for x in standardized_prizes])

#scatter plot much clearer
plt.scatter(standardized_prizes,[normal_pdf(x) for x in standardized_prizes],s=10,c='red')
plt.title('PDF Showing Prize Value on Golden Balls ')
plt.show()
