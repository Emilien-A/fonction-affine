import streamlit as st
import datanalyst  # Importe la page datanalyst.py
import fonction_affine  # Importe la page fonction_affine.py
import hello  # Importe la page hello.py

# Barre de navigation (menu)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisis une page :", ["Hello", "Fonction Affine", "Data Analyst"], index=0)

# Navigation entre les différentes pages
if page == "Hello":
    st.title("Page d'accueil - Hello")
    hello.app()  # Appelle la fonction principale dans hello.py

elif page == "Fonction Affine":
    st.title("Fonction Affine")
    fonction_affine.app()  # Appelle la fonction principale dans fonction_affine.py

elif page == "Data Analyst":
    st.title("Analyse de Données")
    datanalyst.app()  # Appelle la fonction principale dans datanalyst.py