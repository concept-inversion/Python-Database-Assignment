from databaseModule import DB_connect
import json
#generate query from user input
class CRUD():
    def __init__(self, *args, **kwargs):
        # use static methods in future
        self.db = DB_connect('mysql.db') 
    
    def Create(self,each):
        columns = ', '.join(each.keys())
        placeholders = ':'+', :'.join(each.keys())
        statement = 'INSERT INTO PEOPLE (%s) VALUES (%s)'% (columns, placeholders,)
        data=self.db.Link.execute(statement,each)   
        return data

    def Update(self,param):
        statement= 'UPDATE PEOPLE SET %s'% (param)
        print(statement)
        data=self.db.executeDB(statement)
        return data 

    def Read(self, param):
        statement= ' SELECT * FROM PEOPLE WHERE (%s)'% (param)
        data=self.db.executeDB(statement)
        return data.fetchall()
    
    def View(self):
        statement= ' SELECT * FROM PEOPLE ' 
        data=self.db.executeDB(statement)
        return data.fetchall()

    def Delete(self, param):
        statement= 'DELETE FROM PEOPLE WHERE (%s)'%(param)
        data=self.db.executeDB(statement)
        return data

    def JsonLoader(self,data):
        raw=json.load(open(data))
        for each in raw:
            columns = ', '.join(each.keys())
            placeholders = ':'+', :'.join(each.keys())
            statement = 'INSERT INTO PEOPLE (%s) VALUES (%s)'% (columns, placeholders,)
            data=self.db.Link.execute(statement,each)
        return data
    
    def close(self):
        self.db.closeDB()


