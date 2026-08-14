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
    species_type = "Discussion One"

    def __init__(self, topic_name, post_count):
        self.topic_name = topic_name
        self.post_count = post_count

    def display_info(self):
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
    sub_category = "Discussion Topic"

    def __init__(self, topic_name, post_count, author_name, tags):
        super().__init__(topic_name, post_count)
        self.author_name = author_name
        self.tags = tags

    def new_method(self):
        return f"Author {self.author_name} has contributed to this thread."

    def display_info(self):
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
    print("\n=== Namespace Demonstration ===")

    obj1 = ChildClass("Python OOP", 12, "Alice", ["code", "classes"])
    obj2 = ChildClass("Namespaces", 8, "Bob", ["scope"])

    print(f"Accessing class variable via class (ChildClass.sub_category): {ChildClass.sub_category}")
    print(f"Accessing class variable via object 1 (obj1.sub_category): {obj1.sub_category}")

    obj1.special_badge = "Gold Star"

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
    print("\n=== Copy Demonstration ===")

    original_obj = ChildClass("Original Topic", 15, "Charlie", ["draft", ["reference1", "reference2"]])

    shallow_copied_obj = copy(original_obj)

    deep_copied_obj = deepcopy(original_obj)

    print("--- BEFORE MODIFYING NESTED DATA ---")
    print(f"Original Tags:       {original_obj.tags}")
    print(f"Shallow Copy Tags:   {shallow_copied_obj.tags}")
    print(f"Deep Copy Tags:      {deep_copied_obj.tags}")

    original_obj.tags[1].append("reference3")

    print("\n--- AFTER MODIFYING ORIGINAL'S NESTED DATA ---")
    print(f"Original Tags:       {original_obj.tags}")
    print(f"Shallow Copy Tags:   {shallow_copied_obj.tags}  (Affected because inner list is shared)")
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
    print("=== Unit 1 OOP Assignment ===")

    parent_obj = ParentClass("General Forum", 50)
    print("\n[Parent Object Test]")
    print(parent_obj.display_info())

    child_obj = ChildClass("Weekly Discussion", 20, "Dana", ["introduction", ["post1"]])
    print("\n[Child Object Test]")
    print(child_obj.display_info())
    print(child_obj.new_method())

    demonstrate_namespaces()

    demonstrate_copying()


if __name__ == "__main__":
    main()