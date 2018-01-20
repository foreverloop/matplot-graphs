from matplotlib import pyplot as plt
import math

#linear line plot
x = range(100)
y = [z * 0.2 + 3 for z in x]
plt.plot(x,y,color='orangered')
plt.show()

#parabola plot, x squared
sq = [z **2 for z in range(-50,50)]
sqx = range(-50,50)
plt.plot(sqx,sq)
plt.show()

#error function plot
y = [math.erf(x) for x in range(-50,50)]
x = range(-50,50)
plt.plot(x,y)
plt.show()

#natural logarithmic plot
x = range(1,101)
y = [math.log(z) for z in x]
plt.plot(x,y)
plt.show()

#exponential plot (no negatives)
x = range(100)
y = [z ** 3 for z in x]
plt.plot(x,y)
plt.show()