import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    return value * conversion_dict[from_unit] / conversion_dict[to_unit]

st.title("Unit Converter")

category = st.selectbox("Choose a category", ["Length", "Weight", "Temperature"])

if category == "Length":
    units = {"Meter": 1.0, "Kilometer": 1000, "Centimeter": 0.01, "Mile": 1609.34, "Foot": 0.3048}
elif category == "Weight":
    units = {"Gram": 1.0, "Kilogram": 1000, "Pound": 453.592, "Ounce": 28.3495}
elif category == "Temperature":
    units = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", list(units.keys()))
with col2:
    to_unit = st.selectbox("To", list(units.keys()))
value = st.number_input("Enter the value", min_value=0.0)

if st.button("Convert", use_container_width=True):
    if category != "Temperature":
        result = convert_units(value, from_unit, to_unit, units)
    else:
        # Temperature conversion logic
        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32

    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")