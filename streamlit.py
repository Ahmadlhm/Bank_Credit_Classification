import streamlit as st
import requests
from config import API_URL

st.title("Bank Credit Classification")

with st.form("add_form"):
    st.subheader("Type Features to predict the Credit Score!")
    Age = st.number_input("Age", step = 1 )
    Annual_Income = st.number_input("Annual_Income", step = 50)
    Monthly_Inhand_Salary = st.number_input("Monthly_Inhand_Salary", step = 50)
    Interest_Rate = st.number_input("Interest_Rate", step = 5)
    Credit_Mix = st.number_input("Credit_Mix", placeholder = "0 -> 'Bad', 1 -> 'Standard', 2 -> 'Good'", min_value = 0, max_value = 2, step = 1) 
    Outstanding_Debt = st.number_input("Outstanding_Debt", step = 50, min_value = 100)
    Credit_Utilization_Ratio = st.number_input("Credit_Utilization_Ratio", step = 5)
    Payment_of_Min_Amount_yes = st.number_input("Payment_of_Min_Amount_yes", placeholder = "1 -> 'Yes'", min_value = 0, max_value = 1, step = 1)
    Payment_of_Min_Amount_no = st.number_input("Payment_of_Min_Amount_no", placeholder = "1 -> 'No'", min_value = 0, max_value = 1, step = 1)
    Total_EMI_per_month = st.number_input("Total_EMI_per_month", step = 10)
    Monthly_Balance = st.number_input("Monthly_Balance", step = 10)
    if st.form_submit_button("Predict"):
            response = requests.post(API_URL, json={
                "features": [Age, Annual_Income,
                 Monthly_Inhand_Salary, Interest_Rate,
                 Outstanding_Debt,
                 Credit_Utilization_Ratio,Total_EMI_per_month,Monthly_Balance, Credit_Mix, Payment_of_Min_Amount_yes,
                 Payment_of_Min_Amount_no]
            })
            
        
            if response.status_code == 200:
                prediction = response.json().get("predicted_class", "No prediction returned")
                st.success(f"Predicted Credit Score: {prediction}")
            else:
                st.error(f"API Error: {response.status_code}")
            