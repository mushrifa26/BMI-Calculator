import streamlit as st

# App title
st.title("🧮 BMI Calculator")

# User inputs
st.header("Enter Your Details")
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=65.0)
age = st.number_input("Age", min_value=1, max_value=120, value=21)
gender = st.radio("Gender", ("Male", "Female"))

# Calculate BMI
if st.button("Calculate BMI"):
    height_m = height / 100  # convert cm → meters
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI: {bmi:.2f}")

    # Interpretation
    if bmi < 18.5:
        st.warning("Underweight 😟 — You may need to gain some weight.")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal 👍 — Healthy weight range!")
    elif 25 <= bmi < 29.9:
        st.info("Overweight ⚠ — Consider lifestyle improvements.")
    else:
        st.error("Obese 🚨 — Health risk, consult a doctor.")

    # Show Ideal weight range
    min_wt = 18.5 * (height_m ** 2)
    max_wt = 24.9 * (height_m ** 2)
    st.write(f"✅ For your height, the ideal weight range is *{min_wt:.1f} kg - {max_wt:.1f} kg*.")