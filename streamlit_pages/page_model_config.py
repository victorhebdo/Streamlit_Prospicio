
import streamlit as st
from app import config
#from app import models

from sklearn.model_selection import train_test_split

MODEL_TYPE = ["date", "value"]
MODEL_OPTIONS = ["RandomForrest", "LinearReg"]
SERIES_OPTIONS = ["Seed", "Series A", "Series B"]

def page_model():

    st.title("Choose model and parameters")

    st.write("## Main parameters")

    st.write("Data selected in previous page")
    prevision_type = st.selectbox("Prevision of : ", MODEL_TYPE)
    model_type = st.selectbox("Model : ", MODEL_OPTIONS)
    feature_series = st.selectbox("Series origin/feature : ", SERIES_OPTIONS)
    target_series = st.selectbox("Series target : ", SERIES_OPTIONS)

    test_split = st.number_input("Test split", value=0.2)



    fit_launch = st.button("Launch fit !")

    if fit_launch:
        # if st.session_state.get('df_pretreated_data', None) is None:
        #     st.warning("You must first select some data on the previous page !")

        # if st.session_state.get('evaluator_instance', None) is not None:
        #     st.info("You already fitted a model")

        model_data = DatasetModel(
                st.session_state['df_pretreated_data'],
                feature_fund=feature_series,
                target_fund=target_series,
                target_type=prevision_type,
                drop_cols=["Investor Names", "Lead Investors"],
                max_target_filter=50000000,
            )

        df_features, df_target, comp_names = (
            model_data.features,
            model_data.target,
            model_data.comp_names,
        )

        x_train, x_test, y_train, y_test, names_train, names_test = train_test_split(
            df_features, df_target, comp_names, test_size=test_split
        )


        st.success("Model was fitted !")

    st.write("## Config file content")
    for name, value in config.__dict__.items():
        if name[0].isupper():  # Select only caps starting variables => CONSTANTS
            st.text_input(label=name, value=value)
