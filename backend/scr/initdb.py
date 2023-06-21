import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('system.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.

# Creating table
table = """ CREATE TABLE TRADES (
    		ID INT PRIMARY KEY NOT NULL,
			tickerName VARCHAR(255) NOT NULL,
			type INT NOT NULL,
			enterPrice VARCHAR(25),
			exitPrice VARCHAR(25),
			isOpen VARCHAR(25)
		); """

# cursor_obj.execute(table)
statement = '''SELECT * FROM TRADES'''
  
cursor_obj.execute(statement)
  
print("All the data")
output = cursor_obj.fetchall()
di = {"trades": []}
for row in output:
  di["trades"].append(list(row))

print(di)
  

print("Table is Ready")

# Close the connection
connection_obj.close()
