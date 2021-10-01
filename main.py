import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Population import Population

simulation_length = 50
population = Population(10, simulation_length)

anim = animation.FuncAnimation(population.fig, population.animate_population, interval=20, repeat=False, frames=simulation_length)
plt.show()
