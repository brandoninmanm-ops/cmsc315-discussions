"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Loops through every element index from the beginning to the end of the list
    for i in range(len(lst)):
        # Checks if the current element matches the target value
        if lst[i] == target:
            # Returns the index when the target is found
            return i

    # Returns -1 if the loop finishes without finding the target.Linear search has O(n) time complexity because
    # it must evaluate every single element one by one, meaning execution time grows with list size.
    return -1

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Set up low and high pointers to track the current search range
    low = 0
    high = len(lst) - 1

    # Keeps the loop running as long as there's still room left to search
    while low <= high:
        # Finds the middle index to split the remaining search space
        mid = (low + high) // 2

        # Checks if the middle name matches the name value
        if lst[mid] == target:
            return mid
        # If the name comes after the middle element, discards the left half by moving the low pointer
        # up past the midpoint
        elif lst[mid] < target:
            low = mid + 1
        # If the name comes before the middle element, discards the right half by moving the high pointer
        # down below the midpoint
        else:
            high = mid - 1

    # Returns -1 if the name is not found after search has ended
    return -1

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS (Client List)===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST (SMALL CLIENT LIST) ===")

    # Creates a small sorted list array of names to test with
    small_names = ["Brandon I.", "Daniel J.", "Jesus C.", "Lola B.", "Melanie D."]

    # Sets a variable for an existing name for easier following
    # Searches for an existing name using linear search and reflect the index found at.
    existing_name = "Jesus C."
    small_linear_found = linear_search(small_names, existing_name)
    print(f"Linear Search for '{existing_name}': Client found at index {small_linear_found}")

    # Sets a variable for a missing name for easier following
    # Searches for a missing_target name using linear search in small_names array
    missing_name = "Oscar R."
    small_linear_missing = linear_search(small_names, missing_name)
    print(f"Linear Search for '{missing_name}': Returned {small_linear_missing} Client name not on record.")

    # Searches for the existing_target name using binary search in small_names array and reflect the index found at.
    small_binary_found = binary_search(small_names, existing_name)
    print(f"Binary Search for '{existing_name}': Client found at index {small_binary_found}")

    # Searches for the missing_target name using binary search in small_names array
    small_binary_missing = binary_search(small_names, missing_name)
    print(f"Binary Search for '{missing_name}': Returned {small_binary_missing} Client name not on record.")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST (LARGE CLIENT LIST) ===")

    # Creates a large sorted dataset array representing a business client list
    large_client_list = [
        "Alonzo C.", "Artemis K.", "Bobby B.", "Brandon I.", "Chappy G.", "Clint E.", "Daniel J.",
        "Diana M.", "Ethan S.", "Fiona T.", "Frank C.", "Georgina L.", "Henry H.", "Henry J.",
        "Ian B.", "Jesus C.", "Julia Q.", "Justin A.", "Lola B.", "Melanie D.", "Melrose O.",
        "Oscar R.", "Puddles D.", "Randy B.", "Sia M.", "Xaviar P.", "Zelda L."
    ]

    # Sets a client name from deeper in array to the variable large_target for easier following
    large_name = "Puddles D."

    # Tests linear search on the larger client list array using the large_target name and reflect the index found at.
    large_linear_result = linear_search(large_client_list, large_name)
    print(f"Linear Search in large client list for client '{large_name}': Found at index {large_linear_result}")

    # Tests binary search on the larger client list array using the large_target name and reflect the index found at.
    large_binary_result = binary_search(large_client_list, large_name)
    print(f"Binary Search in large client list for client '{large_name}': Found at index {large_binary_result}")

    # Binary search becomes more efficient as datasets grow larger because it cuts the remaining search space
    # in half with every comparison step O(log n), while linear search must check items one by one sequentially
    # O(n), taking more steps as the list expands.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Searches an empty list to verify proper handling without out-of-bounds errors
    empty_list = []
    empty_name = "Melanie M."
    empty_result = binary_search(empty_list, empty_name)
    print(f"Empty List: Client {empty_name} not on record, Returned {empty_result}.")

    # Edge case 2: Searches a single name list, where the name matches the only item in the array
    single_list = ["Sia M."]
    single_name = "Sia M."
    single_result = binary_search(single_list, single_name)
    print(f"Single Name list Match: Client {single_name} found at index {single_result}.")

    # Edge case 3: Searches a dataset where the name value is located at the very first position
    first_position_list = ["Brandon I.", "Daniel J.", "Jesus C.", "Kelly C.", "Mike H.", "Paul S."]
    first_pos = "Brandon I."
    first_result = binary_search(first_position_list, first_pos)
    print(f"First Position: Client {first_pos} found at index {first_result}.")

    # Edge case 4: Searches a dataset where the name value is located in the last position of the list
    last_position_list = ["Brandon I.", "Daniel J.", "Jesus C.", "Kelly C.", "Mike H.", "Paul S."]
    last_pos = "Paul S."
    last_result = binary_search(last_position_list, last_pos)
    print(f"Last Position: Client {last_pos} found at index {last_result}.")

    # Edge case 5: Searches a single-element list where the name value does not match the name present
    mismatch_list = ["Lola B."]
    mismatch_name = "Brandon I."
    mismatch_result = binary_search(mismatch_list, mismatch_name)
    print(f"Single Name list mismatch: Client {mismatch_name} not on record, Returned {mismatch_result}.")

    # Edge case 6: Searches a sorted list containing duplicate name values to see how it behaves
    duplicate_list = ["Brandon I.", "Daniel J.", "Daniel J.", "Jesus C."]
    duplicate_name = "Daniel J."
    duplicate_result = binary_search(duplicate_list, duplicate_name)
    print(f"Duplicate Names: Client {duplicate_name} found at index {duplicate_result}.")
if __name__ == "__main__":
    main()