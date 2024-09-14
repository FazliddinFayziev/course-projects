from DoubleLinkNode import DoubleLinkNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtRear(self, item):
        myNode = DoubleLinkNode(item)
        if self.head is None and self.tail is None:
            self.head = myNode
            self.tail = myNode
        else:
            self.tail.setNext(myNode)
            myNode.setPrev(self.tail)
            self.tail = myNode

    def insertNodeAtFront(self, item):
        myNode = DoubleLinkNode(item)
        if self.head is None and self.tail is None:
            self.head = myNode
            self.tail = myNode
        else:
            myNode.setNext(self.head) 
            self.head.setPrev(myNode) 
            self.head = myNode

    def traverseLinkedList(self):
        length = 140
        print("+" * length)
        print("Exploring the Doubly Linked List: ")
        print("+" * length)
        temp = self.head
        while True:
            if temp is None:
                break
            else:
                print(temp, end='')
                temp = temp.getNext()
        print('\n' + "+" * length)
