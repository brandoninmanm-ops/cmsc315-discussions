# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation

I implemented the search operations using both linear search and binary search as underlying algorithmic approaches to 
manage and query a client list. I modeled the code around a basic client directory lookup tool designed to track and 
verify customer names.

I tested both my algorithms on a small dataset to verify functionality under basic conditions. Including searching 
for an existing client and handling a missing client name across both linear and binary search functions.

I then scaled the list by testing both algorithms on a larger dataset containing 27 alphabetized client names. 
Using the target name "Puddles D.", I observed how sequential linear scanning behaves versus binary search's 
divide-and-conquer approach as the pool of client names grew.

I built six edge cases to test my code's boundaries: an empty list, a single-name match, a first-position match,
a last-position match, a single-name mismatch and duplicate names search. Each of my test outputs clear reporting 
messages showing the specific client name searched and the resulting index or failure status.

My code implements and compares two search strategies: linear search for sequential evaluation and binary search 
for divide-and-conquer efficiency. It uses sorted array data structures representing a client directory to manage 
and query customer records across varying dataset sizes. Time complexity principles are applied to contrast the 
linear scale of O(n) operations with the logarithmic scale of O(logn) midpoint pointer updates. Boundary handling 
is demonstrated through my edge cases covering empty lists, single-element evaluations, positional extremes, and 
duplicate values.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

Working on this code helped me lock down how sequential scans compare to divide-and-conquer logic. Building both 
linear and binary search for my client directory gave me a solid grasp of O(n) versus O(logn) time complexities 
and pointer management.

The trickiest part for me was making sure the binary search pointers updated cleanly without getting stuck in an 
infinite loop, especially when handling tricky edge cases like empty lists or single-element mismatches. Stepping 
through the midpoint calculation logic step-by-step helped me step through it.

As for choosing between them, linear search is fine when your data is unsorted or small because you don't have to
waste time ordering it first, or about time to locate. But for a massive, growing client directory, binary search 
is a timesaver since it chops the search space in half at every step, making it more efficient despite the requirement
for a sorted list.

One thing I was interested in was integrating Python's time.perf_counter() to test out the microsecond-level 
execution times and see the raw performance gap between the two algorithms across different dataset sizes.