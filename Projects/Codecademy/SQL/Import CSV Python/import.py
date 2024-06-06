# Import required modules
import csv
import sqlite3

# Connecting to the database
connection = sqlite3.connect('database_name.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE table_name(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column_1 TEXT NOT NULL,
                column_2 INTEGER NOT NULL);
                '''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the csv file
file = open('csv_file_name.csv')

# Reading the contents of the csv file
contents = csv.reader(file)

# SQL query to insert data into the table
insert_records = "INSERT INTO table_name (column_1, column_2) VALUES(?, ?)"

# Importing the contents of the file into the table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from the table 
# This step verifies that the data of the csv file has been successfully inserted into the table
select_all = "SELECT * FROM table_name"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
	print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()
