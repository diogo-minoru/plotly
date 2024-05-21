from random import randint

class Die:
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    
die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []

max_result = die1.num_sides + die2.num_sides

poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


import plotly.express as px

title = "Resultados de dois dados sendo jogados 1000 vezes"
labels = {"x": "Result", "y": "Frequency of Result"}

fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

# Fazer com que cada coluna tenha sua própria legenda no valor do eixo x
fig.update_layout(xaxis_dtick = 1)

fig.show()
