# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation

Binary Search Tree Operations (Insert, Search, In-Order Traversal)
I implemented the tree operations using a Binary Search Tree (BST) as the underlying hierarchical structure 
to manage a collection of names ("Melanie", "Jesus", "Oscar", "Sia", "Daniel", "Puddles", "Brandon", "Rocky", 
"Lola"). Having an interest in organized records and directory management, I thought it would be fun to model 
this around an alphabetical name directory. Although I did consider modifying the code to include a numeric ID 
with each name, I went with keeping standard single-value nodes so I wouldn't deviate from the instructions or 
source code template too much.

I set up insert(value) and _insert_recursive(node, value) to use recursive branching to place a new name into its 
correct sorted position within the tree. I routed smaller values to the left subtree and larger values to the 
right subtree, creating a new node when an empty spot was reached to keep the tree linked.

I built search(value) and _search_recursive(node, value) to traverse down the tree recursively by comparing target
values against current nodes. It returned True immediately upon finding a matching name or False if it hit a dead
end, illustrating a logarithmic search where I relied on the BST structure to eliminate half of the remaining 
search space at every single step instead of scanning items linearly as a list would.

I implemented inorder() and _inorder_recursive(node, values) to perform an in-order traversal visiting the left 
subtree, current node, and right subtree in sequence. Because the BST guarantees that everything on the left is 
smaller and everything on the right is bigger, I saw how left-root-right visiting naturally output the names in 
a fully sorted alphabetical sequence from the names Brandon all the way to Sia.

I modeled my code around a name directory holding the initial values "Melanie", "Jesus", "Oscar", "Sia", "Daniel",
"Puddles", "Brandon", "Rocky", "Lola". I tested searches for both the existing "Melanie", "Brandon" values as 
well as the missing "Alice", "Zack" name values. Edge cases were tested by creating a single-node tree containing
only "Melanie", verifying how single-node searches ("Melanie", "Oscar") and in-order traversals behaved when root
children were both None.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## My Reflection

Working on this assignment really helped me wrap my head around how Binary Search Trees operate. I learned how 
recursion and base cases drive tree traversal and why checking for None prevents crashes. Using an alphabetical 
name directory with names like Melanie, Brandon, and Sia made it easy to visualize hierarchical sorting.

One major challenge I ran into was understanding how recursive helper methods pass nodes back up the chain to keep
the tree linked, especially during edge cases like a single-node tree. I overcame this by tracing execution 
step-by-step and adding detailed comments to map out what happens when a search hits a dead end.

Compared to a standard linear list where you check every item one by one, a BST is much more efficient. For 
example, when searching for "Brandon" in my tree with root "Melanie", the algorithm looks left, instantly 
skipping the right side's larger names like "Oscar" and "Sia". Every comparison cuts the remaining search space
in half, giving you logarithmic performance instead of sequential scanning.