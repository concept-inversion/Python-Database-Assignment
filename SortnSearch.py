from databaseModule import DB_connect
from crudController import CRUD

class sortSearch():
    def __init__(self, *args, **kwargs):
        self.crud= CRUD()

    def Search(self):
        #Search in every column
        pass


    def Sort(self,*args):
        data = self.crud.View()
        print("suce")
        data = [x[1] for x in data]
        self.InsertionSort(data)

    def InsertionSort(self,data):
        length = len(data)
        for i in range(length):
            Value = data[i]
            holePos = i
            while ((holePos >0) and (data[holePos-1] > Value)):
                data[holePos] = data[holePos-1]
                holePos= holePos-1        
            data[holePos]=Value
        print(data)
        return data

    def QuickSort(self):
        pass

