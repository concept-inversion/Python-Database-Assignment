import json
from databaseModule import DB_connect
from crudController import CRUD

'''
class Program():
    def Delete():

    def Insert():
    
    def Update():
    
    def Select():
    
    def upload_json():
'''

#if __name__== '__main__'    
new= CRUD()
#new.JsonLoader('raw_data.json')
data1=new.Update("Email = 'kale' WHERE Image= 'hans.io'")
data = new.Read("Email= 'kale'")

for each in data:
    print(each)

