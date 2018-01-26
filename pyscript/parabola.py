#code showing how fast pyplot can create a graph
from matplotlib import pyplot as plt
plt.plot(range(-50,50),[z ** 2for z in range(-50,50)],color='orangered')
plt.show()
