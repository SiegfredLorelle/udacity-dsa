"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

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

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        # If there are element in ll (not empty)
        if self.head.next:
            # Save previous head as tmp (neeeded to return)
            tmp_previous_head = self.head
            # Make the next element as haed
            self.head = self.head.next
            return tmp_previous_head
        # If in ll is empty, then there is no head
        self.head = None
        return self.head


class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        # Save the previous head as tmp
        tmp_previous_head = self.ll.head
        # Insert the new element in the ll
        self.ll.insert_first(new_element)
        # Change the pointer of the new_element (new head) to the previous head (save as tmp)
        self.ll.head.next = tmp_previous_head 

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        # Save the previous head as tmp
        tmp_previous_head = self.ll.head
        # If the ll is not empty
        if tmp_previous_head:
            # Delete the first element(head) and return it
            self.ll.delete_first()
            return tmp_previous_head
        # If ll is empty or head is not configured
        return None


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value) 
print(stack.pop().value) 
print(stack.pop().value) 
print(stack.pop()) 
stack.push(e4)
print(stack.pop().value) 