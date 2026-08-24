# Singly Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Display / Traverse
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")

    # 2. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print(data, "inserted at beginning")

    # 3. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(data, "inserted at end")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

        print(data, "inserted at end")

    # 4. Insert at a specific position
    def insert_position(self, data, position):
        new_node = Node(data)

        # Insert at first position
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(data, "inserted at position", position)
            return

        temp = self.head

        # Move to node before required position
        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position")
                return

            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

        print(data, "inserted at position", position)

    # 5. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        deleted = self.head.data

        self.head = self.head.next

        print(deleted, "deleted from beginning")

    # 6. Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        # Only one node
        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            print(deleted, "deleted from end")
            return

        temp = self.head

        # Move to second-last node
        while temp.next.next is not None:
            temp = temp.next

        deleted = temp.next.data

        temp.next = None

        print(deleted, "deleted from end")

    # 7. Delete from a specific position
    def delete_position(self, position):
        if self.head is None:
            print("Linked List is empty")
            return

        # Delete first node
        if position == 1:
            deleted = self.head.data
            self.head = self.head.next

            print(deleted, "deleted from position", position)
            return

        temp = self.head

        # Move to node before required position
        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position")
                return

            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position")
            return

        deleted = temp.next.data

        temp.next = temp.next.next

        print(deleted, "deleted from position", position)

    # 8. Search an element
    def search(self, key):
        temp = self.head
        position = 1

        while temp is not None:
            if temp.data == key:
                print(key, "found at position", position)
                return

            temp = temp.next
            position += 1

        print(key, "not found")

    # 9. Count number of nodes
    def count(self):
        temp = self.head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 10. Reverse the linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous

        print("Linked List reversed")


# ------------------------------------------------
# Main Program
# ------------------------------------------------

ll = SinglyLinkedList()

# Insert operations
ll.insert_beginning(20)
ll.insert_beginning(10)

ll.insert_end(30)
ll.insert_end(40)

print("\nLinked List:")
ll.display()

# Insert at position
ll.insert_position(25, 3)

print("\nAfter inserting 25 at position 3:")
ll.display()

# Search
print()
ll.search(30)
ll.search(100)

# Count
ll.count()

# Delete beginning
print()
ll.delete_beginning()

print("After deleting from beginning:")
ll.display()

# Delete end
print()
ll.delete_end()

print("After deleting from end:")
ll.display()

# Delete position
print()
ll.delete_position(2)

print("After deleting position 2:")
ll.display()

# Reverse
print()
ll.reverse()

print("After reversing:")
ll.display()

# Count again
ll.count()