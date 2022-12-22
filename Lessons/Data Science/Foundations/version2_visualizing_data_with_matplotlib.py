from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# define the range of x-values
hour = range(24)

# define the y-values
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

# define the title
plt.title("Codecademy Learners Time Series")

# define the x-axis label
plt.xlabel("Hour")

# define the y-axis label
plt.ylabel("Viewers")

# plot the data
plt.plot(hour, viewers_hour)

# define a legend
plt.legend(['2015-01-01'])

# add a subplot
ax = plt.subplot()

# set the color of the subplot
ax.set_facecolor('seashell')

# define the data for the subplot
ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

# Loop through the data
y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

# fill the area between y_upper and y_lower
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

# show the plot
plt.show()