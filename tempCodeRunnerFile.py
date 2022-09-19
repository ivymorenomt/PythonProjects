
def dataStruct():
    print("Data Structures is selected")
    
def algo():
    print("Algorithms is selected")

def main():
    print("1. Data Structures")
    print("2. Algorithms")
    userinput = input("Enter your choice: ")
    if(userinput == '1'):
        dataStruct()
    else:
        algo()




if __name__ == "__main__":
    main()