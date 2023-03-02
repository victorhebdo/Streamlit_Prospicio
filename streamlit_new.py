import streamlit as st
import pandas as pd
import requests

# Make an API call
url = 'http://127.0.0.1:8000/predict'

df = pd.read_csv("data_streamlit.csv")

company = st.selectbox('Enter company name', df["name"])
if st.button("Predict"):
    data = df[df["name"] == company].iloc[0]

    params = {
                "country_code": data["country_code"],
                "employee_range": data["employee_range"],
                "min_revenues": data['min_revenues'],
                "traffic_monthly":data['traffic.monthly'],
                "industries_cleaned": ",".join([industry.strip(" '") for industry
                                                in data["industries_cleaned"].strip("{}").split(",")])
                }

    response = requests.get(url, params = params)
    data = response.json()["prediction"]
    if data == 1:
        st.success("The company is about to fundraise !")
    else:
        st.error("The company will not fundraise soon")
