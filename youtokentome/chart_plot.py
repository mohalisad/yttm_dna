# for running this code, be in the root of project and run:
# python ./youtokentome/chart_plot.py ./simpletest/bpe_pair_count_chart.txt ./simpletest/bpe_sentence_count_chart.txt

import sys
import matplotlib.pyplot as plt

all_inputs = sys.argv[1:]

fig = plt.figure()
ax1 = fig.add_subplot(111)

for file in all_inputs:
    x_values = list()
    y_values = list()

    file1 = open(file, 'r')
    count = 0
    while True:
        count += 1
        line = file1.readline()
        if not line:
            break
        line = line.strip()
        x_values.append(count)
        y_values.append(int(line))
    file1.close()

    ax1.scatter(x_values, y_values, label=file.split("/")[-1].split(".")[0])

plt.legend(loc='upper right')
plt.show()
