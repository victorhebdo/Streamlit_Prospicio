import streamlit as st
import io

#from app import config

def page_data():
    st.title("Choose data source")

    if st.session_state.get('df_pretreated_data', None) is not None:
        st.info("Some Data is already loaded.")

    st.write("## CSV File")
    csv_file = st.file_uploader(
        "Upload the data as csv",
        type=["csv"],
    )

    if csv_file:

        crunch_data = (#MODEL TO PUT(
            filepath=io.StringIO(csv_file.read().decode("utf-8")),
            necessary_col_list=config.SELECTED_COLS,
            category_threshold=5,
        )

        df_pretreated = crunch_data.df_pretreated
        st.session_state['df_pretreated_data']= df_pretreated
        st.success("Data is ready !")

    st.write("## AirTable - SQL?")
