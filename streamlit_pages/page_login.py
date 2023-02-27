import streamlit as st
import streamlit_authenticator as stauth
import yaml


def page_welcome_login():
    st.title("Prospicio - DS interface")

    with open('./secrets/st_credentials.yaml') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status:
        st.write(f"### You are logged in. Welcome {name} !")
        authenticator.logout("Logout", "main")

    elif not authentication_status:
        st.error("Username / password combination incorrect")

    elif authentication_status is None:
        st.warning("Please enter your username and password")

    st.write("## Utilisation de l'app")
    st.markdown("""Étapes à suivre : \n
    * définir les données sur la page 'Données' \n
    * choisir les paramètres du modèle \n
    * visualiser les résultats """)
