"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable shared across all instances of ParentClass
    species_type = "Discussion One"

    def __init__(self, topic_name, post_count):
        # Initialize instance variables for the topic name and post count
        self.topic_name = topic_name
        self.post_count = post_count

    def display_info(self):
        # Return a formatted string displaying parent object attributes
        return f"Parent Object -> Topic: {self.topic_name}, Posts: {self.post_count}, Type: {self.species_type}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable specific to ChildClass
    sub_category = "Discussion Topic"

    def __init__(self, topic_name, post_count, author_name, tags):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__(topic_name, post_count)
        # Initialize new instance variables for the author and tags
        self.author_name = author_name
        self.tags = tags

    def new_method(self):
        # Return a string using the new child instance variables
        return f"Author {self.author_name} has contributed to this thread."

    def display_info(self):
        # Override the parent display_info method to include child-specific attributes
        return (f"Child Object -> Topic: {self.topic_name}, Posts: {self.post_count}, "
                f"Author: {self.author_name}, Tags: {self.tags}, Type: {self.species_type}")

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\nNamespace Demonstration ")

    # Create two child class objects with distinct initial values
    obj1 = ChildClass("Python OOP", 12, "Alice", ["code", "classes"])
    obj2 = ChildClass("Namespaces", 8, "Bob", ["scope"])

    # Access class variable directly via the class and via an instance object
    print(f"Accessing class variable via class (ChildClass.sub_category): {ChildClass.sub_category}")
    print(f"Accessing class variable via object 1 (obj1.sub_category): {obj1.sub_category}")

    # Add a dynamic instance attribute to only the first object
    obj1.special_badge = "Gold Star"

    # Display internal dictionaries (__dict__) to inspect instance and class namespaces
    print(f"\nObject 1 __dict__:\n{obj1.__dict__}")
    print(f"\nObject 2 __dict__:\n{obj2.__dict__}")

    print(f"\nChildClass __dict__ (Class Namespace):\n{ChildClass.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\nCopy Demonstration")

    # Create an object with a nested mutable list structure inside 'tags'
    original_obj = ChildClass("Original Topic", 15, "Charlie", ["draft", ["reference1", "reference2"]])

    # Create a shallow copy using the copy() function
    shallow_copied_obj = copy(original_obj)

    # Create a deep copy using the deepcopy() function
    deep_copied_obj = deepcopy(original_obj)

    print("BEFORE MODIFYING NESTED DATA")
    print(f"Original Tags:       {original_obj.tags}")
    print(f"Shallow Copy Tags:   {shallow_copied_obj.tags}")
    print(f"Deep Copy Tags:      {deep_copied_obj.tags}")

    # Mutate the inner nested list within the original object
    original_obj.tags[1].append("reference3")

    print("\nAFTER MODIFYING ORIGINAL'S NESTED DATA")
    print(f"Original Tags:       {original_obj.tags}")
    # Explanation: Shallow copy replicates the outer container but references the same inner mutable objects
    print(f"Shallow Copy Tags:   {shallow_copied_obj.tags}  (Affected because inner list is shared)")
    # Explanation: Deep copy recursively duplicates all nested objects, keeping them completely independent
    print(f"Deep Copy Tags:      {deep_copied_obj.tags}  (Unaffected because inner structure is independently cloned)")

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("Unit 1 OOP Assignment")

    # Instantiate and test the parent class object
    parent_obj = ParentClass("General Forum", 50)
    print("\nParent Object Test")
    print(parent_obj.display_info())

    # Instantiate and test the child class object, demonstrating inheritance and method overriding
    child_obj = ChildClass("Weekly Discussion", 20, "Dana", ["introduction", ["post1"]])
    print("\nChild Object Test")
    print(child_obj.display_info())
    print(child_obj.new_method())

    # Execute the namespace demonstration function
    demonstrate_namespaces()

    # Execute the copying demonstration function
    demonstrate_copying()


if __name__ == "__main__":
    main()