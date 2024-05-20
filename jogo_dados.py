from random import randint

class Die:
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    
die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


import plotly.express as px

title = "Resultados de 1000 dados"
labels = {"x": "Result", "y": "Frequency of Result"}

fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.show()
