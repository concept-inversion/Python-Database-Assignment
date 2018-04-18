import sqlite3
from sqlite3 import Error


class DB_connect(object):
    def __init__(self, name):
        try:
            self.Link = sqlite3.connect(name)
            self.cursor = self.Link.cursor()
            self.createTable()
        except Error as err:
            print(err)   

    def executeDB(self,statement):
        try:
            data = self.cursor.execute(statement)
            self.Link.commit()
            return data
        except Error as err:
            print(err)
        
            
        
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
            data= self.cursor.execute(statement)
            self.Link.commit()
            print("table creataed")
        except Error as err:
            print(err)
      
    def closeDB(self):
        try:
            self.Link.commit()
            self.Link.close()
            print('Database Closed Successfully')
        except Error as err:
            print(err)
