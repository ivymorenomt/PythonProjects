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
        pass

    def searchArr(self,s):
        
                return f'The value {s} is found'
            #TODO: Fix search;maybe list comprehension?

    # def arraymain():
    #     print('You selected Arrays. What do you want to do?')
    #     userinput = input('C-Create \nV-View \nI-Insert \nS-Search \nD-Delete \nOR \nM-Go Back to MAIN : \n')
    #     if(userinput == 'C'):
    #         print("Create an array")
    #         array.createarr()
    #     elif(userinput=='V'):
    #         print('View the array')
    #     elif(userinput == 'I'):
    #         print("Insert a value in an array")
    #     elif(userinput == 'S'):
    #         print("Search a value in array")
    #     elif(userinput == 'D'):
    #         print("Delete a value in array")
    #     else:
    #         main()

arr = Array()
arr.createarr()
# print(arr.viewArr())
print(arr.searchArr(2))