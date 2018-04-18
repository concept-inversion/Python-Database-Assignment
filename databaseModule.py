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
        self.cursor.execute(statement)
    
    def createTable(self):
        statement = '''
        CREATE TABLE IF NOT EXISTS PEOPLE
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL
        )
        '''
        self.cursor.execute(statement)
        
    def closeDB(self):
        self.Link.commit()
        self.Link.close()        

if __name__== '__main__':

    database = DB_connect('mysql.db')
    database.createTable()
    database.closeDB()