class Stack:
    def __init__(self):
        self.items = []
        self.max_item = None

    def push(self, item):
        if self.items == []:
            self.items.append(item)
            self.max_item = item
        else:
            self.max_item = max(self.max_item, item)
            self.items.append(item)
