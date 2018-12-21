import pygal

from die import Die

#
die_1 = Die()
die_2 = Die(10)

#
results = [die_1.roll()+die_2.roll() for roll_num in range(50000)]

#
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

#
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
#   '13', '14', '15', '16']
hist.x_labels = [str(label_value) for label_value in range(2, max_result+1)]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file(r'images\different_dice_wListComprehension.svg')



