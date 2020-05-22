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

