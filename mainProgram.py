import json
from databaseModule import DB_connect
from crudController import CRUD
from SortnSearch import sortSearch
from texttable import Texttable
class Program():
    def __init__(self, *args, **kwargs):
        self.crud = CRUD()

    def Delete(self):
        # [Column name] [operation][cond]
        cond = input("[Delete]Enter the query starting from column name: ")
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
            format[key]= input("Enter the "+ key )
        self.crud.Create(format)

    def Update(self):
        # [Column name] [operation][cond]
        cond = input("[Update]Enter the query starting from column name: ")
        self.crud.Read(cond)
    
    def Viewtable(self):
        output=self.crud.View()
        self.View(output)
    
    def View(self,data):
        
        Ttable = Texttable(150)
        Header = ["Id",    
        "Bio",
        "Name",
        "Dob",
        "Gender",
        "Image",
        "Longitude",
        "Phone",
        "Link",
        "Address",
        "Latitude",
        "Email"
        ]
        
        if data:
            Ttable.add_rows(data)
            Ttable.set_deco(Texttable.BORDER | Texttable.HEADER | Texttable.VLINES | Texttable.HLINES )
            Ttable.header(Header)
            print(Ttable.draw())
        else:
            print("No Data to show")

    def Select(self):
        # [Column name] [operation][cond]
        cond = input("[Select]Enter the query starting from column name: ")
        output = self.crud.Read(cond)
        if output:
            for each in output:
                print (each)
        else:
            print("no data")
        
    
    def upload_json(self):
        data = input("Enter json file: ")
        self.crud.JsonLoader(data)
    
    def sort(self):
        sor = sortSearch()
        out= sor.Sort()
        self.View(out)

    def close(self):
        self.crud.close()
        

if __name__== '__main__':
    new = Program()
    options = [None,new.Insert,new.Select,new.Update,new.Delete,new.upload_json,new.Viewtable,new.sort]
    while True:
        action = int(input(
            '''
            Press 1 to Insert
            Press 2 to Select
            Press 3 to Update
            Press 4 to Delete
            Press 5 to Load JSON
            Press 6 to View all rows
            Press 7 to Sort by name
            Press 0 to exit
            
            '''
        ))
        if(action==0):
            new.close()
            break
        else:
            options[action]()
        


