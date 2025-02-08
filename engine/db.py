import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# install SQLite package to view database in visual form 

#create a table sys_command

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

#insert into table

query = "INSERT INTO sys_command VALUES (null,'vm ware','C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe')"
cursor.execute(query)
con.commit()

#create a table web_command
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)

#insert into table

#query = "INSERT INTO web_command VALUES (null,'stock market today','https://www.moneycontrol.com/stocksmarketsindia/#google_vignette')"
#cursor.execute(query)
#con.commit()

#testing module
#app_name="one note"
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results) #show path with brackets
#print(results[0]) # remove one bracket from path
#print(results[0][0]) #removes two bracket from path






