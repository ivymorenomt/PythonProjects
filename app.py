
import os

def clearScreen():
    os.system('cls')

def arrays():
    print('You selected Arrays. What do you want to do?')
    userinput = input('C-Create \nI-Insert \nS-Search \nD-Delete \nOR \nM-Go Back to MAIN : \n')
    if(userinput == 'C'):
        print("Create an array")
    elif(userinput == 'I'):
        print("Insert a value in an array")
    elif(userinput == 'S'):
        print("Search a value in array")
    elif(userinput == 'D'):
        print("Delete a value in array")
    else:
        clearScreen()
        main()
1
def dataStruct():
    clearScreen()
    print("Data Structures is selected")
    print("1. Arrays \n2. Strings \n3. Linked Lists \n4.Trees \n5. Graphs \n6. Tries")
    userinput = input("Enter your selection:")
    if(userinput == '1'):
        arrays()
    
def algo():
    print("Algorithms is selected")
    userinput = input("Enter your choice:")
    print("Algorithms is selected")

def main():
    print("1. Data Structures \n2. Algorithms \neXit")
    userinput = input("Enter your choice: ")
    if(userinput == '1'):
        dataStruct()        
    elif(userinput == '2'):
        algo()
    else:
        os.system('exit')




if __name__ == "__main__":
    main()