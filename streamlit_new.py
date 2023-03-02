import streamlit as st
import requests

# Make an API call
url = 'http://127.0.0.1:8000/predict'

params = {
            "country_code": st.text_input('Country Code'),
            "employee_range": st.number_input('Employee Range'),
            "min_revenues": st.number_input('Revenue'),
            "traffic_monthly":st.number_input('Traffic Monthly'),
            "industries_cleaned": st.text_input('Industries')
            }

if st.button("Predict"):
    response = requests.get(url, params = params)
    data = response.json()["prediction"]
    if data == 1:
        st.success("The company is about to fundraise !")
    else:
        st.error("The company will not fundraise soon")
