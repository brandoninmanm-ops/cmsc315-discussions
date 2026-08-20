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
   I defined the base ParentClass featuring a shared class variable (species_type) 
   and a constructor (__init__) to set up instance attributes. I included display_info(self), 
   which was written to return a formatted string displaying the parent object's current state and attributes.

2. Create a child class using inheritance.
   I built a ChildClass that inherited from the parent using super().__init__(), adding new class and instance 
   variables (including a nested mutable list). I overrode the parent's display_info(self) method to integrate 
   both parent and child attributes, and I added a custom extension method (new_method(self)) to return a 
   customized string tracking the thread author.

3. Demonstrate class and instance namespaces.
   I instantiated child objects, accessed class variables via both the class and instances, dynamically added a
   new attribute to a single object, and inspected scope boundaries. I added the method demonstrate_namespaces(), 
   which outputted internal mapping namespaces using built-in __dict__ attributes for both individual objects and 
   the classes.

4. Demonstrate shallow and deep copying.
   I initialized an object with nested mutable data, created copies, mutated the original nested list, and 
   observed how memory allocations differed. I added the method demonstrate_copying(), which used the copy()
   function for shallow copies and the deepcopy() function for deep copies.

5. Create and test objects in `main()`.
   I set up the primary execution entry point to test all classes, inheritance hierarchies, and evaluation modules.
   I structured main() to instantiate parent and child objects, call their respective display and extension methods, 
   and sequentially invoke demonstrate_namespaces() and demonstrate_copying().

6. Add a student-created extension.
   I implemented a unique student extension method inside the child class to enhance functionality beyond the base
   parent attributes. I  utilized new_method(self), which returned a targeted thread contributor string using the 
   child's unique author_name instance variable.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   This week I really got a handle on how classes work, especially setting up parent and child classes
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