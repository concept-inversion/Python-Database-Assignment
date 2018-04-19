import json
from databaseModule import DB_connect
from crudController import CRUD


class Program():
    def __init__(self, *args, **kwargs):
        self.crud = CRUD()

    def Delete(self):
        # [Column name] [operation][cond]
        cond = input("Enter the query starting from column name: ")
        self.crud.Delete(cond)

    def Insert(self):
        format = {
        "Bio": "",
        "Name": "",
        "Dob": "",
        "Gender": "",
        "Image": "",
        "Longitude": "",
        "Phone": "",
        "Link": "",
        "Address": "",
        "Latitude": "",
        "Email": ""
        }
        for key in format:
            format[key]= input("Enter the  "+key )
        self.crud.Create(format)

    def Update(self,args):
        # [Column name] [operation][cond]
        cond = input("Enter the query starting from column name: ")
        self.crud.Read(cond)

    def Select(self):
        # [Column name] [operation][cond]
        cond = input("Enter the query starting from column name: ")
        output = self.crud.Read(cond)
        #print("output from database : " + output)
        return output
    
    def upload_json(self,data):
        self.crud.JsonLoader(data)
        

if __name__== '__main__':
    new = Program()
#new.Insert()
    data=new.Select()
    for each in data:
        print (each)
    '''
    new.upload_json('raw_data.json')
    data1=new.Update("Email = 'kale' WHERE Image= 'hans.io'")
    data = new.Select("Email= 'kale'")
    '''

