# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Implementation

Stack (LIFO)

I implemented the Stack class using a standard Python list (self.items) as 
the underlying data structure to manage element storage.

__init__() initialized an empty list to hold the stack items.

push(value) appended the new value to the end of the list. This supported LIFO behavior 
because the most recently appended item sat at the top of the stack and would be accessed 
or removed first.

pop() checked if the stack was empty using is_empty() to prevent an IndexError. If empty, 
it printed a warning and returned None; otherwise, it removed and returned the top item.

peek() checked for emptiness and returned the top item via self.items[-1] without removing it, 
acting as a read-only inspection of the most recent element.

is_empty() returned True when the internal list length was zero.

I modeled the stack demo around pushing multiple integers (22, 3, 89, 9), peeking at the top element, 
and popping them sequentially to demonstrate LIFO behavior. Edge cases were tested by popping and peeking 
an empty stack, and by confirming a single-item stack became empty after its one item was removed.

Queue (FIFO)

I implemented the Queue class using collections.deque (self.items), which supports efficient O(1) appends 
and removals from both ends.

__init__() initialized an empty deque object.

enqueue(value) appended the new value to the back of the queue. This supported FIFO behavior because incoming 
elements joined the back of the line behind all previously added items.

dequeue() checked if the queue was empty to prevent removal errors, printing an error message and returning None 
if empty, or else removing and returning the front element via popleft().

front() checked for emptiness and returned the first element (self.items[0]) without removing it, showing who was 
next in line.

is_empty() returned True when the deque held no items.

I modeled the queue demo around enqueuing names ("Melanie", "Puddles", "Oscar", "Jesus"), inspecting the front of
the line, and dequeuing items in arrival order to prove FIFO behavior. Edge cases were tested by dequeuing and viewing
 the front of an empty queue, and by verifying a single-item queue became empty after its single item was dequeued.


## My Reflection

While working on this assignment, I learned how to build stacks and queues
from scratch using Python lists and deques. I started out by carefully reading
through the template and commenting on what every section did before I wrote my
own code, which made the rest of the assignment much easier to follow.

One big challenge I ran into was figuring out what happens if someone tries to pop
an item from an empty stack or queue, which usually causes a crash. I fixed this by
using an is_empty check inside my methods, so it safely prints a warning message instead
of crashing.

The main difference between the two really comes down to order. Stacks use LIFO for things
like an undo button where the newest action matters first. Queues use FIFO for things like
lines or print jobs where order of arrival matters.