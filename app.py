import streamlit as st

    # PRESSURE
    elif conversion_type == "Pressure":
        value = st.number_input("Enter value in Pascal", min_value=0.0)

        kpa = value / 1000
        bar = value / 100000
        psi = value * 0.000145038

        st.success(f"Kilopascal: {kpa:.2f} kPa")
        st.success(f"Bar: {bar:.4f} bar")
        st.success(f"PSI: {psi:.4f} psi")

    # TEMPERATURE
    elif conversion_type == "Temperature":
        value = st.number_input("Enter temperature in Celsius")

        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15

        st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
        st.success(f"Kelvin: {kelvin:.2f} K")

    # WEIGHT
    elif conversion_type == "Weight":
        value = st.number_input("Enter weight in kilograms", min_value=0.0)

        grams = value * 1000
        pounds = value * 2.20462

        st.success(f"Grams: {grams:.2f} g")
        st.success(f"Pounds: {pounds:.2f} lb")

# -----------------------------
# MATERIAL DENSITY CHECKER
# -----------------------------
elif menu == "Material Density Checker":

    st.header("Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Cast Iron": 7200
    }

    material = st.selectbox("Select Material", list(materials.keys()))

    density = materials[material]

    st.info(f"Density of {material}: {density} kg/m³")

    volume = st.number_input("Enter Volume in m³", min_value=0.0)

    mass = density * volume

    st.success(f"Estimated Mass: {mass:.2f} kg")

st.write("---")
st.caption("Developed using Streamlit")
