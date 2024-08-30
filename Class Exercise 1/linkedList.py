
# ============================================================>
# ========================= NODE =============================>
# ============================================================>

class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# ============================================================>
# =================== LINKED LIST ============================>
# ============================================================>

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def appendFront(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head  
            self.head.prev = node  
            self.head = node
    
    def appendEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail  
            self.tail.next = node
            self.tail = node
    
    def removeFront(self):
        if self.head == None:
            return None
        else:
            removedNode = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return removedNode
    
    def removeEnd(self):
        if self.head == None:
            return None
        else:
            removedNode = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return removedNode
        
    def getList(self):
        lists = []
        if self.head == None:
            return []
        else:
            current = self.head
            while current != None:
                lists.append(current.data)
                current = current.next
            return lists
        
# ============================================================>
# ================== MAIN FUNCTION ===========================>
# ============================================================>

def main():

    # ================== Welcome Page =============================>

    print("Welcome to linkedList!")
    print("Here You can Add elements in LinkedList")
    print("Or Remove Any Element From LinkedList")
    storage = LinkedList()
    start = True

    while start:

        # =============== INITIAL CHOICE ===========================>

        print("\nCurrent LinkedList: ", storage.getList())
        print("Choose an option:")
        print("1. Add a value")
        print("2. Remove a value")
        print("3. Stop the process")
        userInput = input("Enter your choice (1, 2, or 3): ")

        # ================== CHOICE FOR 1 =========================>

        if userInput == "1":
            data = input("Enter the value to add: ")
            print("Where would you like to add your value?")
            print('To Front -> A')
            print('To End -> B')
            position = input("Enter A or B: ").upper()

            if position == "A":
                storage.appendFront(data)
                print(f"Value '{data}' added to the front of the list.")
            elif position == "B":
                storage.appendEnd(data)
                print(f"Value '{data}' added to the end of the list.")
            else:
                print("Invalid choice. Please enter A or B.")

        # ================== CHOICE FOR 2 =========================>

        elif userInput == "2":
            print("From where would you like to remove a value?")
            print('From Front -> A')
            print('From End -> B')
            position = input("Enter A or B: ").upper()

            if position == "A":
                removedNode = storage.removeFront()
                if removedNode:
                    print(f"Value '{removedNode.data}' removed from the front of the list.")
                else:
                    print("The list is empty. Nothing to remove from the front.")
            elif position == "B":
                removedNode = storage.removeEnd()
                if removedNode:
                    print(f"Value '{removedNode.data}' removed from the end of the list.")
                else:
                    print("The list is empty. Nothing to remove from the end.")
            else:
                print("Invalid choice. Please enter A or B.")
            
        # ================== CHOICE FOR 3 =========================>

        elif userInput == "3":
            print("Thank you for using our LinkedList. Here is your final list:")
            print(storage.getList())
            start = False

        # ================== OUT OF CHOICE ========================>

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
