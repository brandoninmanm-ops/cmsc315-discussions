# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
   Implementation: Define a foundational base class representing a generic discussion forum entity
   Include a class-level variable
   Implement an constructor taking at least two instance attributes
   Define an instance method to return a formatted string displaying the parent object's current state

2. Create a child class using inheritance.
   Implementation: Build a specialized subclass inheriting from ParentClass to demonstrate inheritance, method overriding, and 	functionality extension.
   Inherit using class ChildClass/ParentClass
   Add a new class-level variable
   Expand the constructor while introducing new instance variables and tags, including a nested mutable list for copying tests
   Create a student-defined extension method to provide unique behavior
   Override the parent's method to integrate both parent and child attributes

3. Demonstrate class and instance namespaces.
   Implementation: Showcase Python's scope lookup hierarchy and dynamic attribute handling using object dictionaries.
   Instantiate at least two unique ChildClass objects
   Access a class variable via both the class reference and an instance reference
   Dynamically assign a new attribute to a single instance post-instantiation
   Output and inspect mapping namespaces using built-in attributes for both individual objects and the parent/child classes

4. Demonstrate shallow and deep copying.
   Implementation: Contrast memory allocation behavior between shallow and deep copies when handling nested mutable objects
   Initialize an object containing a nested mutable data structure
   Generate a shallow copy using copy and a deep copy using deepcopy
   Mutate a nested element within the original object's container
   Compare outcomes to demonstrate how shallow copies preserve reference pointers to inner mutable items while deep copies 	recursively clone all underlying structures independently.

5. Create and test objects in `main()`.
   Implementation: Establish the primary execution entry point to test all classes, inheritance hierarchies, and demonstration 	modules
   Instantiate and test a standalone ParentClass object, verifying its constructor and display method
   Instantiate and test a ChildClass object, verifying inherited methods, overridden display output, and the student-created 	extension method
   Invoke demonstrate sequentially to execute the full evaluation suite.

6. Add a student-created extension.
   Implementation: Built a custom student-created extension method inside the child class that introduces targeted thread contributor 	tracking functionality beyond the base parent attributes.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   This week I really got a handle on how classes work in Python, especially setting up parent and child classes
   with inheritance. I also learned how namespaces work using __dict__ to see what's actually stored inside an object
   versus the class. Plus, doing the shallow vs. deep copy exercise really cleared up how Python handles memory when
   you have lists nested inside other objects.

2. What challenges did you encounter, and how did you overcome them?
   My biggest hurdle was wrapping my head around shallow copying. I kept messing up why changing a nested list in the
   original object also changed the shallow copy. I ended up having to run a few test prints and read up on it to
   finally realize shallow copies only copy the outer shell, whereas you need deepcopy if you want the inner lists to
   be totally separate.

3. Compare OOP to procedural programming.
   Procedural programming is pretty much just writing step-by-step functions that pass variables back and forth in a
   straight line. OOP is different because it bundles the data and the functions that use that data together into objects.
   It just feels a lot more natural to organize your code that way once a project gets past a certain size.

4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application
   development, and future use.
   The best part about OOP is that you don't have to rewrite the same code over and over again. Because of inheritance,
   you can build a solid parent class and then just reuse it for your child classes. This cuts down on a ton of overhead
   and makes maintenance way easier. In real-world app development, that kind of modularity is a lifesaver—if something
   breaks or needs an update later on, you can just fix it in one spot instead of hunting through a massive file trying
   to untangle a bunch of procedural functions.