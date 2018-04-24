import statistics
import random
import threading
from databaseModule import DB_connect
from crudController import CRUD


class sortSearch():
    def __init__(self, crud):
        self.crud= crud

    def Search(self):
        #Search in every column
        data= self.crud.View()
        key = (input('''
                        Press and Enter 1 to start search from Numbers[INT,FLOAT,REAL etc]
                        Press and Enter 2 to start search from Text[VARCHAR,TEXT,WORDS,SENTENCES etc]
                        Press and Enter any other keys to exit
                        
                        P.S : It will search all columns eventually.
                                                '''))

        if key == '1':
            order= [0,7,8,10,11,1,2,4,5,6,9,3]
        elif key == '2':
            order= [1,2,4,5,6,9,3,0,7,8,10,11]
        else:
            exit
        search = input("Enter the variable to search: ")
        result= []
        for o in order:
            for i in range(len(data)-1):
                value = str(data[i][o])
                if search == (value):
                    result.append(data[i])
        return result    




    def Sort(self,*args):
        data = self.crud.View()
        key = (input('''
                        Press and Enter 1 for Insertion sort
                        Press and Enter 2 for Quick Sort
                        Press and Enter any other keys to exit
                        '''))
        
        if key == '1':
            out = self.InsertionSort(data)
            return out
        elif key == '2':
            out = self.ThreeP_QuickSort(data)
            return out
        else: 
            exit
        

    def InsertionSort(self,data):
        length = len(data)
        for i in range(length):
            Value = data[i]
            holePos = i
            while ((holePos >0) and (data[holePos-1][1] > Value[1])):
                data[holePos] = data[holePos-1]
                holePos= holePos-1        
            data[holePos]=Value
        
        return data

    def ThreeP_QuickSort(self,data):
        def pivotFind(start,end):
            if (end-start) > 3:
                rand = random.sample(range(start,end),3)
            else:
                rand = random.sample(range(start,end),1)
            x= [data[a] for a in rand]
            median = statistics.median(x)
            pivot =next((i for i,t in enumerate(data) if t[1]==median),-1)
            return pivot
        
        def partitionFunc(left,right,pivot):
            newPivotIndex = left -1    
            for index in range(left,right):
                if data[index][1]<data[right][1]:#check if current val is less than pivot value
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