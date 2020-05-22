#Creating a database engine

from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

#What are the tables in the database?

from sqlalchemy  import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')
table_names = engine.table_names()
print(table_names)

#The Hello World of SQL Queries!

from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Chinook.sqlite')
con = engine.connect()
rs = con.execute('select * from Album')
df = pd.DataFrame(rs.fetchall())
con.close()
print(df.head())

#Customizing the Hello World of SQL Queries

with engine.connect() as con:
    rs = con.execute('select LastName,Title from Employee')
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys()

#Filtering your database records using SQL's WHERE

engine = create_engine('sqlite:///Chinook.sqlite')
with engine.connect() as con:
    rs = con.execute('select * from Employee where EmployeeId >=6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df.head())

#Ordering your SQL records with ORDER BY

engine = create_engine('sqlite:///Chinook.sqlite')
with engine.connect() as con:
    rs = con.execute('select * FROM Employee order by BirthDate')
    df = pd.DataFrame(rs.fetchall())
    df.columns=rs.keys()
print(df.head())

#Pandas and The Hello World of SQL Queries!

engine = create_engine('sqlite:///Chinook.sqlite')
df = pd.read_sql_query('select * from Album', engine)

#Pandas for more complex querying

engine = create_engine('sqlite:///Chinook.sqlite')
df = pd.read_sql_query('select * FROM employee where EmployeeId>=6 order by BirthDate',engine)

#The power of SQL lies in relationships between tables: INNER JOIN

with engine.connect() as con:
    rs = con.execute('select Title,Name from Album innner join Artist using(ArtistID)')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df.head())

#Filtering your INNER JOIN

df = pd.read_sql_query('select * from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId where Milliseconds < 250000',engine)
