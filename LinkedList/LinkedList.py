class Node:
    def __init__(self, data, next = None):
        self.value = data
        self.next = next
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    def add_end(self, data):
        temp = self.head
        while(temp.next != None):
             temp = temp.next
        temp.next = Node(data)
        return temp
    def add_first(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        return temp
    def delete_first(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
    def delete_last(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None
    def insert_at(self, data, i):
        node = Node(data)
        temp = self.head
        while i - 1 > 0:
            temp = temp.next
            i-=1
        node.next = temp.next
        temp.next = node
    def delete_at(self, i):
        temp = self.head
        while i - 1 > 0:
            temp = temp.next
            i-=1
        temp.next = temp.next.next
    def print(self):
        temp = self.head
        while temp != None:
            print("|",temp.value,"|"," --> ", end = '')
            temp = temp.next
        print("None")
list = LinkedList(10)
list.add_end(20)
list.add_end(30)
list.add_first(50)
list.insert_at(100, 2)
list.delete_first()
list.print()