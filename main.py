import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Population import Population

population = Population()

# def animate_func(i):
#     ax1.clear()
#     population.update_population()
#     for i in range(0,len(population.population_list)):
#         plt.scatter(population.population_list[i].positionX, population.population_list[i].positionY, marker='o',
#                     s=population.population_list[i].Wealth[population.population_list[i].year])


# fig = plt.figure()
# ax1 = fig.add_subplot(1, 1, 1)
anim = animation.FuncAnimation(population.fig, population.animate_population, interval=100, repeat=False, frames=30)
plt.show()
