from Income.Individual import Individual
import matplotlib.pyplot as plt
import statistics

class Population:
    def __init__(self, population_size, simulation_length):
        self.population_size = population_size
        self.population_list = []
        self.wealth_list = []
        self.mean_list = []
        self.stdev_list = []

        self.fig, (self.plot1, self.plot2, self.plot3) = plt.subplots(3, 1)
        self.plot2.set_xlim([0, simulation_length])
        self.plot3.set_xlim([0, simulation_length])

        for i in range(0, self.population_size):
            individual = Individual()
            self.population_list.append(individual)

    def update_population(self):
        self.wealth_list = []

        for i in range(0, len(self.population_list)):
            self.population_list[i].simulate_year()
            self.wealth_list.append(self.population_list[i].Wealth[-1])

    def animate_population(self, i):
        self.plot1.clear()
        self.update_population()
        for ind in range(0, len(self.population_list)):

            if self.population_list[ind].Wealth[self.population_list[ind].year] > 1:
                s = self.population_list[ind].Wealth[self.population_list[ind].year]
            else:
                s = 0

            self.plot1.scatter(self.population_list[ind].positionX, self.population_list[ind].positionY, marker='o', s=s)

        #print(self.wealth_list)
        self.mean_list.append(statistics.mean(self.wealth_list))
        self.plot2.plot(self.mean_list)
        self.stdev_list.append(statistics.stdev(self.wealth_list) / statistics.mean(self.wealth_list))
        self.plot3.plot(self.stdev_list)
