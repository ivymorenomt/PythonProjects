
import os

import array

def clearScreen():
    os.system('cls')

def dataStruct():
    clearScreen()
    print("Data Structures is selected")
    print("1. Arrays \n2. Strings \n3. Linked Lists \n4.Trees \n5. Graphs \n6. Tries")
    userinput = input("Enter your selection:")
    if(userinput == '1'):
        array.arraymain() 
        # TODO: call the class properly
    
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