from DoublyLinkedList import DoublyLinkedList

if __name__ == '__main__':
    myList = DoublyLinkedList()

    myList.insertNodeAtRear('Exercise / Yoga')
    myList.insertNodeAtRear('Meditate')
    myList.insertNodeAtRear('Read a Book')
    myList.insertNodeAtRear('Check Emails')
    myList.insertNodeAtRear('Check News')
    myList.insertNodeAtRear('Take a Shower')

    myList.traverseLinkedList()

    myList.insertNodeAtFront('Check Mobile Apps')

    myList.traverseLinkedList()

    print(f"Head: {myList.head.getData()}")
    print(f"Tail: {myList.tail.getData()}")
