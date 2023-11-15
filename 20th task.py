class StringReverser:
    def reverse_words(self, input_string):
        # Split the input string into words
        words = input_string.split()

        # Reverse the order of the words
        reversed_words = words[::-1]

        # Join the reversed words to form the final string
        reversed_string = ' '.join(reversed_words)

        return reversed_string

# Example usage:
if __name__ == "__main__":
    reverser = StringReverser()

    # Take user input for a string
    input_string = input("Enter a string: ")

    # Reverse the string using the class method
    reversed_result = reverser.reverse_words(input_string)

    # Display the result
    print(f"The reversed string is: {reversed_result}")
