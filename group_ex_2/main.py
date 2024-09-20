from linkedList import LinkedList

def main():
    quit = True
    elements = LinkedList()
    print("--------------------------------------")
    print("|         Welcome to program!         |")
    print("--------------------------------------")
    while quit:
        print("--------------------------------------")
        print("|         Choose Number:              |")
        print("--------------------------------------")
        print("--------------------------------------")
        print("| 1. Add Element                      |")
        print("| 2. Romeve Element                   |")
        print("| 3. Display List                     |")
        print("| 4. Quit                             |")
        print("--------------------------------------")

        number = int(input("Choose number: "))

        if number == 1:
            print("-----------------------------------")
            print("|  Add Element (Any Type of Data)  |")
            print("-----------------------------------")
            data = input("Give your data: ")
            elements.appendEnd(data)
            print("------------------------")
            print("|  Element is Added!   |")
            print("------------------------")

        elif number == 2:
            elements.removeFront()
            print("-------------------------")
            print("|  Element is Removed!   |")
            print("-------------------------")

        elif number == 3:
            print("-------------------------")
            print("|  All Elements:        |")
            print("-------------------------")
            print(elements.getList())

        elif number == 4:
            print("-------------------------------------------")
            print("|  Thank you for using our program!       |")
            print("-------------------------------------------")
            quit = False

        else: 
            print("-------------------------------")
            print("|  Something went wrong!      |")
            print("-------------------------------")
            print("----------------------------------")
            print("|  Please follow the rules!      |")
            print("----------------------------------")

main()




            


