import streamlit as st
import bcrypt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connexion à Google Sheets pour stocker les utilisateurs
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Colocation Utilisateurs").sheet1

# Fonction de hachage et vérification du mot de passe
def crypt_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def inscrire_utilisateur(prenom, email, password):
    hashed_password = crypt_password(password)
    sheet.append_row([prenom, email, hashed_password.decode()])

def verifier_utilisateur(login, password):
    users = sheet.get_all_records()
    for user in users:
        if user['Prenom'] == login or user['Email'] == login:
            if check_password(password, user['Mot de passe']):
                return True
    return False

# Initialiser les colonnes du tableau Kanban pour les tâches
if 'kanban' not in st.session_state:
    st.session_state.kanban = {
        "À faire": [],
        "Fini": []
    }

# Fonction pour ajouter une tâche dans "À faire"
def ajouter_tache(tache):
    st.session_state.kanban["À faire"].append(tache)

# Fonction pour déplacer une tâche vers "Fini"
def deplacer_vers_fini(tache):
    st.session_state.kanban["À faire"].remove(tache)
    st.session_state.kanban["Fini"].append(tache)

# Menu de navigation
def afficher_menu():
    st.sidebar.title("Menu")
    menu_selection = st.sidebar.selectbox("Navigation", ["Accueil", "Tâches", "Paramètres", "Déconnexion"])

    if menu_selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil.")
    elif menu_selection == "Tâches":
        afficher_tableau_kanban()
    elif menu_selection == "Paramètres":
        st.write("Modifier les paramètres.")
    elif menu_selection == "Déconnexion":
        st.session_state.logged_in = False
        st.session_state.page = "connexion"
        st.write("Vous êtes déconnecté.")

# Tableau Kanban pour les tâches
def afficher_tableau_kanban():
    st.title("Tableau Kanban des tâches")

    # Ajouter une nouvelle tâche
    nouvelle_tache = st.text_input("Ajouter une tâche à votre binôme")
    if st.button("Ajouter tâche") and nouvelle_tache:
        ajouter_tache(nouvelle_tache)
        st.success(f"Tâche ajoutée : {nouvelle_tache}")

    # Afficher les tâches "À faire"
    st.subheader("À faire")
    for tache in st.session_state.kanban["À faire"]:
        if st.button(f"Marquer '{tache}' comme Fini", key=tache):
            deplacer_vers_fini(tache)

    # Afficher les tâches "Fini"
    st.subheader("Fini")
    for tache in st.session_state.kanban["Fini"]:
        st.write(tache)

# Navigation entre inscription et connexion
if 'page' not in st.session_state:
    st.session_state.page = "connexion"

if st.session_state.page == "connexion":
    st.subheader("Connexion")
    login = st.text_input("Entrez votre prénom ou email")
    password = st.text_input("Entrez votre mot de passe", type="password")
    
    if st.button("Connexion"):
        if verifier_utilisateur(login, password):
            st.session_state.logged_in = True
            st.session_state.page = "taches"
        else:
            st.error("Login ou mot de passe incorrect.")

    if st.button("Inscription"):
        st.session_state.page = "inscription"

elif st.session_state.page == "inscription":
    st.subheader("Inscription")
    prenom = st.text_input("Entrez votre prénom")
    email = st.text_input("Entrez votre email")
    password = st.text_input("Entrez votre mot de passe", type="password")
    
    if st.button("Je valide"):
        if prenom and email and password:
            inscrire_utilisateur(prenom, email, password)
            st.success(f"Compte créé pour {prenom}. Redirection vers la connexion.")
            st.session_state.page = "connexion"
        else:
            st.error("Veuillez remplir tous les champs.")

elif st.session_state.page == "taches":
    st.title("Calendrier des tâches")
    st.write("Bienvenue sur la page de gestion des tâches.")
    afficher_menu()