
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