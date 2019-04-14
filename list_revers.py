class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        previous_value = None
        current_value = self.head
        while(current_value is not None):
            next_value = current_value.next
            current_value.next = previous_value
            previous_value = current_value
            current_value = next_value
        self.head = previous_value 
