import pygal

from die import Die

#
die_1 = Die()
die_2 = Die(10)

#
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

#
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
    '13', '14', '15', '16']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file(r'images\different_dice.svg')


