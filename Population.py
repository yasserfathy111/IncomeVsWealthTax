from Income.Individual import Individual
import matplotlib.pyplot as plt


class Population:
    def __init__(self):
        self.population_size = 10
        self.population_list = []

        self.fig = plt.figure()
        self.plot1 = self.fig.add_subplot(1, 1, 1)

        for i in range(0, self.population_size):
            individual = Individual()
            self.population_list.append(individual)

    def update_population(self):
        for i in range(0, len(self.population_list)):
            self.population_list[i].simulate_year()


    def animate_population(self, i):
        self.plot1.clear()
        self.update_population()
        for i in range(0, len(self.population_list)):

            if self.population_list[i].Wealth[self.population_list[i].year] > 1:
                s = self.population_list[i].Wealth[self.population_list[i].year]
            else:
                s = 0

            plt.scatter(self.population_list[i].positionX, self.population_list[i].positionY, marker='o',
                        s=s)

