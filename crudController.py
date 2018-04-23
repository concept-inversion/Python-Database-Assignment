import json
from databaseModule import DB_connect
from postgreModule import Postgre_db
#generate query from user input
class CRUD():
    '''
    Class to implement CRUD functionality:
    1. Create(self, each)
        Inserts data in the database.
        each -> Python dict input
    2. Update(self,param)
        Updates  columns 
    3. Read(self, param)
    
    4. Delete(self,param)
    
    5. View(self, param)

    6. Jsonloader(self, data)
    
    '''
    
    def __init__(self, *args, **kwargs):
        # use without self
        self.db = DB_connect('mysql.db') 
        
    def Create(self,each):
        #columns = ', '.join(each.keys())
        #placeholders = ':'+', :'.join(each.keys())
        statement = ("INSERT INTO People ( Bio, Name, Dob, Gender, Email, Longitude, Latitude, Phone, Link, Image,Address )"
                  " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data=self.db.executeDB(statement,(each['Bio'],each['Name'],each['Dob'],each['Gender'],each['Email'],each['Longitude'],each['Latitude'],each['Phone'],each['Link'],each['Image'],each['Address']))   
        print("Data Inserted")
        return data

    def Update(self,param):
        statement= 'UPDATE PEOPLE SET %s'% (param)
        print(statement)
        data=self.db.executeDB(statement,param)
        print("Data Updated")
        return data 

    def Read(self, param):
        statement= ' SELECT * FROM PEOPLE WHERE (%s)'% (param)
        data=self.db.executeDB(statement,param)
        if data:
            return data.fetchall()
    
    def View(self,param=[]):
        statement= ' SELECT * FROM PEOPLE ' 
        data=self.db.executeDB(statement,param)
        if data:
            return data

    def Delete(self, param):
        statement= 'DELETE FROM PEOPLE WHERE (%s)'%(param)
        data=self.db.executeDB(statement,param)
        return data

    def JsonLoader(self,data):
        raw=json.load(open(data))
        for each in raw:
            #columns = ', '.join(each.keys())
            #placeholders = ':'+', :'.join(each.keys())
            statement = ("INSERT INTO People ( Bio, Name, Dob, Gender, Email, Longitude, Latitude, Phone, Link, Image,Address )"
                  " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            data=self.db.executeDB(statement,(each['Bio'],each['Name'],each['Dob'],each['Gender'],each['Email'],each['Longitude'],each['Latitude'],each['Phone'],each['Link'],each['Image'],each['Address']))
        return data
    
    def close(self):
        self.db.closeDB()


