# Importer les bibliothèques nécessaires
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le jeu de données avec Pandas
data = pd.read_csv('train.csv')

# 1. Afficher les données dans un tableau interactif
# Utilisation de st.dataframe pour afficher les données
st.dataframe(data)

# 2. Afficher les 10 premières lignes du jeu de données
# Utilisation de la fonction head() pour afficher les premières lignes
st.write(data.head(10))

# 3. Afficher les statistiques descriptives
# Utilisation de la fonction describe() pour obtenir des informations statistiques
st.write(data.describe())

# 4. Sélection des colonnes à afficher
# Multiselect permet à l'utilisateur de choisir les colonnes à afficher
colonnes = st.multiselect(
    'Sélectionnez les colonnes à afficher',  # Message pour l'utilisateur
    options=data.columns.tolist(),           # Liste des colonnes disponibles
    default=data.columns.tolist()            # Par défaut, toutes les colonnes sont sélectionnées
)

# 5. Afficher les colonnes sélectionnées
# Afficher les colonnes choisies par l'utilisateur dans un tableau interactif
st.write(data[colonnes].head(10))

# 6. Sélectionner deux colonnes pour la visualisation
# Utilisation de selectbox pour choisir deux colonnes pour un graphique scatterplot
x_colonne = st.selectbox('Sélectionnez la colonne pour l’axe X', options=data.columns)
y_colonne = st.selectbox('Sélectionnez la colonne pour l’axe Y', options=data.columns)

# 7. Créer un nuage de points avec Seaborn
# Utilisation de Matplotlib pour définir la figure et Seaborn pour tracer le scatterplot
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=x_colonne, y=y_colonne, ax=ax)

# Afficher le graphique dans Streamlit
st.pyplot(fig)

# 8. Filtrer les données par classe de passagers (Pclass)
# Selectbox pour choisir la classe et filtrer les données
pclass = st.selectbox('Sélectionnez la classe de passagers', options=data['Pclass'].unique())

# 9. Appliquer le filtre sur la classe sélectionnée
data_filtre = data[data['Pclass'] == pclass]

# 10. Afficher les données filtrées
st.write(data_filtre.head(10))

# 11. Télécharger les données filtrées en CSV
# Conversion du DataFrame filtré en CSV, puis utilisation d’un bouton de téléchargement
csv = data_filtre.to_csv(index=False)
st.download_button(
    label="Télécharger les données filtrées",  # Texte sur le bouton
    data=csv,                                  # Données à télécharger
    file_name='data_filtrée.csv',              # Nom du fichier
    mime='text/csv'                            # Type du fichier
)

# 12. Ajouter un choix de colonne pour la couleur dans le graphique
# Utilisation de selectbox pour choisir une colonne catégorielle pour définir la couleur (hue)
hue_colonne = st.selectbox('Sélectionnez une colonne pour la couleur', options=data.columns)

# 13. Sélectionner une palette de couleurs pour le graphique
# Choix parmi les palettes Seaborn disponibles
palette = st.selectbox('Sélectionnez la palette de couleurs', options=sns.palettes.SEABORN_PALETTES.keys())

# 14. Créer un nuage de points avec la palette sélectionnée et la colonne de couleur
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=x_colonne, y=y_colonne, hue=hue_colonne, palette=palette, ax=ax)

# 15. Afficher le graphique dans Streamlit
st.pyplot(fig)