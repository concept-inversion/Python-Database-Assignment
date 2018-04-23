import psycopg2
from psycopg2 import Error
class Postgre_db:
    '''
    Implementation of PostgreSQL module
    Functions:
    1. closeDB(self)
        [Connection].closeDB() : Commit the database and closes the connection with the database. 

    2. executeDB(self,statement,key)
        [Conncetion].executeDB(self, statement, key) : Executes a SQL Query in the Database
            statement -> Query
            key -> Optional parameters
    
    3. createTable()
        Creates a Table with a fixed schema 
    '''
    def __init__(self, *args, **kwargs):        
        try:
            self.Link = psycopg2.connect("dbname=postgre user=concept password=concept host=localhost port=5432 ")
            self.cursor = self.Link.cursor()
            self.createTable()
            print("connection done")
        except Error as err:
            print(err)
    
    def closeDB(self):
        try:
            self.Link.commit()
            self.Link.close()
            print('Database Closed Successfully')
        except Error as err:
            print(err)

    def executeDB(self,statement,key):
        try:
            self.cursor.execute(statement,key)
            self.Link.commit()
            print("Execution Completed Successful")
            return (self.cursor.fetchall())

        except Error as err:
            print(err)
    

    def createTable(self):
        statement = (
         '''
        CREATE TABLE IF NOT EXISTS PEOPLE
        (Id SERIAL PRIMARY KEY,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Bio TEXT,
        Gender VARCHAR(12),
        Link TEXT,
        Address TEXT,
        Longitude REAL,
        Latitude REAL,
        Image TEXT,
        Phone INT,
        Dob DATE
        );
        '''    )    
        try:
            self.cursor.execute(statement)
            self.Link.commit()
            print("Table Created")
        except Error as err:
            print(err)