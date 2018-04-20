import statistics
from databaseModule import DB_connect
from crudController import CRUD
import random
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
        #out = self.InsertionSort(data)
        out = self.ThreeP_QuickSort(data)
        return out

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

    def ThreeP_QuickSort(self,data):
        
        
        def pivotFind(start,end):
            if (end-start) > 3:
                rand = random.sample(range(start,end),3)
            else:
                rand = random.sample(range(start,end),1)
            x= [data[a] for a in rand]
            median = statistics.median(x)
            pivot = data.index(median)
            return pivot
        
        def partitionFunc(left,right,pivot):
            newPivotIndex = left -1    
            for index in range(left,right):
                if data[index]<data[right]:#check if current val is less than pivot value
                    newPivotIndex=newPivotIndex+1
                    data[newPivotIndex], data[index] = data[index],data[newPivotIndex]
                    
            data[newPivotIndex+1],data[right] = data[right] , data[newPivotIndex+1]
            return newPivotIndex+1

        def quick(start,end):
            if start < end:
                pivot = pivotFind(start,end) 
                data[pivot],data[end]=data[end],data[pivot]
                p = partitionFunc(start,end,pivot)
                quick(start,p-1)
                quick(p+1,end)
        
        length = len(data)
        quick(0,length-1)
        return data