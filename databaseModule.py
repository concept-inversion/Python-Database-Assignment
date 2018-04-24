import sqlite3
from sqlite3 import Error
import json

class DB_connect(object):
    '''
    Implementation of SQLite Python module
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
    
    def __init__(self, name):
        try:
            self.Link = sqlite3.connect(name)
            self.cursor = self.Link.cursor()
            self.createTable()
        except Error as err:
            print(err)   
            
    def executeDB(self,statement,key):
        try:
            self.cursor.execute(statement,key)
            self.Link.commit()
            return (self.cursor.fetchall())

        except Error as err:
            print(err)
            self.Link.rollback()



    def createTable(self):
        statement = '''
 CREATE TABLE IF NOT EXISTS PEOPLE
        (Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Bio TEXT,
        Gender VARCHAR(12),
        Link TEXT,
        Address TEXT,
        Longitude REAL,
        Latitude REAL,
        Image BLOB,
        Phone INT,
        Dob DATE

        );
'''        
        try:
            self.cursor.execute(statement)
            self.Link.commit()
            print("table creataed")
        except Error as err:
            print(err)
    
    def JsonLoader(self,data):
        raw=json.load(open(data))
        for each in raw:
            columns = ', '.join(each.keys())
            placeholders = ':'+', :'.join(each.keys())
            statement = 'INSERT INTO PEOPLE (%s) VALUES (%s)'% (columns, placeholders,)
            data=self.cursor.execute(statement,each)
        return data

    def Create(self,each):
        columns = ', '.join(each.keys())
        placeholders = ':'+', :'.join(each.keys())
        statement = 'INSERT INTO PEOPLE (%s) VALUES (%s)'% (columns, placeholders,)
        data=self.Link.execute(statement,each)   
        return data

    def closeDB(self):
        try:
            self.Link.commit()
            self.Link.close()
            print('Database Closed Successfully')
        except Error as err:
            print(err)
