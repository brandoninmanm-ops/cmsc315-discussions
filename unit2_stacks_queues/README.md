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