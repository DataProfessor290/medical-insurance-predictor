import streamlit as st
import pandas as pd
import joblib

# =============================
# 🎯 App Config
# =============================
st.set_page_config(
    page_title="Medical Insurance Charge Predictor",
    page_icon="💊",
    layout="centered",
)

# =============================
# Load Model
# =============================
model = joblib.load("Medical Insurance RF Model.joblib")

# =============================
# 🏥 App Title
# =============================
st.title("💊 Medical Insurance Charge Predictor")
st.write("Enter patient details below to estimate **medical insurance charges** using a Random Forest model.")

st.divider()

# =============================
# 📥 User Inputs
# =============================
age = st.number_input("Age", min_value=0, max_value=100, value=30)

sex = st.selectbox("Sex", ["Male", "Female"])   # raw string (pipeline encodes)

# --- BMI Options ---
st.subheader("⚖️ BMI Information")
bmi_option = st.radio("Do you know your BMI?", ["Yes, I know my BMI", "No, calculate my BMI"])

if bmi_option == "Yes, I know my BMI":
    bmi = st.number_input("Enter your BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
else:
    st.caption("💡 Enter your weight in kilograms (e.g., 65.0)")
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1, format="%.2f")

    st.caption("💡 Enter your height in meters (e.g., 1.75)")
    height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01, format="%.2f")

    if height > 0:
        bmi = round(weight / (height ** 2), 2)
        st.success(f"📏 Your calculated BMI is: **{bmi}**")

        # WHO Classification
        if bmi < 18.5:
            st.warning("⚠️ Classification: Underweight")
        elif bmi < 25:
            st.success("✅ Classification: Normal")
        elif bmi < 30:
            st.warning("⚠️ Classification: Overweight")
        elif bmi < 35:
            st.error("🚨 Classification: Obese Class I")
        elif bmi < 40:
            st.error("🚨 Classification: Obese Class II")
        else:
            st.error("🚨 Classification: Obese Class III")
    else:
        bmi = 25.0  # Default safe value if no input yet

children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

smoker = st.selectbox("Smoker", ["Yes", "No"])  # raw string (pipeline encodes)

region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])  # raw string (pipeline encodes)

# =============================
# 🔮 Predict Button
# =============================
if st.button("🔮 Predict Charges"):
    # Make sure column names match training
    input_data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }])

    prediction = model.predict(input_data)[0]
    
    # Format as Nigerian Naira (₦)
    st.success(f"💰 Estimated Insurance Charges: **₦{prediction:,.2f}**")

    # =============================
    # 🌍 Currency Conversion
    # =============================
    usd_rate = 1540
    gbp_rate = 2087
    eur_rate = 1802

    usd = round(prediction / usd_rate, 2)
    gbp = round(prediction / gbp_rate, 2)
    eur = round(prediction / eur_rate, 2)

    st.write("### 🌍 Converted Amounts")
    st.info(f"""
    - 🇺🇸 USD: **${usd:,.2f}**  
    - 🇬🇧 GBP: **£{gbp:,.2f}**  
    - 🇪🇺 EUR: **€{eur:,.2f}**  
    """)

    # =============================
    # 🩺 Personalized Health Insights
    # =============================
    st.subheader("🩺 Personalized Health Insights")

    if bmi < 18.5:
        st.warning("⚠️ You are underweight. Consider a nutrition plan to reach a healthy weight.")
    elif bmi < 25:
        st.success("✅ Your BMI is in the normal range. Keep up the good lifestyle!")
    elif bmi < 30:
        st.warning("⚠️ You are overweight. Consider regular exercise and a balanced diet.")
    else:
        st.error("🚨 You are in the obese range. Medical consultation is strongly advised.")

    if smoker == "Yes":
        st.error("🚭 Smoking significantly increases insurance premiums and health risks. Quitting will lower future costs.")

    # =============================
    # 📊 Insurance Premium Ranges in Nigeria
    # =============================
    st.subheader("📊 Insurance Premium Ranges in Nigeria")

    st.markdown("""
    - **₦3,500 – ₦20,000/year** → Basic/Low-cost (outpatient, telemedicine, essential care)  
    - **₦20,000 – ₦50,000/year** → Entry to Mid-level (some inpatient, emergency, diagnostics)  
    - **₦50,000 – ₦150,000+/year** → Comprehensive (inpatient, surgeries, maternity, specialist care)  
    """)

    if prediction < 20000:
        st.info("💡 Your estimated premium falls in the **low-cost/basic range**.")
    elif prediction < 50000:
        st.info("💡 Your estimated premium is in the **entry to mid-level range**.")
    else:
        st.info("💡 Your estimated premium is in the **comprehensive/high coverage range**.")

# =============================
# 📝 Footer
# =============================
st.markdown("---")
st.markdown(
    """
    <div style="font-size: 13px; color: #999999; text-align: center;">
        Built with ❤️ using <a href="https://streamlit.io" target="_blank" style="color: #1f77b4;">Streamlit</a><br>
        Based on WHO BMI classification<br><br>
        Created by <strong>Tolulope Emuleomo</strong> aka <strong>Data Professor</strong> 🧠<br>
        🔗 <a href="https://twitter.com/dataprofessor_" target="_blank" style="color: #1DA1F2;">@dataprofessor_</a> |
        <a href="https://github.com/dataprofessor290" target="_blank" style="color: #6e5494;">GitHub</a><br>
        💼 <span style="color: #cccccc;">Data Scientist</span>
    </div>
    """,
    unsafe_allow_html=True
)
