import streamlit as st
import pandas as pd

def app():
    st.title("Analyse de données CSV")
    st.write("Je télécharge un fichier CSV et j'explore ses données. Je peux afficher les colonnes, appliquer des filtres et visualiser des statistiques.")

    # Chargement du fichier CSV
    uploaded_file = st.file_uploader("Télécharge un fichier CSV", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Aperçu des données :")
        st.dataframe(data.head())

        # Afficher les statistiques descriptives
        st.write("### Statistiques descriptives")
        st.write(data.describe())

        # Sélectionner des colonnes à afficher
        colonnes = st.multiselect("Je sélectionne les colonnes à afficher", options=data.columns.tolist(), default=data.columns.tolist())
        st.write(data[colonnes].head())

        # Filtrage des données
        colonne_filtre = st.selectbox("Choisis une colonne pour filtrer", options=data.columns)
        valeur_filtre = st.text_input(f"Entrez la valeur à filtrer pour {colonne_filtre}")
        if valeur_filtre:
            data_filtre = data[data[colonne_filtre].astype(str).str.contains(valeur_filtre, na=False)]
            st.write(f"Résultats filtrés pour la valeur '{valeur_filtre}' dans la colonne {colonne_filtre} :")
            st.write(data_filtre)

        # Téléchargement des données filtrées
        if st.button("Télécharger les données filtrées"):
            csv = data_filtre.to_csv(index=False)
            st.download_button("Télécharger CSV", data=csv, file_name="donnees_filtrees.csv", mime="text/csv")