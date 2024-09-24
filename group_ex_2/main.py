from linkedList import LinkedList

# GROUP ALFA:
# MASHHUR
# FAZLIDDIN

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
        print("| 1. Add Element                      |")
        print("| 2. Remove Element                   |")
        print("| 3. Display List                     |")
        print("| 4. Quit                             |")
        print("--------------------------------------")

        try:
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
                print("|  Invalid Option!            |")
                print("|  Please choose between 1-4. |")
                print("-------------------------------")
        
        except ValueError:
            print("-------------------------------")
            print("|  Invalid input!             |")
            print("|  Please enter a number.     |")
            print("-------------------------------")

main()
