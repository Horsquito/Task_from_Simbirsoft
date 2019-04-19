class Stack:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        if not self.items:
            self.items.append(item)
            self.max_items.append(item)
        else:
            if max(self.max_items) < item:
                self.max_items.append(item)
            self.items.append(item)

    def get_max_item(self):
        return self.max_items[-1]
