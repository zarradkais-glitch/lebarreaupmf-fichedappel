import streamlit as st
import unicodedata
import pandas as pd
import os

# Configuration de la page
st.set_page_config(
    page_title="Le Barreau | Plateforme Officielle de Recrutement",
    page_icon="⚖️",
    layout="centered"
)

# Design épuré, élégant et sombre
st.markdown("""
    <style>
    .stApp {
        background-color: #120F0D;
        color: #F5F2EF;
    }
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #E6D5C3;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #D4AF37 0%, #AA8225 100%);
        color: #120F0D;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button:hover {
        opacity: 0.95;
    }
    </style>
""", unsafe_allow_html=True)

# Fichier de sauvegarde locale pour la persistance des données
DATA_FILE = "recrutements_db.csv"

# Base de données initiale par défaut des candidats avec attribution équipe (POUR / CONTRE)
default_database = [
    { "name": "Mehdi Besbes", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Yasmine Ben Ali", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Yessine Bouchoucha", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Lydia Meddeb", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Kenza Smat", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Yasmine Oudi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Rahma Snoussi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Selim Darghouth", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Farah El Asmi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Nermine Maya Adhoum", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Zyne Zampol", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Yassine Albouchi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Ines Ben Naceur", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Farah Alaya", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Sohane Wawrzynowski", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },
    { "name": "Sarra Chaouch", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
    { "name": "Baya Hadj Ali", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Oui, il l'est encore", "presence": "Non pointé", "notes": {} },

    { "name": "Mehdi Zenkri", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Tasnim Louati", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Farah Borgi", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Bechir El Ouadhane", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Maher Ben Ouirane", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Nour Mahjoub", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Yasmine Kasraoui", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Salima Mourani", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Ramy Bouhamed", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Amine Ouerghi", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Yasmine Bousrour", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Lyne Naouali", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Sara Sancho", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Myriam Abbes", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Lina Hermassi", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Hosni Rahmatoallah", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Yasmine Mahjoub", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Sarra Khedher Behia", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} }
]

# Gestion du chargement et de la sauvegarde des données (Persistance automatique)
import json

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            db = []
            for _, row in df.iterrows():
                db.append({
                    "name": row["name"],
                    "session": row["session"],
                    "topic": row["topic"],
                    "date": row["date"],
                    "location": row["location"],
                    "judges": row["judges"],
                    "docName": row["docName"],
                    "team": row["team"],
                    "presence": row["presence"],
                    "notes": json.loads(row["notes"]) if pd.notna(row["notes"]) else {}
                })
            return db
        except Exception:
            return default_database
    return default_database

def save_data(db):
    df_list = []
    for c in db:
        df_list.append({
            "name": c["name"],
            "session": c["session"],
            "topic": c["topic"],
            "date": c["date"],
            "location": c["location"],
            "judges": c["judges"],
            "docName": c["docName"],
            "team": c["team"],
            "presence": c["presence"],
            "notes": json.dumps(c["notes"])
        })
    df = pd.DataFrame(df_list)
    df.to_csv(DATA_FILE, index=False)

if 'database' not in st.session_state:
    st.session_state.database = load_data()

def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower().strip()

# En-tête général du site
st.markdown("<h1 style='text-align: center;'>Le Barreau</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #A89F96; text-transform: uppercase; letter-spacing: 1px;'>Lycée Pierre Mendès France — Plateforme de Recrutement 2026</p>", unsafe_allow_html=True)
st.write("")

# Système d'onglets principaux (Espace Candidat vs Espace Bureau Exécutif)
tab_candidat, tab_bureau = st.tabs(["🎓 Espace Candidat", "🔒 Espace Bureau Exécutif"])

# ==========================================
# ONGLET 1 : ESPACE CANDIDAT
# ==========================================
with tab_candidat:
    if 'candidate_session' not in st.session_state:
        st.session_state.candidate_session = None

    if st.session_state.candidate_session is None:
        with st.form("login_form_cand"):
            st.markdown("### Connexion Candidat")
            st.write("Entrez vos prénom et nom exacts pour accéder aux détails de votre session.")
            
            full_name_input = st.text_input("Prénom et Nom", placeholder="")
            submitted_cand = st.form_submit_button("Accéder à mon espace")
            
            if submitted_cand:
                norm_input = normalize(full_name_input)
                found = next((c for c in st.session_state.database if normalize(c["name"]) == norm_input), None)
                
                if found:
                    st.session_state.candidate_session = found
                    st.rerun()
                else:
                    st.error("Nom introuvable. Veuillez vérifier l'orthographe ou contacter le bureau.")
    else:
        c = st.session_state.candidate_session
        
        st.markdown(f"### Bienvenue, {c['name']}")
        st.info(f"📍 **Numéro de session :** {c['session']} | 👥 **Équipe :** {c['team']}")
        
        st.write("---")
        
        st.markdown(f"**Sujet de session :** {c['topic']}")
        st.markdown(f"**Date et horaire :** {c['date']}")
        st.markdown(f"**Lieu exact :** {c['location']}")
        st.markdown(f"**Juges et évaluateurs :** {c['judges']}")
        st.markdown(f"**Équipe assignée :** {c['team']}")
        
        st.write("---")
        st.markdown("### 🎥 Ressources et Vidéos de Préparation")
        
        if "Session 1" in c['session']:
            st.markdown("**1. Vidéo de soutien (Facultatif) :** Support en plus pour enrichir vos connaissances générales et vous appuyer dessus pour le débat.")
            st.video("https://youtu.be/TEjAtdHGGNM?si=4qAr1RzkE1Qk2e1P")
        else:
            st.markdown("**1. Vidéo de soutien (Facultatif) :** Support en plus pour enrichir vos connaissances générales et vous appuyer dessus pour le débat.")
            st.video("https://youtu.be/-PqpU3n_W6s?si=YKhTSEaygUzsev_K")
            
        st.write("")
        st.markdown("**2. Vidéo méthode (Très conseillé) :** Destinée à comprendre comment fonctionne un débat juridique et structurer votre argumentation.")
        st.video("https://youtu.be/c4n3g2r_NAo?si=HJu0JM6ON41cHO2K")
        
        st.write("")
        if st.button("← Se déconnecter"):
            st.session_state.candidate_session = None
            st.rerun()

# ==========================================
# ONGLET 2 : ESPACE BUREAU EXÉCUTIF
# ==========================================
with tab_bureau:
    if 'bureau_user' not in st.session_state:
        st.session_state.bureau_user = None

    # Dictionnaire des accès autorisés du bureau
    bureau_accounts = {
        "Kaïs Zarrad": "KaisZarrad123pass",
        "Adam Chtourou": "AdamChtourou123pass",
        "Sarra Ben Mahmoud": "Secrétariat123pass",
        "Mayara Hamaoui": "Secrétariat123pass",
        "Nadia Sfia": "MadameSfia123pass"
    }

    if st.session_state.bureau_user is None:
        with st.form("login_form_bureau"):
            st.markdown("### 🔒 Connexion Bureau Exécutif & Prof. Référente")
            st.write("Réservé aux membres habilités du bureau.")
            
            selected_member = st.selectbox("Sélectionner votre profil", list(bureau_accounts.keys()))
            password_input = st.text_input("Mot de passe", type="password")
            submitted_bureau = st.form_submit_button("Connexion Bureau")
            
            if submitted_bureau:
                if password_input == bureau_accounts[selected_member]:
                    st.session_state.bureau_user = selected_member
                    st.rerun()
                else:
                    st.error("Mot de passe incorrect.")
    else:
        user_name = st.session_state.bureau_user
        st.success(f"Connecté en tant que : **{user_name}**")
        
        if st.button("Se déconnecter du Bureau"):
            st.session_state.bureau_user = None
            st.rerun()
            
        st.write("---")
        
        # Sous-navigation de l'espace bureau
        bureau_tab_eval, bureau_tab_teams, bureau_tab_ranking = st.tabs([
            "📝 Évaluations & Présences", 
            "⚙️ Gestion des Équipes & Sessions", 
            "🏆 Classement & Résultats (Top 25)"
        ])
        
        # ------------------------------------------
        # SOUS-ONGLET 1 : EVALUATIONS & PRESENCES
        # ------------------------------------------
        with bureau_tab_eval:
            st.markdown("### Gestion des Présences et Notation des Candidats")
            st.write("Chaque évaluateur note les 5 critères (sur 4 points chacun, total sur 20). Vos notes s'enregistrent et s'additionnent automatiquement.")
            
            selected_cand_name = st.selectbox("Choisir un candidat à évaluer", [c["name"] for c in st.session_state.database])
            cand_obj = next(c for c in st.session_state.database if c["name"] == selected_cand_name)
            
            # Gestion de la présence
            current_presence = cand_obj.get("presence", "Non pointé")
            presence_options = ["Non pointé", "Présent", "Absent"]
            new_presence = st.selectbox("Statut de présence", presence_options, index=presence_options.index(current_presence))
            if new_presence != current_presence:
                cand_obj["presence"] = new_presence
                save_data(st.session_state.database)
                st.success("Statut de présence mis à jour !")
            
            st.write(f"**Session :** {cand_obj['session']} | **Sujet :** {cand_obj['topic']} | **Équipe actuelle :** {cand_obj['team']}")
            st.write("---")
            
            # Formulaire de notation par évaluateur
            st.markdown(f"#### Grille de notation (Évaluateur : {user_name})")
            existing_notes = cand_obj["notes"].get(user_name, {"arg": 0, "ecoute": 0, "equipe": 0, "regles": 0, "langue": 0})
            
            with st.form(f"form_note_{selected_cand_name}"):
                arg = st.slider("1. Argumentation (sur 4)", 0, 4, int(existing_notes.get("arg", 0)))
                ecoute = st.slider("2. Écoute (sur 4)", 0, 4, int(existing_notes.get("ecoute", 0)))
                equipe = st.slider("3. Esprit d'équipe (sur 4)", 0, 4, int(existing_notes.get("equipe", 0)))
                regles = st.slider("4. Respect des règles (sur 4)", 0, 4, int(existing_notes.get("regles", 0)))
                langue = st.slider("5. Maîtrise de la langue (sur 4)", 0, 4, int(existing_notes.get("langue", 0)))
                
                submitted_notes = st.form_submit_button("Enregistrer mes notes")
                
                if submitted_notes:
                    cand_obj["notes"][user_name] = {
                        "arg": arg, "ecoute": ecoute, "equipe": equipe, "regles": regles, "langue": langue
                    }
                    save_data(st.session_state.database)
                    st.success("Notes enregistrées avec succès sur la plateforme !")
        
        # ------------------------------------------
        # SOUS-ONGLET 2 : GESTION DES EQUIPES & SESSIONS
        # ------------------------------------------
        with bureau_tab_teams:
            st.markdown("### ⚙️ Modification des détails et équipes (POUR / CONTRE)")
            st.write("Modifiez l'affectation des équipes ou les paramètres d'un candidat en temps réel.")
            
            mod_cand_name = st.selectbox("Sélectionner le candidat à modifier", [c["name"] for c in st.session_state.database], key="mod_select")
            mod_cand = next(c for c in st.session_state.database if c["name"] == mod_cand_name)
            
            with st.form("form_edit_candidate"):
                new_team = st.selectbox("Équipe", ["Oui...", "Non..."], index=0 if mod_cand["team"] == "Oui..." else 1)
                new_session = st.selectbox("Session", ["Session 1", "Session 2"], index=0 if mod_cand["session"] == "Session 1" else 1)
                
                submitted_mod = st.form_submit_button("Mettre à jour les informations")
                
                if submitted_mod:
                    mod_cand["team"] = new_team
                    mod_cand["session"] = new_session
                    if "Session 1" in new_session:
                        mod_cand["topic"] = "Est-ce que le droit international est encore légitime de nos jours ?"
                        mod_cand["docName"] = "Background Guide - Droit International"
                        mod_cand["judges"] = "Kaïs Zarrad et Adam Chtourou"
                    else:
                        mod_cand["topic"] = "Faut-il limiter la liberté d'expression en France ?"
                        mod_cand["docName"] = "Background Guide - Liberté d'Expression"
                        mod_cand["judges"] = "Sarra Ben Mahmoud et Mayara Hamaoui"
                        
                    save_data(st.session_state.database)
                    st.success(f"Modifications enregistrées pour {mod_cand['name']} !")
                    st.rerun()

        # ------------------------------------------
        # SOUS-ONGLET 3 : CLASSEMENT & RESULTATS (TOP 25)
        # ------------------------------------------
        with bureau_tab_ranking:
            st.markdown("### 🏆 Classement Général Automatique (Confidentiel)")
            st.write("La plateforme calcule automatiquement la moyenne générale de chaque candidat à partir de toutes les notes attribuées par les différents membres du bureau. Les 25 premiers sont automatiquement retenus.")
            
            ranking_data = []
            for c in st.session_state.database:
                evals = c["notes"]
                if evals:
                    total_scores = []
                    for evaluator, score_dict in evals.items():
                        s = score_dict.get("arg", 0) + score_dict.get("ecoute", 0) + score_dict.get("equipe", 0) + score_dict.get("regles", 0) + score_dict.get("langue", 0)
                        total_scores.append(s)
                    avg_score = sum(total_scores) / len(total_scores)
                else:
                    avg_score = 0.0
                
                ranking_data.append({
                    "Nom": c["name"],
                    "Session": c["session"],
                    "Équipe": c["team"],
                    "Présence": c["presence"],
                    "Moyenne (/20)": round(avg_score, 2),
                    "Évaluateurs ayant noté": len(evals)
                })
            
            df_rank = pd.DataFrame(ranking_data)
            df_rank = df_rank.sort_values(by="Moyenne (/20)", ascending=False).reset_index(drop=True)
            df_rank.index += 1 # Le classement commence à 1
            
            # Détermination des acceptés / refusés (Top 25)
            def get_status(idx):
                return "Accepté (Top 25)" if idx <= 25 else "Refusé"
            
            df_rank["Statut"] = [get_status(i) for i in df_rank.index]
            
            st.dataframe(df_rank, use_container_width=True)
            
            st.write("---")
            st.info("💡 **Rappel :** Ce classement est confidentiel et réservé exclusivement à l'affichage sur le canal du bureau exécutif.")

st.write("---")
st.markdown("<p style='text-align: center; color: #A89F96; font-size: 0.8rem;'>© 2026 Le Barreau — Lycée Pierre Mendès France, Tunis.</p>", unsafe_allow_html=True)
