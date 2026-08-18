"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque

class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # Initialize an empty Python list to hold the stack elements.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Append the new value to the end of the list, making it the top of the stack.
        self.items.append(value)
        # This supports LIFO behavior because the most recently appended item is positioned
        # at the end of the list and will be the very first one accessed or removed.

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Check if the stack is empty before attempting a removal to prevent IndexError.
        if self.is_empty():
            print("Error: Cannot pop empty stack.")
            return None
        # Removes and returns the top item from the list.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Check if the stack is empty before attempting to view the top element.
        if self.is_empty():
            print("Error: Cannot peek empty stack.")
            return None
        # Peek returns the value at the top of the stack without altering or removing it from the stack.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Returns True if the length of the internal list is zero, otherwise False.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # Initialize an empty deque object.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Add the new value to the back.
        self.items.append(value)
        # This supports FIFO behavior because incoming items join the back of the line,
        # waiting behind all previously added elements.

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Check if the queue is empty to prevent removal errors.
        if self.is_empty():
            print("Error: Cannot dequeue an empty queue.")
            return None
        # Removes and returns the element from the front.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Check if the queue is empty before trying to inspect the front item.
        if self.is_empty():
            print("Error: Cannot view the front of an empty queue.")
            return None
        # Returns the value at the very front without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Returns True if deque is zero, else False.
        return len(self.items) == 0


def main():
    print("UNIT 2: STACKS AND QUEUES")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n STACK DEMO ")

    # Instantiates a new Stack object.
    my_stack = Stack()

    # Pushes four integer values onto the stack.
    print("Pushing values to the stack: 22, 3, 89, 9")
    my_stack.push(22)
    my_stack.push(3)
    my_stack.push(89)
    my_stack.push(9)

    # Displays the current top item using the peek method without removing.
    print(f"Peek: {my_stack.peek()}")

    # Loops through the stack until empty, popping and printing elements, LIFO.
    print("\nDemonstrating LIFO by popping all items:")
    while not my_stack.is_empty():
        print(f"Popped item: {my_stack.pop()}")

    # Tests the empty-stack error handling by calling pop() on an already empty stack.
    print("\nEdge Case: Testing pop() on an empty stack:")
    my_stack.pop()

    # Tests the empty-stack error handling by calling peek() on an already empty stack.
    print("\nEdge Case: Testing peek() on an empty stack:")
    my_stack.peek()

    # Tests a single-item stack lifecycle.
    print("\nEdge Case: Verifying single-item stack is empty after pop:")
    single_stack = Stack()
    single_stack.push(22)
    print(f"Pushed 22. Is stack empty? {single_stack.is_empty()}")
    print(f"Popped item: {single_stack.pop()}")
    print(f"Is stack empty after pop? {single_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n QUEUE DEMO ")

    # Instantiate a new Queue object for demonstration.
    my_queue = Queue()

    # Enqueue four values representing customers in line.
    print("Enqueuing values: 'Melanie', 'Puddles', 'Oscar', 'Jesus'")
    my_queue.enqueue("Melanie")
    my_queue.enqueue("Puddles")
    my_queue.enqueue("Oscar")
    my_queue.enqueue("Jesus")

    # Displays the current front element using the front method without removing it.
    print(f"Front of queue: {my_queue.front()}")

    # Loops through the queue until empty, dequeuing elements to prove FIFO behavior.
    print("\nDemonstrating FIFO, dequeue() for all elements:")
    while not my_queue.is_empty():
        print(f"Dequeued: {my_queue.dequeue()}")

    # Tests the empty-queue error handling by calling dequeue() on an already empty queue.
    print("\nEdge Case: Testing dequeue() on an empty queue:")
    my_queue.dequeue()

    # Tests the empty-queue error handling by calling front() on an already empty queue.
    print("\nEdge Case: Testing front() on an empty queue:")
    my_queue.front()

    # Tests a single-item queue lifecycle.
    print("\nEdge Case: Verifying single-item queue becomes empty:")
    single_queue = Queue()
    single_queue.enqueue("Single-Item")
    print(f"Enqueued 'Single-Item'. Is queue empty? {single_queue.is_empty()}")
    print(f"Dequeued item: {single_queue.dequeue()}")
    print(f"Is the queue empty after removal? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()