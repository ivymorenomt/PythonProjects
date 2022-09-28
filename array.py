from array import Array
from app import main

class Array:

    def __init__(self,lst=[]):
        self.value = lst

    def createarr(self):
        str = input('Enter a string to create an array: \n')
        for letter in str:
            self.value.append(letter)
        for i,j in enumerate(self.value):
            print(i,j)
        return self.value
    
    def viewArr(self):
        return f'the current list is {self.value}'

    def insertArr(self):
        inp = input("Enter a value to insert: ")
        return self.value.append(inp)

    def searchArr(self):
        # Linear Search - TODO: For more search related stuff, create different searches in algorithms class
        #The search below is Time - O(n), Space - O(n)
        inp = input("Enter a value to search: ")
        for ind, elem in enumerate(self.value):
            if elem == inp:
                return f'The value {inp} is found in {ind}'
    
    def deleteArr(self, target):
        for ind, elem in enumerate(self.value):
            if elem == target:
                self.value.pop(ind)
                return f'The element {elem} is deleted from {ind}. Current array is now {self.value}'
            
    def arraymain():
        list1 = []
        arr = array(list1)
        print('You selected Arrays. What do you want to do?')
        userinput = input('C-Create \nV-View \nI-Insert \nS-Search \nD-Delete \nOR \nM-Go Back to MAIN : \n')
        if(userinput == 'C'):
            print("Create an array")
            arr.createarr()
        elif(userinput=='V'):
            print('View the array')
            arr.viewArr()
        elif(userinput == 'I'):
            print("Insert a value in an array")
            arr.insertArr()
        elif(userinput == 'S'):
            print("Search a value in array")
        elif(userinput == 'D'):
            print("Delete a value in array")
        else:
            main()

Array.arraymain()