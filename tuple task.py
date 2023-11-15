#Create a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Access elements in a tuple
print("Elements in the tuple:")
for element in my_tuple:
    print(element)

# Accessing elements by index
print("\nAccessing elements by index:")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("\nSlicing the tuple:")
sliced_tuple = my_tuple[1:4]
print("Sliced tuple:", sliced_tuple)

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated_tuple = tuple1 + tuple2
print("\nConcatenated tuple:", concatenated_tuple)

# Nested tuple
nested_tuple = ((1, 2), ("a", "b"), (3, "c"))
print("\nNested tuple:", nested_tuple)

# Unpacking a tuple
num1, num2, *rest = tuple1
print("\nUnpacking tuple:", "num1 =", num1, ", num2 =", num2, ", rest =", rest)
