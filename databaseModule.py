import sqlite3
from sqlite3 import Error

class DB_connect(object):
    def __init__(self, name):
        try:
            self.Link = sqlite3.connect(name)
            self.cursor = self.Link.cursor()
            print(sqlite3.version)
        except Error as err:
            print(err)   

    def executeDB(self,statement):
        try:
            self.cursor.execute(statement)
        except Error as err:
            print(err)
            
        
    def createTable(self):
        statement = '''
        CREATE TABLE IF NOT EXISTS PEOPLE
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        BIO TEXT,
        GENDER TEXT,
        LINK TEXT,
        ADDRESS TEXT,
        LONGITUDE REAL,
        LATITUDE REAL,
        IMAGE BLOB,
        PHONE INT,
        DOB TEXT
        );
        '''
        
        try:
            self.cursor.execute(statement)
            self.Link.commit()
        except Error as err:
            print(err)
      
        

    def closeDB(self):
        try:
            self.Link.commit()
            self.Link.close()
            print('Database Closed Successfully')
        except Error as err:
            print(err)
                

if __name__== '__main__':

    database = DB_connect('mysql.db')
    database.createTable()
    database.closeDB()