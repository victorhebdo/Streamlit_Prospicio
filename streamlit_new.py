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
    result = response.json()["prediction"]
    if result == 1:
        st.success("The company is about to fundraise !")
    else:
        st.error("The company will not fundraise soon")


    st.write("## Company Information")
    st.write(f"The information for **{company}** :")
    st.write("")
    st.write("### Administrative Data")
    st.write(f"- Country : **{data['country_code'].upper()}** ")
    industry_list = ', '.join([industry.strip(" '").replace("_", " ") for industry in data['industries_cleaned'].strip('{}').split(',')])
    st.write(f"- Industries : **{industry_list}**")
    st.write("### Financial Data")
    st.write("- Revenue: $1,234,567")
    st.write("- Net Income: $123,456")
