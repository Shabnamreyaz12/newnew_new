import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    st.title("Temperature Converter")
    st.write("Convert temperatures between Celsius and Fahrenheit.")

    # Input for choosing conversion
    choice = st.selectbox("Choose conversion type:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    
    if choice == "Celsius to Fahrenheit":
        # Input for Celsius temperature
        celsius = st.number_input("Enter temperature in Celsius:", value=0.0, format="%.2f")
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == "Fahrenheit to Celsius":
        # Input for Fahrenheit temperature
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=0.0, format="%.2f")
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.write(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Run the Streamlit app
if __name__ == "__main__":
    temperature_converter()

