import streamlit as st
import pandas as pd
import pickle
import time

# ---------------- LOAD MODEL & ENCODERS ----------------
model = pickle.load(open("rf_model.pkl", "rb"))
le_gender = pickle.load(open("le_gender.pkl", "rb"))
le_city = pickle.load(open("le_city.pkl", "rb"))
le_product = pickle.load(open("le_product.pkl", "rb"))
le_payment = pickle.load(open("le_payment.pkl", "rb"))
le_device = pickle.load(open("le_device.pkl", "rb"))

st.set_page_config(page_title="E-Commerce Predictor", layout="centered")

# --------- COLOR THEME ---------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
h1, h2, h3, label, span, p {
    color: #f1f5f9 !important;
}
div.stButton > button {
    background-color: #22c55e;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
div.stButton > button:hover {
    background-color: #16a34a;
    color: white;
}
div[data-baseweb="select"] > div {
    background-color: #1e293b;
    color: white;
}
input {
    background-color: #1e293b !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🛒 E-Commerce Purchase Amount Predictor")
st.subheader("Predict how much a customer will spend")

# ---- Layout ----
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", le_gender.classes_)
    city = st.selectbox("City", le_city.classes_)
    product = st.selectbox("Product Category", le_product.classes_)
    payment = st.selectbox("Payment Method", le_payment.classes_)
    device = st.selectbox("Device Type", le_device.classes_)
    age = st.number_input("Age", 1, 100, 25)
    unit_price = st.number_input("Unit Price", 0.0, 10000.0, 100.0)

with col2:
    quantity = st.number_input("Quantity", 1, value=1)
    discount_amount = st.number_input("Discount Amount", 0.0, value=0.0)
    session_duration = st.number_input("Session Duration (Minutes)", 1, value=10)
    pages_viewed = st.number_input("Pages Viewed", 1, value=5)
    is_returning = st.selectbox("Returning Customer", [0,1])
    delivery_days = st.number_input("Delivery Time (Days)", 1, value=3)
    customer_rating = st.slider("Customer Rating", 1, 5, 3)

# ---- Encode categorical inputs ----
gender = le_gender.transform([gender])[0]
city = le_city.transform([city])[0]
product = le_product.transform([product])[0]
payment = le_payment.transform([payment])[0]
device = le_device.transform([device])[0]

# ---- Create input DataFrame ----
input_df = pd.DataFrame([[age, gender, city, product, unit_price, quantity,
                          discount_amount, payment, device,
                          session_duration, pages_viewed, is_returning,
                          delivery_days, customer_rating]],
                        columns=[
                            'Age','Gender','City','Product_Category','Unit_Price','Quantity',
                            'Discount_Amount','Payment_Method','Device_Type',
                            'Session_Duration_Minutes','Pages_Viewed','Is_Returning_Customer',
                            'Delivery_Time_Days','Customer_Rating'
                        ])

# ---- Prediction with animation ----
if st.button("🚀 Predict Total Amount"):
    with st.spinner("🤖 Model is predicting..."):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        pred = model.predict(input_df)

    st.success(f"💰 Predicted Total Amount: ₹ {pred[0]:.2f}")
    st.balloons()