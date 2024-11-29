def temperature_converter(choice, value):
    if choice == '1':
        return f"{value}°C is equal to {celsius_to_fahrenheit(value):.2f}°F"
    elif choice == '2':
        return f"{value}°F is equal to {fahrenheit_to_celsius(value):.2f}°C"
    else:
        return "Invalid choice."

# Example usage
choice = '1'  # Replace with '2' for Fahrenheit to Celsius
value = 25    # Replace with any number
print(temperature_converter(choice, value))

