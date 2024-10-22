import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    # Introduction
    st.markdown("![Titanic](https://www.link-to-titanic-image.com)")
    st.markdown("# Bienvenue à mon projet Titanic! 🛳️")
    st.markdown("Dans cette application, je vais explorer les données du célèbre Titanic et visualiser plusieurs aspects importants des passagers.")
    
    # Charger directement le fichier Titanic depuis un chemin local
    # Assure-toi que le fichier 'train.csv' est dans le même répertoire que ton projet ou spécifie un chemin absolu
    titanic_data = pd.read_csv('train.csv')
    
    st.write("Voici un aperçu des données Titanic :")
    st.dataframe(titanic_data.head())

    # Statistiques descriptives
    st.write("### Statistiques descriptives")
    st.write(titanic_data.describe())

    # Filtrage des classes
    st.markdown("### Filtrage des passagers par classe 🛳️")
    classe = st.selectbox('Sélectionne une classe de passagers', titanic_data['Pclass'].unique())
    data_classe = titanic_data[titanic_data['Pclass'] == classe]
    st.write(data_classe.head())

    # Graphique des survivants
    st.write("### Visualisation des survivants par classe et sexe")
    fig, ax = plt.subplots()
    sns.barplot(x='Pclass', y='Survived', hue='Sex', data=titanic_data, ax=ax)
    plt.xlabel("Classe")
    plt.ylabel("Taux de survie")
    plt.title("Taux de survie selon la classe et le sexe")
    st.pyplot(fig)

    # Filtrage par âge
    st.markdown("### Filtrage des passagers par tranche d’âge")
    age_min, age_max = st.slider('Sélectionnez une tranche d’âge', int(titanic_data['Age'].min()), int(titanic_data['Age'].max()), (20, 50))
    data_age = titanic_data[(titanic_data['Age'] >= age_min) & (titanic_data['Age'] <= age_max)]
    st.write(data_age.head())

    # Téléchargement des données filtrées
    csv = data_classe.to_csv(index=False)
    st.download_button(
        label="Télécharger les données filtrées",
        data=csv,
        file_name='titanic_data_classe.csv',
        mime='text/csv',
    )