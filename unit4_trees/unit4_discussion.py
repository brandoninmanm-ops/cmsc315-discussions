"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""

class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initializes references
        # to the left and right child nodes.

        # Saves the value passed into this node
        self.value = value

        # Left and right children are empty
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # Starts with an empty tree, so root = None
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Kicks off recursion from the root node
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If an empty spot is reached, creates a new node; otherwise, recursively route smaller
        # values left and larger values right, returning the node back up the chain to keep the tree linked
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Starts searching from the root node
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Hits a dead end, value isn't here
        if node is None:
            return False

        # Finds a match
        if node.value == value:
            return True

        # BST search is more efficient than linear search because at every single step,
        # half the remaining tree (left or right) is eliminated instead of checking every
        # single item like a list!
        if value < node.value:
            # Looks in the left subtree if alphabetically smaller
            return self._search_recursive(node.left, value)
        else:
            # Looks in the right subtree if alphabetically larger
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Container for traversal results
        values = []

        # Starts helper traversal
        self._inorder_recursive(self.root, values)

        # Returns the final list of values
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # Step 1: Visits left subtree first to get smaller items
            self._inorder_recursive(node.left, values)

            # Step 2: Grabs the current node's value
            values.append(node.value)

            # Step 3: Visits right subtree for larger items
            self._inorder_recursive(node.right, values)

# This traversal produces sorted output because the BST structure guarantees
# everything on the left is alphabetically smaller and everything on the right is larger,
# allowing left-root-right visiting to output the names in an alphabetized sequence from Brandon to Sia!


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Creates a tree instance
    my_bst = BST()

    # I used nine name values to populate both left and right sides alphabetically
    values_to_insert = ["Melanie", "Jesus", "Oscar", "Sia", "Daniel", "Puddles", "Brandon", "Rocky", "Lola"]

    # Inserts each name one by one
    for val in values_to_insert:
        my_bst.insert(val)

    # Displays inserted values
    print(f"Inserted values: {values_to_insert}")

    # A BST efficiently reduces search space because every comparison discards half the tree.
    # Searching for 'Brandon', which comes earlier alphabetically than the root 'Melanie',
    # instantly skips the entire right side of the tree containing larger names like 'Oscar' and 'Sia'!

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # Gets sorted list via in-order traversal
    sorted_result = my_bst.inorder()

    # Displays output
    print(f"In-order traversal results: {sorted_result}")

    # Since in-order traversal always visits left, root, then right, and the tree is
    # structured with alphabetically smaller names on the left and larger on the right,
    # it naturally produces a fully sorted alphabetical list of names, starting from 'Brandon' up to 'Sia'.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Checks existing value, should be true
    print(f"Searching for 'Melanie' (exists): {my_bst.search('Melanie')}")

    # Checks another existing value, should eb true
    print(f"Searching for 'Brandon' (exists): {my_bst.search('Brandon')}")

    # Checks missing value, should be false
    print(f"Searching for 'Becky' (does not exist): {my_bst.search('Becky')}")

    # Checks another missing value, should eb false
    print(f"Searching for 'Tosh' (does not exist): {my_bst.search('Tosh')}")

    # The search method navigates left or right recursively until it either finds a match True,
    # or hits a dead end None or False.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Creates a tree with only one node to test single-node behavior
    single_node_tree = BST()
    single_node_tree.insert("Melanie")

    # Searches for the single existing value, should return True
    print(f"Searching single-node tree for 'Melanie': {single_node_tree.search('Melanie')}")

    # Searches for a non-existent value, should return False
    print(f"Searching single-node tree for 'Oscar': {single_node_tree.search('Oscar')}")

    # Performs in-order traversal on the single-node tree, should return Melanie
    print(f"Traversing single-node tree: {single_node_tree.inorder()}")

# With only one node containing "Melanie", the root has no children (left and right are None),
# so recursive operations like searching for "Oscar" or traversing immediately hit base cases
# after a single step.

if __name__ == "__main__":
    main()