def from_ascii_to_char():
    print("Welcome to the ASCII to Character Converter!")
    print("Enter a number between 33 and 126 to see its corresponding character.")
    print("To end the program, enter -1.")

    while True:
        try:
            num = input("Please provide a number (Enter -1 to end this program): ")
            number = int(num)

            if 33 <= number <= 126:
                print(f"The character for ASCII {number} is '{chr(number)}'.")
            elif number == -1:
                print("Thank you for using our program! Goodbye!")
                break
            else:
                print("Invalid number! Please enter a number between 33 and 126. To end the program, enter -1.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

from_ascii_to_char()
