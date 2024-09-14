class DoubleLinkNode:
    def __init__(self, data):
        self.data = data  
        self.prev = None  
        self.next = None  

    def getData(self):
        return self.data

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def __str__(self):
        return f"[{self.data}] <-> "
