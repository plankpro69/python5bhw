import random

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def get_length(self) -> int:
        return self.length
    
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next
    
    def get_first_elem(self):
        return self.head.value if self.head else None
    
    def get_last_elem(self):
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.value
    
    def find(self, value: int) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

if __name__ == "__main__":
    linked_list = LinkedList()
    for _ in range(10):  # Füge 10 zufällige Zahlen hinzu
        linked_list.append(random.randint(1, 100))
    
    print("Länge der Liste:", linked_list.get_length())
    print("Elemente der Liste:")
    linked_list.display()
    
    print("Erstes Element:", linked_list.get_first_elem())
    print("Letztes Element:", linked_list.get_last_elem())
    print("Ist 30 enthalten?:", linked_list.find(30))
