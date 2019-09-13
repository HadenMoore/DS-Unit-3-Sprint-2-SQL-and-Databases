# Part 2: The Northwind Database

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

# Part 3: Sailing the Northwind Seas

questions = ['Question1: What are the ten most expensive items (per unit price) in the database and their suppliers?',
			 'Question2: What is the largest category (by number of unique products in it)?',
			 "Question3: (Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories."]

queries = ["SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName AS Supplier FROM Product, Supplier WHERE Product.SupplierID = Supplier.ID ORDER BY UnitPrice DESC LIMIT 10;",
		   "SELECT Category.CategoryName, COUNT(*) FROM Product, Category WHERE Product.CategoryID = Category.ID GROUP BY Product.CategoryID ORDER BY COUNT(*) DESC LIMIT 1;",
		   "SELECT Employee.FirstName, Employee.LastName, COUNT(*) FROM Employee, EmployeeTerritory WHERE EmployeeTerritory.EmployeeID = Employee.ID GROUP BY Employee.ID ORDER BY COUNT(*) DESC LIMIT 1;"]

# Iterating, executing queries, and printing the questions and results. 
for i in range(len(questions)):
	print(questions[i])
	curs.execute(queries[i])
	results = curs.fetchall()
	if len(results) == 1:
		print(results)
	else:
		for res in results:
			print(res)
	print('\n')

# Part 4: Questions (and your Answers)

questions = ['Question1: In the Northwind database, what is the type of relationship between the `Employee` & `Territory` tables?',
			 '''Question2: What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where 
it is not appropriate?''',
			 'Question3: What is "NewSQL", and what is it trying to achieve?']

answers = ['Answer1: In the Employee table, there are 9 employees. The Territory Table has 53 Territories. Meaning there is a relationship of One-to-Many.',
           '''Answer2: You would use MongoDB when you need an exteremly simple, easy to install, high performance, high availability and automatic scaling document store model. 
           You would not want to use MongoDB if you are working with Highly Transactional Systems or when the data model is designed up front. Or when you have tightly coupled systems.''',
           '''Answer3: NewSQL is a class of Relational Database Management systems that seek to provide the scalability of NoSQL Systems for Online Transaction Processing (OLTP) workloads while maintaining the ACID guarantees of a Traditional Database System.''']
           
# Iterating, executing queries, and printing the questions and results.           
for i in range(len(questions)):
  print(questions[i])
  print(answers[i])
  print('\n')