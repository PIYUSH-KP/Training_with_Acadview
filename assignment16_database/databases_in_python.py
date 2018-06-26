import mysql.connector as pkp
import sqlite3

"""Q.1- Create a database. Create the following tables:
1. Book
2. Titles
3. Publishers
4. Zipcodes
5. AuthorsTitles
6. Authors
Refer to the diagram below"""

try:
    con = pkp.connect(host='localhost', database='piyushkpdb', user='root', password='piyushkp123')
cursor = con.cursor()
query1 = 'Create table Authors(AuthorID int primary key,FirstName varchar(25),MiddleName varchar(25),LastName varchar(25))'
cursor.execute(query1)
query2 = 'Create table ZipCodes(ZipCodeID int primary key,City varchar(25),State varchar(20),ZipCode int)'
cursor.execute(query2)
query3 = 'Create table Publishers(PublisherID int primary key,Name varchar(25),StreetAddress varchar(50),SuiteNumber int,ZipCodeID int,foreign key(ZipCodeID) references ZipCode(ZipCodeID))'
cursor.execute(query3)
query4 = 'Create table Titles(TitleId int primary key,Title varchar(35),ISBN int,PublisherID int,Publication_Year int,foreign key(PublisherID) references Publishers(PublisherID))'
cursor.execute(query4)
query5 = 'Create table Books(BookId int primary key,TitleId int,Location varchar(25),Genre varchar(10),foreign key(TitleId) references Titles(TitleId))'
cursor.execute(query5)
query6 = 'Create table AuthorsTitles(AuthorTitleID int primary key,AuthorID int ,TitleId int,foreign key(AuthorID) references Authors(AuthorID),foreign key(TitleId) references Titles(TitleId))'
cursor.execute(query6)
print('Table is Created')
except pkp.DatabaseError as e:
if con:
    con.rollback()
print('Something is worong!!!! ', e)
finally:
if cursor:
    cursor.close()
if con:
    con.close()


print("__"*60)
# Q.2- Insert values in the tables.
conn = sqlite3.connect("piyushkpdb.db")
cur = conn.cursor()
a = 'insert into AuthorsTitles values("AT1","AI1",100);'
cur.execute(a)
b = 'insert into Authors values("AI1","PIYUSH","KUMAR","PANDEY");'
cur.execute(b)
c = 'insert into Titles values(101,"Bang Bang","ISBN1",2000);'
cur.execute(c)
c = 'insert into Titles values(102,123466789012,"ISBN2",2001);'
cur.execute(c)
d = 'insert into Book values(1,BT1,"WINTERFELL","ENTERTAIER");'
cur.execute(d)
d = 'insert into Book values(2,BT2,"BAKER STREET","DETECTIVE");'
cur.execute(d)
d = 'insert into Book values(3,BT3,"INDIA","COMIC");'
cur.execute(d)
e = 'insert into Publishers values("ABC1","Ayush Kumar","patna",23,800020);'
cur.execute(e)
e = 'insert into Publishers values("ABC2","Mukul Pandey","Phagwara",12,144411);'
cur.execute(e)
f = 'insert into ZipCodes values(144411,"Jalandhar","Punjab",144411);'
cur.execute(f)
f = 'insert into ZipCodes values(96600,"Ara","Delhi",800012);'
cur.execute(f)
conn.commit()
print("VALUES INSERTED ")


print("__"*60)

# Q.3- Update any values in any of the tables. Print the original and updated values.
conn = sqlite3.connect("piyushkpdb.db")
cur = conn.cursor()
a = 'update Book set location = "ARGENTINA" where bookId = 3;'
cur.execute(a)
a = 'update ZipCodes set State = "Bihar" where ZipCodeId="800012"'
cur.execute(a)
a = "select * from Authors;"
cur.execute(a)
for data in cur.fetchall():
    print(data)

