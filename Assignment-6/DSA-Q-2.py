
class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Check if queue is empty
    def isempty(self):
        return self.front is None

    # 1. Enqueue
    def enqueue(self, new_node):
        if self.isempty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # 2. Dequeue
    def dequeue(self):
        if self.isempty():
            print("queue is empty")
        else:
            temp = self.front
            print("deleted element:", temp.data)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            temp = None

    # 3. Display
    def display(self):
        temp = self.front
        print("queue elements....")

        while temp:
            print(temp.data)
            temp = temp.next

    # 4. Reverse queue using stack
    def reverse(self):
        st = []

        temp = self.front
        while temp:
            st.append(temp.data)
            temp = temp.next

        self.front = None
        self.rear = None

        while st:
            self.enqueue(node(st.pop()))

    # 5. Merge two queues
    def merge(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(node(temp.data))
            temp = temp.next

    # 6. Check identical queues
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None


# Main program
q1 = queue()
q2 = queue()

# Enqueue elements in Queue 1
q1.enqueue(node(10))
q1.enqueue(node(20))
q1.enqueue(node(30))
q1.enqueue(node(40))

# Enqueue elements in Queue 2
q2.enqueue(node(10))
q2.enqueue(node(20))
q2.enqueue(node(30))
q2.enqueue(node(40))

print("Original Queue:")
q1.display()

# Dequeue
q1.dequeue()
q1.display()

# Reverse Queue
q1.reverse()
print("Reversed Queue:")
q1.display()

# Merge two queues
q1.merge(q2)
print("Merged Queue:")
q1.display()

# Check identical queues
if q1.identical(q2):
    print("Both queues are identical")
else:
    print("Queues are not identical")
