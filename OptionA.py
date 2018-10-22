# Course: CS 2302
# Author: Luis A. Gutierrez
# Lab 2: Option A
# Instructor: Diego Aguirre
# TA: Manoj Saha
# Purpose of Program: The purpose of this program is to merge two text files that contain employee IDs and
# merge them into a singly linked list. This program compares the list to find duplicate IDs. It also implements bubble
# sort and merge sort to sort the linked list in ascending order.


# Node class
class Node(object):
    item = -1
    next = None

    # Constructor method for Node class
    def __init__(self, item, next):
        self.item = item
        self.next = next


# Function to create a singly linked list from a single text file
def linked_list_from_1_file(f):
    file1 = open(f)
    head = None
    for line in file1:
        head = Node(int(line), head)
    return head


# Function to create a singly linked list from two text files
def linked_list_from_2_files(f1, f2):
    file1 = open(f1)
    file2 = open(f2)
    head = None  # when finished, will point to the last element in the file
    for line in file1:
        head = Node(int(line), head)

    for line in file2:
        head = Node(int(line), head)

    return head


# Function to print linked list
def print_list(head):
    # The list is empty
    if head is None:
        print("List is empty")
    else:
        # The list is not empty
        current = head
        while current is not None:
            print(current.item)
            current = current.next


# Function that compares every element in the list and returns a new linked list of the duplicates
def solution1(head):
    if head is None:
        print("Empty list")
    elif head.next is None:
        print("Only one item in the list. No possible duplicates in list")
    else:
        slow = head  # Keep track of current
        fast = head  # Used to compare to current(slow)

        duplicates_head = None

        while slow.next is not None:
            while fast is not None:
                if slow == fast:
                    fast = fast.next
                if slow.item == fast.item:  # If duplicate found, and not already seen, add to duplicates list
                    current = duplicates_head
                    in_list = False
                    while current is not None:  # Check if already added to duplicates list
                        if current.item == slow.item:
                            in_list = True
                        current = current.next
                    if not in_list:  # If not already in duplicates list, add it to the list as a new node
                        duplicates_head = Node(slow.item, duplicates_head)
                fast = fast.next
            fast = head
            slow = slow.next
        return duplicates_head


# Function that sorts linked list using Bubble Sort
def solution2(head):
    if head is None:
        return head
    elif head.next is None:
        return head
    else:
        a = head
        current = head.next
        to_compare = head
        temp = Node(-1, None)  # Used for the switch operation

        while a is not None:
            while current is not None:
                # If current is less than the item in the previous node, perform the switch operation
                if current.item < to_compare.item:
                    temp.item = to_compare.item
                    to_compare.item = current.item
                    current.item = temp.item
                current = current.next
                to_compare = to_compare.next
            to_compare = head
            current = head.next
            a = a.next
        return head


# Function that sorts a linked list using Merge Sort
def solution3(head):
    # Base case
    if head is None:
        return None
    if head.next is None:
        return head
    else:
        # Find middle of list
        middle = find_middle(head)
        # Set the head of the second half
        after_middle = middle.next
        # Separate both halves
        middle.next = None

        # Recursive call to divide the lists again
        left = solution3(head)
        right = solution3(after_middle)

        sorted_list = merge_and_sort_lists(left, right)
        return sorted_list


# Function that sorts and merges two lists (used for merge sort)
def merge_and_sort_lists(a, b):
    sorted_list = Node(-1, None)
    temp_head = sorted_list
    # Base case
    if a is None:
        sorted_list.next = b
    if b is None:
        sorted_list.next = a
    else:
        while a is not None or b is not None:
            if a is None:
                sorted_list.next = b
                b = b.next
            elif b is None:
                sorted_list.next = a
                a = a.next
            else:
                if a.item <= b.item:
                    sorted_list.next = a
                    a = a.next
                else:
                    sorted_list.next = b
                    b = b.next
            sorted_list = sorted_list.next
        sorted_list = temp_head.next  # Prevent -1 from being printed after the list has been sorted
    return sorted_list


# Function that finds the middle node of a singly linked list
def find_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        if fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        else:
            fast = fast.next
    return slow


# This function creates an array of size 0 to m where m is the largest ID found in the linked list "head"
def solution4(head):
    # If the list is empty
    if head is None:
        return None
    else:
        # Find the largest ID in the list to use as the size for the array
        largest_id = head.item
        current = head
        while current is not None:
            if current.item > largest_id:
                largest_id = current.item
            current = current.next

        # Fill the array with Booleans to see if that index has already been seen or not later
        seen = []
        for i in range(largest_id + 1):
            seen.append(False)  # Set False the indexes from 0 to the largest value in the list

        # Traverse the linked list and check if already ID has already been seen
        duplicates_list = None
        traverse = head

        while traverse is not None:
            # If seen for the first time, set the index at the same ID to True
            if seen[traverse.item] is False:
                seen[traverse.item] = True
            # Add value that is duplicate to duplicates list if not already in list, else don't add
            else:
                traverse_duplicates = duplicates_list
                in_list = False
                # Traverse duplicates list to check if already added to the duplicates list
                while traverse_duplicates is not None:
                    if traverse.item == traverse_duplicates.item:
                        in_list = True
                    traverse_duplicates = traverse_duplicates.next
                # If haven't added yet, add it to the list
                if not in_list:
                    duplicates_list = Node(traverse.item, duplicates_list)
            traverse = traverse.next
        return duplicates_list


def main():
    # Linked list from both files
    head = linked_list_from_2_files("activision.txt", "vivendi.txt")

    # Test solution1
    print("-----Testing solution1-----")
    print_list(solution1(head))
    print("-----End Test-----")

    # Test solution2
    print("-----Testing solution2-----")
    print_list(solution2(head))
    print("-----End Test-----")

    # Test solution3
    print("-----Testing solution3-----")
    print_list(solution3(head))
    print("-----End Test-----")

    # Test solution4
    print("-----Testing solution4-----")
    print_list(solution4(head))
    print("-----End Test-----")


main()
