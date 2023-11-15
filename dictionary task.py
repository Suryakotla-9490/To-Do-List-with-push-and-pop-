# Create a dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "grades": {"math": 90, "english": 85, "history": 88}
}

# Accessing values in the dictionary
print("Dictionary values:")
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])
print("Grades:", my_dict["grades"])

# Accessing nested values in the dictionary
print("\nAccessing nested values:")
print("Math grade:", my_dict["grades"]["math"])

# Modifying values in the dictionary
my_dict["age"] = 26
my_dict["grades"]["history"] = 90
#Adding a new key-value pair
my_dict["gender"] = "Male"

# Removing a key-value pair
del my_dict["grades"]["english"]

# Displaying the modified dictionary
print("\nModified Dictionary:")
print(my_dict)

# Iterating over keys and values in the dictionary
print("\nIterating over keys and values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
