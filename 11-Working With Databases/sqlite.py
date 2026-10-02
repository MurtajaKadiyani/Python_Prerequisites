import sqlite3

## Connect to an SQLite database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

## Create a Table
cursor.execute(
    """ Create Table IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
    ) """
)

## Commit the changes
connection.commit()

cursor.execute('''
select * from employees
''')

## Insert the data in sqlite table
cursor.execute('''
Insert Into employees(name,age,department)
               values('Murtaja',36,'Agrntic AI Head')
''')

cursor.execute('''
INSERT INTO employees (name, age, department)
VALUES ('Bob', 25, 'Engineering')
''')

cursor.execute('''
INSERT INTO employees (name, age, department)
VALUES ('Charlie', 35, 'Finance')
''')
## commi the changes
connection.commit()

## Query the data from the table
cursor.execute('Select * from employees')
rows = cursor.fetchall()

## print the queried data
for row in rows:
    print(row)

## Update the data in the table
cursor.execute('''
UPDATE employees
SET age = 35
WHERE name = 'Murtaja' 
''')

connection.commit()

## Query the data from the table
cursor.execute('Select * from employees')
rows=cursor.fetchall()

## print the queried data

for row in rows:
    print(row)

## Delete the data from the table
cursor.execute('''
DELETE FROM employees
WHERE name = 'Bob'
''')
connection.commit()

## Query the data from the table
cursor.execute('Select * from employees')
rows=cursor.fetchall()

## print the queried data

for row in rows:
    print(row)

## Working Wwith Sales Data
# Connect to an SQLite database
connection = sqlite3.connect('sales.db')
cursor = connection.cursor()

# Create a table for sales data
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT
)
''')

# Insert data into the sales table
sales_data = [
    ('2023-01-01', 'Product1', 100, 'North'),
    ('2023-01-02', 'Product2', 200, 'South'),
    ('2023-01-03', 'Product1', 150, 'East'),
    ('2023-01-04', 'Product3', 250, 'West'),
    ('2023-01-05', 'Product2', 300, 'North')
]

cursor.executemany('''
INSERT INTO sales(date, product, sales, region)
VALUES (?, ?, ?, ?)
''', sales_data)

connection.commit()

# Query data from the sales table
cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)

## close the connection
connection.close()

# Query data from the sales table
cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()    

# Print the queried data
for row in rows:
    print(row)

