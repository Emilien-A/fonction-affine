import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def app():
    st.write("## Visualisation interactive d'une fonction affine")
    st.write("Dans cet exercice, je peux modifier la pente et l'ordonnée à l'origine de la fonction affine, puis visualiser la courbe correspondante.")

    # Paramètres pour la fonction affine
    a = st.slider("Choisis la pente (a)", -10, 10, 1)
    b = st.slider("Choisis l'ordonnée à l'origine (b)", -10, 10, 0)
    color = st.color_picker("Choisis la couleur de la courbe", "#00f900")

    # Générer les données pour la fonction affine
    x = np.linspace(-10, 10, 100)
    y = a * x + b

    fig, ax = plt.subplots()
    ax.plot(x, y, color=color, label=f"y = {a}x + {b}")
    ax.set_title("Graphique de la fonction affine")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)