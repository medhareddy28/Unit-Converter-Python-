# unit_converter.py

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Welcome message
print("Welcome to Unit Converter (Celsius ↔ Fahrenheit)")
print("1. Celsius to Fahrenheit")     # Option 1
print("2. Fahrenheit to Celsius")     # Option 2

# Take user input for conversion choice
choice = input("Enter your choice (1 or 2): ")

# If user chooses Celsius to Fahrenheit
if choice == '1':
    c = float(input("Enter temperature in Celsius: "))  # Take Celsius input
    f = celsius_to_fahrenheit(c)                        # Convert to Fahrenheit
    print(f"{c}°C = {f:.2f}°F")                          # Print formatted result

# If user chooses Fahrenheit to Celsius
elif choice == '2':
    f = float(input("Enter temperature in Fahrenheit: "))  # Take Fahrenheit input
    c = fahrenheit_to_celsius(f)                           # Convert to Celsius
    print(f"{f}°F = {c:.2f}°C")                             # Print formatted result

# If user enters an invalid option
else:
    print("Invalid choice! Please enter 1 or 2.")
