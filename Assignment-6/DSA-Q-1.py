
# Create a Node
class node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Create Stack using Linked List
class stack:
    def __init__(self):
        self.top = None

    # Check whether stack is empty
    def isempty(self):
        return self.top is None

    # Insert element into stack
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # Remove top element from stack
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp = self.top
            print("poped element:", temp.data)
            self.top = self.top.next
            temp = None

    # Reverse stack using another stack
    def reverse(self, st1):
        temp = self.top
        while temp:
            st1.push(node(temp.data))
            temp = temp.next

    # Display stack elements
    def print(self):
        temp = self.top
        print("stack element....")
        while temp:
            print(temp.data)
            temp = temp.next


# Main program
st = stack()
st1 = stack()

# Push elements
st.push(node(10))
st.push(node(100))
st.push(node(45))
st.push(node(78))
st.push(node(90))

# Display original stack
st.print()

# Pop element
st.pop()

# Display after pop
st.print()

# Reverse stack using second stack
st.reverse(st1)

# Display reversed stack
st1.print()
