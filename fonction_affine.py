import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title('Visualisation interactive d\'une fonction affine')

# Création des sliders pour ajuster la pente (a) et l'ordonnée à l'origine (b)
a = st.slider('Choisir la pente (a)', min_value=-10, max_value=10, value=1)
b = st.slider('Choisir l\'ordonnée à l\'origine (b)', min_value=-10, max_value=10, value=0)

# Générer un ensemble de valeurs x sur l'intervalle [-10, 10]
x = np.linspace(-10, 10, 100)

# Calculer les valeurs correspondantes de y = ax + b
y = a * x + b

# Créer le graphique de la fonction affine
fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}x + {b}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Ajouter un choix de couleur pour la courbe
couleur = st.color_picker('Choisir la couleur de la courbe', '#00f900')

# Créer le graphique avec des options de personnalisation
fig, ax = plt.subplots()
ax.plot(x, y, color=couleur, label=f'y = {a}x + {b}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graphique de la fonction affine')
ax.legend()

# Afficher le graphique personnalisé dans Streamlit
st.pyplot(fig)