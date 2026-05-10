import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- STUDENT IDENTIFICATION ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.sidebar.markdown(f"""
### Developer Info
**Name:** Tanveer Hassan Khan  
**Roll Number:** 25-ME-111
""")

st.write(f"**Developer:** Tanveer Hassan Khan | **Roll No:** 25-ME-111")
st.divider()

# --- SECTION 1: UNIT CONVERTER ---
st.header("1. Mechanical Unit Converter")

category = st.selectbox("Select Category", ["Length", "Mass", "Pressure"])

if category == "Length":
    units = {"Meters": 1.0, "Kilometers": 1000.0, "Millimeters": 0.001, "Inches": 0.0254, "Feet": 0.3048}
elif category == "Mass":
    units = {"Kilograms": 1.0, "Grams": 0.001, "Pounds": 0.453592, "Newtons (Earth)": 0.10197}
elif category == "Pressure":
    units = {"Pascal": 1.0, "Bar": 100000.0, "PSI": 6894.76, "Atm": 101325.0}

col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Value", value=1.0)
    from_unit = st.selectbox("From", list(units.keys()))

with col2:
    to_unit = st.selectbox("To", list(units.keys()))
    # Conversion Logic: (Value * From_Factor) / To_Factor
    result = (value * units[from_unit]) / units[to_unit]
    st.metric("Result", f"{result:.4f} {to_unit}")

st.divider()

# --- SECTION 2: DENSITY CHECKER ---
st.header("2. Material Density Checker")

# Density data in kg/m^3
material_data = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Concrete": 2400,
    "Water": 1000,
    "Titanium": 4500,
    "Cast Iron": 7200
}

selected_material = st.selectbox("Select Material", list(material_data.keys()))
density = material_data[selected_material]

st.info(f"The density of **{selected_material}** is approximately **{density} kg/m³**.")

# Quick Calculation: Mass based on Volume
st.subheader("Quick Mass Calculator")
volume = st.number_input("Enter Volume (m³)", value=1.0, min_value=0.0)
calculated_mass = volume * density
st.success(f"Estimated Mass: {calculated_mass:,.2f} kg")
