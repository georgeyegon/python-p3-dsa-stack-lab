class Stack:
    def __init__(self, items=None, max_size=10):
        """
        Initialize the stack with items and set the maximum size.
        If no items are provided, an empty stack is created.
        """
        if items is None:
            items = []
        self.items = items
        self.max_size = max_size

    def full(self):
        """
        Check if the stack is full.
        Returns True if the stack has reached its maximum size, False otherwise.
        """
        return len(self.items) >= self.max_size

    def push(self, item):
        """
        Add an item to the stack. Raises an error if the stack is full.
        """
        if self.full():
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack. 
        Raises an error if the stack is empty.
        """
        if not self.items:
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self.items)
