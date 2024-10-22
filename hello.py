import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("Bienvenue dans mon projet Streamlit : Initiation")

    st.write("### Jeu de données")
    st.write("Je vais commencer avec quelques exercices pour manipuler des données. Je vais utiliser différents jeux de données, comme le dataset Titanic.")

    st.write("### Points à aborder")
    st.write("""
    - Visualisation interactive de la fonction affine avec Streamlit.
    - Création d'un outil d'analyse de données interactif avec Streamlit.
    """)

    st.write("### Aperçu des projets")
    st.markdown("""
    | Titre du projet                               | Détails                                                                                           |
    |-----------------------------------------------|---------------------------------------------------------------------------------------------------|
    | Visualisation interactive d'une fonction affine avec Streamlit | Objectif : Créer une visualisation dynamique et interactive de la fonction affine.               |
    |                                               | Fonctionnalités : Modifier la pente et l'ordonnée à l'origine, choisir la couleur de la courbe.  |
    |                                               | Bonus : Ajout de fonctionnalités supplémentaires comme les filtres et le téléchargement de fichiers. |
    |-----------------------------------------------|---------------------------------------------------------------------------------------------------|
    | Création d'un outil d'analyse de données interactif avec Streamlit | Objectif : Permettre l'analyse d'un fichier CSV avec visualisation des statistiques.             |
    |                                               | Fonctionnalités : Uploader un fichier CSV, sélectionner des colonnes, filtrer les données.       |
    |                                               | Bonus : Ajouter des graphiques pour une visualisation des données plus avancée.                 |
    """)

    # Exercice 1 : Analyse du Titanic
    st.write("## Exercice 1 : Analyse des données Titanic")
    st.write("Je télécharge le fichier CSV du Titanic pour commencer. Je vais explorer les données et générer des graphiques.")
    
    titanic_file = st.file_uploader("Télécharge le fichier Titanic", type=["csv"])
    
    if titanic_file is not None:
        titanic_data = pd.read_csv(titanic_file)
        st.write("Voici un aperçu des données Titanic :")
        st.dataframe(titanic_data.head())

        st.write("Statistiques descriptives des données Titanic :")
        st.write(titanic_data.describe())

        st.write("Graphique des survivants selon la classe :")
        fig, ax = plt.subplots()
        titanic_data.groupby('Pclass')['Survived'].sum().plot(kind='bar', ax=ax)
        plt.xlabel("Classe")
        plt.ylabel("Nombre de survivants")
        plt.title("Survivants par classe sur le Titanic")
        st.pyplot(fig)

    # Exercice 2 : Analyse d'un fichier CSV générique
    st.write("## Exercice 2 : Analyse de données CSV génériques")
    st.write("Je télécharge un autre fichier CSV pour explorer un nouveau jeu de données.")

    other_csv_file = st.file_uploader("Télécharge un fichier CSV", type=["csv"], key="other_csv")
    
    if other_csv_file is not None:
        other_data = pd.read_csv(other_csv_file)
        st.write("Aperçu des données :")
        st.dataframe(other_data.head())

        colonnes = st.multiselect('Je sélectionne les colonnes à afficher', options=other_data.columns.tolist(), default=other_data.columns.tolist())
        st.write(other_data[colonnes].head())

        st.write("Je sélectionne des colonnes pour un graphique simple :")
        x_colonne = st.selectbox('Colonne X', options=other_data.columns)
        y_colonne = st.selectbox('Colonne Y', options=other_data.columns)

        fig2, ax2 = plt.subplots()
        ax2.plot(other_data[x_colonne], other_data[y_colonne])
        plt.xlabel(x_colonne)
        plt.ylabel(y_colonne)
        st.pyplot(fig2)

    st.write("Ces exercices me permettent de manipuler des jeux de données. Je continue à explorer les autres sections dans le menu à gauche.")