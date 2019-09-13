import sqlite3 

# Part 1: Making and Populating a Database

# Opening a'blank' DataBase File Connection 
# 'demo_data.sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS demo")

# Creating Demo Table 

create_demo_table = """
CREATE TABLE demo ( 
  s PRIMARY KEY,
  x INT,
  y INT
)
"""

#Executing Table Creation
curs.execute(create_demo_table)

# Generating data to insert into the table I created
row_tuples = [('g', 3, 9),
              ('v', 5, 7),
              ('f', 8, 7)]
              
# Iterating over each row in the list and inserting into table
for row in row_tuples: 
  insert_row = "INSERT INTO demo VALUES" + str(row)
  curs.execute(insert_row)         

# Committing Insert into demo values
conn.commit()  

curs = conn.cursor()

# Querying all data from demo table
curs.execute('SELECT * FROM demo')
curs.fetchall()

# Making lists of the questions and queries

questions = ['Q1: Count how many rows you have - it should be 3!',
             'Q2: How many rows are there where both `x` and `y` are at least 5?',
             'Q3: How many unique values of `y` are there (hint - `COUNT()` can accept a keyword `DISTINCT`)?']

queries = ["SELECT COUNT(*) FROM demo;",
           "SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;",
           "SELECT COUNT(DISTINCT y) FROM demo;"] 

# Iterating, executing, and printing the questions and results:
for i in range(len(questions)):
  print(questions[i])
  curs.execute(queries[i])
  print(curs.fetchall()[0][0])
  print('\n')        
