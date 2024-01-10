# append(value) - добавление узла в конец списка
# prepend(value) - добавление узла в начало списка 
# get(index) - получение значения узла по индексу
# contains(value) - содержится ли узел в списке
# remove(value) - удаление узла по значению 

class Node:
  def __init__ (self, value):
    self.value = value
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return self.head
        head = self.head
        while (head.next):
            head = head.next
        head.next = Node(value)
        return self.head
        
    def prepend(self, value):
        headCurrent = self.head
        self.head = Node(value)
        self.head.next = headCurrent
        return self.head
        
    def get(self, index):
        head = self.head
        i = 0
        while i <= index and head:
            if i == index:
                return head
            i = i + 1
            head = head.next
        else:
            return "Node does not exist"
            
    def contains(self, value):
        head = self.head
        while (head):
            if value == head.value:
                return True
            else:
                head = head.next
        return False
    
    def remove(self, value):
        head = self.head
        if (head.value == value):
            self.head = head.next
            return head
        while (head):
            print(head.value)
            if (head.next and head.next.value == value):
                head.next = head.next.next
                return head
            head = head.next
        return "Node does not exist"
