import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="yay.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")

with open('courses.csv') as csvfile:
    courses_file = csv.DictReader(csvfile)
    for row in courses_file:
        c.execute("INSERT INTO courses VALUES(\'" + row["code"] + "\', " + row['mark'] + "," + row['id'] + ");")
	
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")
with open('peeps.csv') as csvfile:
    peeps_file = csv.DictReader(csvfile)
    for row in peeps_file:
        c.execute("INSERT INTO peeps VALUES(\'" + row["name"] + "\', " + row['age'] + "," + row['id'] + ");")

#command = ""          put SQL statement in this string
#c.execute(command)    run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database


