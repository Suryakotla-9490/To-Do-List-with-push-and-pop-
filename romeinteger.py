class IntegerToRoman:
    def __init__(self):
        self.numeral_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert(self, num):
        if not (0 < num < 4000):
            raise ValueError("Input must be an integer between 1 and 3999")

        result = ''
        for value, numeral in sorted(self.numeral_map.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result


# Example usage:
if __name__ == "__main__":
    converter = IntegerToRoman()

    try:
        # Take user input for an integer
        num_input = int(input("Enter an integer (1 to 3999): "))

        # Convert the integer to a Roman numeral
        result = converter.convert(num_input)

        # Display the result
        print(f"The Roman numeral representation of {num_input} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
