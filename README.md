# 🛒 E-Commerce Sales & Customer Behavior Analysis

This project is a Machine Learning based web application that predicts the **Total Amount Spent by a customer** based on their personal details and browsing behavior. It helps understand how different customer factors influence purchasing decisions in an e-commerce platform.

The application is built using **Python**, **Machine Learning**, and **Streamlit**, and is deployed as a web app.

---

## 🚀 Features

- Predicts total purchase amount using a trained ML model  
- Interactive web interface using Streamlit  
- Uses real-world e-commerce features like:
  - Customer age and gender  
  - City and device type  
  - Product category and payment method  
  - Quantity and unit price  
  - Discount amount  
  - Session duration and pages viewed  
  - Customer rating  
  - Delivery time  
  - Returning customer status  

---

## 🧠 Machine Learning Model

- Algorithm used: **Random Forest Regressor**  
- Trained on e-commerce customer behavior dataset  
- Handles both numerical and categorical features  
- Label Encoding used for categorical variables  
- Model saved using Pickle for reuse in the web app  

---

## 🖥️ Web Application

The Streamlit app allows users to:
1. Enter customer details  
2. Select categorical values from dropdowns  
3. Click **Predict Total Amount**  
4. Get predicted purchase value instantly  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## 📁 Project Structure

```text
app.py
rf_model.pkl
le_city.pkl
le_device.pkl
le_gender.pkl
le_payment.pkl
le_product.pkl
requirements.txt
README.md


## Live Demo

Click the button below to launch the Streamlit app:

[![Launch App](https://img.shields.io/badge/Launch-App-brightgreen?style=for-the-badge&logo=streamlit)](https://e-commerce-sales-customer-behavior-analysis-nxmwkirajcnmxzmiel.streamlit.app/)
