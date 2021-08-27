import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Population import Population

population = Population()

anim = animation.FuncAnimation(population.fig, population.animate_population, interval=100, repeat=False, frames=30)
plt.show()
