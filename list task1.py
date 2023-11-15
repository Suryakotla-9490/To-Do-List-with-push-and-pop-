# Create a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Append an element to the list
my_list.append(6)
print("List after appending 6:", my_list)

# Append multiple elements to the list
my_list.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", my_list)

# Remove an element from the list by value
my_list.remove(4)
print("List after removing 4:", my_list)

# Remove an element from the list by index
removed_element = my_list.pop(1)
print(f"List after removing element at index 1 (removed element: {removed_element}):", my_list)