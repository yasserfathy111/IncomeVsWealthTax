import random

import matplotlib.pyplot as plt


class Individual:
    def __init__(self):

        self.positionX = random.randint(0, 100)
        self.positionY = random.randint(0, 100)

        self.InitialIncome = 100
        self.IncomeChangeRate = 0.1
        self.IncomeChangeRateInst = self.IncomeChangeRate
        self.ExpensesRate = 0.7
        self.ExpensesRateInst = self.ExpensesRate
        self.IncomeTaxRate = 0.3

        self.Income = [self.InitialIncome]
        self.IncomeTaxes = [0]
        self.Expenses = [0]
        self.Savings = [0]
        self.Wealth = [0]

        self.year = 0

    def simulate_year(self):
        self.increment_year()

        self.IncomeChangeRateInst = self.IncomeChangeRate + (random.randint(-15, 15)/100)
        self.Income.append(self.Income[self.year - 1] * (1 + self.IncomeChangeRateInst))
        self.IncomeTaxes.append(self.Income[self.year] * self.IncomeTaxRate)

        self.ExpensesRateInst = self.ExpensesRate + (random.randint(-40, 40)/100)
        self.Expenses.append((self.Income[self.year] - self.IncomeTaxes[self.year]) * self.ExpensesRateInst)

        self.Savings.append(self.Income[self.year] - self.IncomeTaxes[self.year] - self.Expenses[self.year])
        self.Wealth.append(self.Wealth[self.year - 1] + self.Savings[self.year])

        # self.positionX += random.randint(-5, 5)
        # self.positionY += random.randint(-5, 5)

    def increment_year(self):
        self.year += 1

    def plot(self):
        plt.plot(self.Income)
        plt.plot(self.Wealth)
        plt.show()

