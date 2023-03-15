"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Start from 1 because intruction said first pos is 1
        counter = 1
        # Start with the head
        current = self.head
        # Ensures an head exists
        if self.head:
            # Traverse the linked list until given position is reached
            while counter != position:
                # Increment the counter
                counter += 1
                if current.next:
                    # Go to next node/element
                    current = current.next
                else:
                    # Cannot reach given position (invalid)
                    return None
            # Return the node/element when given position is reached
            return current
        # Error because linked list is empty or its head was not configured
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Append the new element to the linked list
        ll.append(new_element)
        # Create a counter to determine position
        counter = 1
        # Start at the head
        current = self.head
        # Ensures an head exists
        if self.head:
            # Traverse linked list until given position is reached
            while counter <= position:
                # If on element before the position
                if counter == position - 1:
                    # Copy its pointer in tmp
                    tmp_pointer = current.next
                    # Then change its pointer to the new element
                    current.next = new_element
                # If on the given position (inserted element)
                elif counter == position:
                    # Add a pointer directing to pointer of previous element (saved in tmp)
                    current.next = tmp_pointer
                # Add a counter and move to next element
                counter += 1
                current = current.next
        # Error because linked list is empty or its head was not configured
        else:
            return None

    def delete(self, value):
        """Delete the first node with a given value."""
        # Ensure a head exists
        if self.head:
            # Start at the head of the linked list
            current = self.head
            # If first element is the one to be deleted
            if current.value == value:
                # Configure second element to be the head
                self.head = current.next
                return

            # If the element to be deleted is not the first element
            while True:
                # Check the if the next element is the one to be deleted
                if current.next.value == value:
                    # Change the pointer to the pointer of the next element (skipping the element to be deleted)
                    current.next = current.next.next
                    return
                current = current.next
        # Error becuase linked list is empty or its head was not configured
        else:
            return None

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)


# Test delete
ll.delete(2)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)