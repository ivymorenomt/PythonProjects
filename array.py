from app import main

class array:

    def __init__(self, val=[]):
        self.value = val

    def createarr():
        lst = []
        str = input('Enter a string to create an array: \n')
        for letter in str:
            lst.append(letter)
        for i,j in enumerate(lst):
            print(i,j)
            
    def arraymain():
        print('You selected Arrays. What do you want to do?')
        userinput = input('C-Create \nV-View \nI-Insert \nS-Search \nD-Delete \nOR \n\nM-Go Back to MAIN : \n')
        if(userinput == 'C'):
            print("Create an array")
            array.createarr()
        elif(userinput=='V'):
            print('View the array')
        elif(userinput == 'I'):
            print("Insert a value in an array")
        elif(userinput == 'S'):
            print("Search a value in array")
        elif(userinput == 'D'):
            print("Delete a value in array")
        else:
            main()
array.arraymain()