# Doubly Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Forward Traversal
    def traverse_forward(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head

        print("Forward: None", end="")

        while current is not None:
            print(" <->", current.data, end="")
            current = current.next

        print(" <-> None")

    # 2. Backward Traversal
    def traverse_backward(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head

        # Move to the last node
        while current.next is not None:
            current = current.next

        print("Backward: None", end="")

        while current is not None:
            print(" <->", current.data, end="")
            current = current.prev

        print(" <-> None")

    # 3. Search
    def search(self, key):
        current = self.head
        position = 1

        while current is not None:
            if current.data == key:
                print(f"{key} found at position {position}.")
                return True

            current = current.next
            position += 1

        print(f"{key} not found.")
        return False

    # 4. Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print(f"Inserted {data} at beginning.")

    # 5. Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at end.")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

        print(f"Inserted {data} at end.")

    # 6. Insert at a Specific Position
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        new_node = Node(data)

        # Insert at beginning
        if position == 1:
            if self.head is not None:
                new_node.next = self.head
                self.head.prev = new_node

            self.head = new_node

            print(f"Inserted {data} at position {position}.")
            return

        current = self.head

        # Move to node before required position
        for i in range(1, position - 1):
            if current is None:
                print("Invalid position.")
                return

            current = current.next

        if current is None:
            print("Invalid position.")
            return

        # Connect new node
        new_node.next = current.next
        new_node.prev = current

        # If new node is not inserted at the end
        if current.next is not None:
            current.next.prev = new_node

        current.next = new_node

        print(f"Inserted {data} at position {position}.")

    # 7. Delete from Beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        deleted_data = self.head.data

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

        print(f"Deleted {deleted_data} from beginning.")

    # 8. Delete from End
    def delete_at_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # Only one node
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None

            print(f"Deleted {deleted_data} from end.")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        deleted_data = current.data

        current.prev.next = None

        print(f"Deleted {deleted_data} from end.")

    # 9. Delete from Specific Position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if position < 1:
            print("Invalid position.")
            return

        current = self.head

        # Delete first node
        if position == 1:
            self.delete_at_beginning()
            return

        # Move to target node
        for i in range(1, position):
            if current is None:
                print("Invalid position.")
                return

            current = current.next

        if current is None:
            print("Invalid position.")
            return

        # Connect previous node to next node
        if current.prev is not None:
            current.prev.next = current.next

        # Connect next node to previous node
        if current.next is not None:
            current.next.prev = current.prev

        print(f"Deleted {current.data} from position {position}.")

    # 10. Delete by Value
    def delete_by_value(self, key):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head

        # Search for the node
        while current is not None and current.data != key:
            current = current.next

        if current is None:
            print(f"{key} not found.")
            return

        # If node is head
        if current == self.head:
            self.delete_at_beginning()
            return

        # Connect previous node
        if current.prev is not None:
            current.prev.next = current.next

        # Connect next node
        if current.next is not None:
            current.next.prev = current.prev

        print(f"Deleted {key} from the list.")

    # 11. Count Nodes
    def count_nodes(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        print(f"Number of nodes: {count}")
        return count


# --------------------------------------------------
# Main Program
# --------------------------------------------------

if __name__ == "__main__":

    dll = DoublyLinkedList()

    print("----- INSERTION -----")

    dll.insert_at_end(20)
    dll.insert_at_beginning(10)
    dll.insert_at_end(40)
    dll.insert_at_position(30, 3)

    dll.traverse_forward()

    print("\n----- BACKWARD TRAVERSAL -----")

    dll.traverse_backward()

    print("\n----- SEARCH -----")

    dll.search(30)
    dll.search(100)

    print("\n----- COUNT -----")

    dll.count_nodes()

    print("\n----- DELETE FROM BEGINNING -----")

    dll.delete_at_beginning()
    dll.traverse_forward()

    print("\n----- DELETE FROM END -----")

    dll.delete_at_end()
    dll.traverse_forward()

    print("\n----- DELETE FROM POSITION -----")

    dll.delete_at_position(2)
    dll.traverse_forward()

    print("\n----- DELETE BY VALUE -----")

    dll.delete_by_value(30)
    dll.traverse_forward()

    print("\n----- FINAL BACKWARD TRAVERSAL -----")

    dll.traverse_backward()