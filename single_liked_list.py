class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_front(self):
            if self.head is None:
                return
            
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


Linkedlist = Linkedlist()

Linkedlist.add_to_front(3)
Linkedlist.add_to_front(2)
Linkedlist.add_to_front(1)

Linkedlist.add_to_end(4)
Linkedlist.add_to_end(5)
Linkedlist.add_to_end(6)

print("Linked list awal:")
Linkedlist.print_linked_list()

Linkedlist.remove_front()
Linkedlist.remove_end()

print("Linked list setelah penghapusan:")
Linkedlist.print_linked_list()

