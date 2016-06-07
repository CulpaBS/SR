import json
import pygal
import numpy as np


with open("2nd_no_scanomap_fixed.json") as json_file:
    json_data = json.load(json_file)

keys = []
average_data = []

for data in json_data:
	 keys.append(int(data))

sorted_keys = sorted(keys)

for data in sorted_keys:
	average_data.append(round(np.average(json_data[str(data)]), 2))

with open("2nd_yes_scanomap_fixed.json") as json_file:
    json_data = json.load(json_file)

keys_yes = []
average_data_yes = []

for data in json_data:
	 keys_yes.append(int(data))

sorted_keys_yes = sorted(keys)

for data in sorted_keys_yes:
	average_data_yes.append(round(np.average(json_data[str(data)]), 2))


comparing_Results = []

for i in range(0, len(average_data)):
	comparing_Results.append(((average_data_yes[i] / average_data[i]) - 1)*(-100))


line_chart = pygal.Line(logarithmic=True, x_label_rotation=40, x_title='Input size', y_title='Microseconds')
line_chart.x_labels = map(str, sorted_keys)
line_chart.title = 'Average computation time'
line_chart.add("No scanomap", average_data)
line_chart.add("Yes scanomap", average_data_yes)
line_chart.render_to_png('chart.png')

line_chart = pygal.Bar(x_label_rotation=40, x_title='Input size', y_title='Percentage increase')
line_chart.title = 'Computation speedup'
line_chart.x_labels = map(str, sorted_keys)
line_chart.add('Result', comparing_Results)
line_chart.render()
line_chart.render_to_png('comparing.png')



# Futhark-C


with open("futhark-c-no-scanomap.json") as json_file:
    json_data = json.load(json_file)

keys = []
average_data = []

for data in json_data:
	 keys.append(int(data))

sorted_keys = sorted(keys)

for data in sorted_keys:
	average_data.append(round(np.average(json_data[str(data)]), 2))

with open("futhark-c-yes-scanomap.json") as json_file:
    json_data = json.load(json_file)

keys_yes = []
average_data_yes = []

for data in json_data:
	 keys_yes.append(int(data))

sorted_keys_yes = sorted(keys)

for data in sorted_keys_yes:
	average_data_yes.append(round(np.average(json_data[str(data)]), 2))


comparing_Results = []

for i in range(0, len(average_data)):
	comparing_Results.append(((average_data_yes[i] / average_data[i]) - 1)*(-100))

line_chart = pygal.Line(logarithmic=True, x_label_rotation=40, x_title='Input size', y_title='Microseconds')
line_chart.x_labels = map(str, sorted_keys)
line_chart.title = 'Average computation time'
line_chart.add("No scanomap", average_data)
line_chart.add("Yes scanomap", average_data_yes)
line_chart.render_to_png('futhark-c-chart.png')

line_chart = pygal.Bar(x_label_rotation=40, x_title='Input size', y_title='Percentage increase')
line_chart.title = 'Computation speedup'
line_chart.x_labels = map(str, sorted_keys)
line_chart.add('Result', comparing_Results)
line_chart.render()
line_chart.render_to_png('futhark-c-comparing.png')
