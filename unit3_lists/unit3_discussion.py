"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Calls the built-in insert method to place the new telemetry packet at the specified index
    lst.insert(index, value)
    # Inserting at the beginning or middle forces Python to shift all subsequent packets
    # one position to the right in memory, resulting in linear performance (O(n)).
    # Inserting at the very end is much faster (O(1)) because no other elements require shifting.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Checks if the index falls within valid list boundaries to prevent an IndexError crash
    if 0 <= index < len(lst):
        # Pops out the telemetry packet at that specific index so it can be returned as processed
        removed_item = lst.pop(index)
        # Validating indices first is crucial because it stops invalid lookups from crashing
        # the program and handles unexpected edge cases gracefully.
        return removed_item
    # Returns None if the index is out of bounds to maintain safe and predictable behavior
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Loops through the signal buffer item by item using enumerate to track indices and values
    for idx, element in enumerate(lst):
        # Checks if the current packet matches the target error code being searched for
        if element == value:
            # Returns the index immediately upon finding a matching packet
            return idx
    # Returns -1 if the loop finishes without finding a match
    # This is a linear search because Python scans sequentially from left to right,
    # meaning the position of the packet is unknown ahead of time (O(n) time complexity).
    return -1


def main():
    print("UNIT 3: LIST OPERATIONS")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\nINSERTION TESTS")
    # Initializes a sample satellite telemetry buffer list with distinct hex packet strings
    signal_buffer = ["PKT-A10", "PKT-B22", "PKT-C33"]
    print(f"Original signal buffer: {signal_buffer}")

    # Inserts a high-priority emergency packet at index 0 (the front of the buffer)
    # Triggers a shift of all existing packet elements to the right, creating extra overhead.
    insert_at(signal_buffer, 0, "PKT-ERR-00")
    print(f"After inserting at the beginning: {signal_buffer}")

    # Inserts a diagnostic packet into the middle position of the buffer (index 2)
    insert_at(signal_buffer, 2, "PKT-MID-55")
    print(f"After inserting in the middle: {signal_buffer}")

    # Inserts a routine telemetry packet at the very end of the buffer using the current length as the index
    insert_at(signal_buffer, len(signal_buffer), "PKT-END-99")
    print(f"After inserting at the end: {signal_buffer}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\nDELETION TESTS")
    # Removes the first packet from the front of the buffer and captures the processed code
    popped_start = delete_at(signal_buffer, 0)
    print(f"Removed from beginning: {popped_start} | Updated list: {signal_buffer}")

    # Removes a packet from the calculated middle position of the buffer
    mid_idx = len(signal_buffer) // 2
    popped_mid = delete_at(signal_buffer, mid_idx)
    print(f"Removed from middle: {popped_mid} | Updated list: {signal_buffer}")

    # Removes the final telemetry packet from the end of the buffer
    popped_end = delete_at(signal_buffer, len(signal_buffer) - 1)
    print(f"Removed from end: {popped_end} | Updated list: {signal_buffer}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\nSEARCH TESTS")
    # Searches for an active packet that is confirmed to be in the buffer list
    target_found = "PKT-B22"
    found_index = search_value(signal_buffer, target_found)
    print(f"Searching for existing packet '{target_found}' found at index: {found_index}")

    # Searches for a packet code that is completely absent from the buffer
    target_missing = "PKT-XYZ-99"
    missing_index = search_value(signal_buffer, target_missing)
    print(f"Searching for missing packet '{target_missing}' returned: {missing_index}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\nEDGE CASES")
    # Edge Case 1: Tries to delete a packet using an out-of-bounds invalid index
    bad_index_result = delete_at(signal_buffer, 99)
    print(f"Edge Case 1 - Deleting with invalid index 99 returned: {bad_index_result} (List remains: {signal_buffer})")

    # Edge Case 2: Tests buffer operations on a brand new empty telemetry array
    empty_buffer = []
    print(f"Edge Case 2 - Empty buffer initialized: {empty_buffer}")

    # Inserts a packet into the empty buffer starting at index 0
    insert_at(empty_buffer, 0, "PKT-INIT")
    print(f"After inserting into empty buffer: {empty_buffer}")

    # Tries to delete using a negative out-of-bounds index
    negative_delete = delete_at(empty_buffer, -5)
    print(f"Trying to delete using a negative index returned: {negative_delete}")

if __name__ == "__main__":
    main()