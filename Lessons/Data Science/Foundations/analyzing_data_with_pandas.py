# parse csv file
import pandas as pd

# read csv file
df = pd.read_csv('/Applications/Code/Codecademy/Lessons/Data Science/Foundations/CSV files/languages-spoken-total-responses-2018-census-csv.csv')

# print first 5 rows
print(df.head())

# print last 5 rows
print(df.tail())