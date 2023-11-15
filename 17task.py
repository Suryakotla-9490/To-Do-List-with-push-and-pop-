def copy_file_contents(input_file_name, output_file_name):
    try:
        # Open the first file for reading
        with open(input_file_name, 'r') as input_file:
            # Read the contents of the first file
            file_contents = input_file.read()

        # Open the second file for writing
        with open(output_file_name, 'w') as output_file:
            # Write the contents to the second file
            output_file.write(file_contents)

        print(f"Contents of '{input_file_name}' successfully copied to '{output_file_name}'.")
    except FileNotFoundError:
        print("File not found. Please check the file names and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for file names
input_file_name = input("Enter the name of the input text file: ")
output_file_name = input("Enter the name of the output text file: ")

# Call the function to copy file contents
copy_file_contents(input_file_name, output_file_name)