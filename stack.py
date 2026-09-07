class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # Points to top of the stack

    def is_empty(self):
        return self.top is None

    def push(self, data):
        """Add element to the top of stack - O(1)"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {data}")

    def pop(self):
        """Remove and return element from top of stack - O(1)"""
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        """View the top element - O(1)"""
        if self.is_empty():
            return None
        return self.top.data

    def display(self):
        curr = self.top
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("Stack (Top -> Bottom): " + " -> ".join(elements))


# --- Stack Example Usage ---
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popped:", stack.pop())
    stack.display()