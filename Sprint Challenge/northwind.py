# Part 2

# Opening connection with northwind_small.sqlite3
import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Questions and Queries into lists

questions = [['Q1: What are the ten most expensive items (per unit price) in the database?',
        	 'Q2: What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)',
			 'Q3: (*Stretch*) How does the average age of employee at hire vary by city?']]

queries = ["SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;",
		   "SELECT ROUND(AVG(HireDate - BirthDate),1) AS Avg_Age FROM Employee;",
		   "SELECT CITY, AVG(HireDate - BirthDate) AS Avg_Age FROM Employee GROUP BY CITY;"]

# Iterating, executing, and printing the questions and results 
for i in range(len(questions)):
  print(questions[i])
  curs.execute(queries[i])
  results = curs.fetchall()
  if len(results) ==1:
    print(results)
  else: 
     for res in results:
       print(res)
  print('\n')
