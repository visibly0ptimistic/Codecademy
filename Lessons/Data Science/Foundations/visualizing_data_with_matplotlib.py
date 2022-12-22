from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('/Applications/Code/Codecademy/Lessons/Data Science/Foundations/CSV files/languages-spoken-total-responses-2018-census-csv.csv')

# plot the data
plt.plot(data['Languages_spoken'], data['Census_usually_resident_population_count'], color='red', marker='o')

# set the x-axis label
plt.xlabel('Language')

# set the y-axis label
plt.ylabel('Total Responses')

# set the title
plt.title('Total Responses by Language')

# show the plot
plt.show()
