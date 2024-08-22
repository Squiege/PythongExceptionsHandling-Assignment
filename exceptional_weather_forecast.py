# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

user_input = input("What temperature is it outside in Fahrenheit?")

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius.
# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that 
# this message is displayed regardless of whether an exception was caught or not.

def temp_conversion(user_input):
    try:
        user_input = int(user_input)
        celsius = (user_input - 32) * 5 / 9
    except ValueError:
        print("Please enter a temperature as an integer")
    except Exception as e:
        print(f"An error has occurred: {e}")
    else:
        print(f"{user_input} degree's Fahrenheit is {celsius} degree's Celsius")
    finally:
        print("Thank you for using Devin's Weather Converter")

temp_conversion(user_input)
