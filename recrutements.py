import streamlit as st
import unicodedata
import pandas as pd
import os
import json

# Configuration de la page
st.set_page_config(
    page_title="Le Barreau | Haute Instance & Recrutement",
    page_icon="⚖️",
    layout="centered"
)

# Design de Luxe : Noir Profond, Or Impérial et Ivoire
st.markdown("""
    <style>
    /* Fond général de l'application */
    .stApp {
        background-color: #0B0B0C;
        color: #EAE5DE;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Titres prestigieux */
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #F3EFEA;
        font-weight: normal;
        letter-spacing: 0.5px;
    }
    
    /* Conteneurs de formulaires et blocs style "Carte de Luxe" */
    div.stForm, div.row-widget.stHorizontal, div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        background-color: #141416;
        border: 1px solid #2A2826;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* Boutons de luxe dorés ultra-lisibles */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #DFB15B 0%, #C59B37 100%);
        color: #0B0B0C !important;
        font-family: 'Georgia', serif;
        font-weight: bold;
        letter-spacing: 1px;
        border: none;
        border-radius: 6px;
        padding: 12px 20px;
        text-transform: uppercase;
        font-size: 0.85rem;
        box-shadow: 0 4px 15px rgba(197, 155, 55, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #EFC36D 0%, #D4AF37 100%);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        transform: translateY(-1px);
    }
    
    /* Champs de saisie élégants */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #1A1A1D !important;
        color: #F3EFEA !important;
        border: 1px solid #332F2B !important;
        border-radius: 6px !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #C59B37 !important;
        box-shadow: 0 0 8px rgba(197, 155, 55, 0.3) !important;
    }

    /* Onglets de navigation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #141416;
        border-radius: 6px;
        color: #A89F96;
        border: 1px solid #2A2826;
        padding: 10px 20px;
        font-family: 'Georgia', serif;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1F1D1A 0%, #141416 100%);
        color: #DFB15B !important;
        border-color: #C59B37 !important;
    }
    
    /* Lignes de séparation dorées */
    hr {
        border-color: #2A2826;
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
    { "name": "Sarra Chaouach", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International", "team": "Non, il ne l'est plus", "presence": "Non pointé", "notes": {} },
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
    { "name": "Rahma Hosni", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Yasmine Mahjoub", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
    { "name": "Behia Sarra Khedher", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} },
    { "name": "Sofia Zouari", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Non, il ne faut pas", "presence": "Non pointé", "notes": {} }
    { "name": "Maya Aissa", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression", "team": "Oui, il faut", "presence": "Non pointé", "notes": {} },
]

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

# En-tête majestueux
st.markdown("<h1 style='text-align: center; color: #DFB15B; font-weight: normal; letter-spacing: 2px;'>LE BARREAU</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8C8279; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem;'>Lycée Pierre Mendès France — Session de Recrutement 2026</p>", unsafe_allow_html=True)
st.write("")

# Système d'onglets principaux
tab_candidat, tab_bureau = st.tabs(["🎓 Espace Candidat", "🔒 Espace Bureau Exécutif"])

# ==========================================
# ONGLET 1 : ESPACE CANDIDAT
# ==========================================
with tab_candidat:
    if 'candidate_session' not in st.session_state:
        st.session_state.candidate_session = None

    if st.session_state.candidate_session is None:
        with st.form("login_form_cand"):
            st.markdown("<h3 style='color: #DFB15B; font-size: 1.2rem;'>Identification Candidat</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color: #A89F96; font-size: 0.9rem;'>Veuillez entrer vos prénom et nom exacts pour accéder à votre convocation.</p>", unsafe_allow_html=True)
            
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
        
        st.markdown(f"<h2 style='color: #DFB15B;'>Bienvenue, {c['name']}</h2>", unsafe_allow_html=True)
        st.info(f"📍 **Session :** {c['session']} &nbsp;|&nbsp; ⚖️ **Affectation d'équipe :** {c['team']}")
        
        st.write("---")
        
        st.markdown(f"**Sujet de plaidoirie :** {c['topic']}")
        st.markdown(f"**Date et horaire :** {c['date']}")
        st.markdown(f"**Lieu :** {c['location']}")
        st.markdown(f"**Membres du jury :** {c['judges']}")
        
        st.write("---")
        st.markdown("<h3 style='color: #DFB15B; font-size: 1.1rem;'>Ressources Pédagogiques</h3>", unsafe_allow_html=True)
        
        if "Session 1" in c['session']:
            st.markdown("**1. Document de soutien (Facultatif) :**")
            st.video("https://youtu.be/TEjAtdHGGNM?si=4qAr1RzkE1Qk2e1P")
        else:
            st.markdown("**1. Document de soutien (Facultatif) :**")
            st.video("https://youtu.be/-PqpU3n_W6s?si=YKhTSEaygUzsev_K")
            
        st.write("")
        st.markdown("**2. Guide méthodologique de l'art oratoire :**")
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

    bureau_accounts = {
        "Kaïs Zarrad - co-président": "K9#zL$mP2!qR8v",
        "Adam Chtourou - co-président": "Ad9$xK3#wY5!tN",
        "Mayara Hamaoui - Cheffe communication": "My7*bH2!eD4#sQ",
        "Sarra Ben Mahmoud - Cheffe média": "Sr5#nM8!aF6$pW",
        "Madame Sfia - prof référente": "Sf9!rP4#tV2$jK"
    }

    if st.session_state.bureau_user is None:
        with st.form("login_form_bureau"):
            st.markdown("<h3 style='color: #DFB15B; font-size: 1.2rem;'>Sécurité Bureau Exécutif</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color: #A89F96; font-size: 0.9rem;'>Accès strictement réservé aux membres accrédités.</p>", unsafe_allow_html=True)
            
            selected_member = st.selectbox("Sélectionner votre profil", list(bureau_accounts.keys()))
            password_input = st.text_input("Mot de passe sécurisé", type="password")
            submitted_bureau = st.form_submit_button("Connexion Sécurisée")
            
            if submitted_bureau:
                if password_input == bureau_accounts[selected_member]:
                    st.session_state.bureau_user = selected_member
                    st.rerun()
                else:
                    st.error("Mot de passe incorrect.")
    else:
        user_name = st.session_state.bureau_user
        st.success(f"Connecté avec accréditation : **{user_name}**")
        
        if st.button("Fermer la session Bureau"):
            st.session_state.bureau_user = None
            st.rerun()
            
        st.write("---")
        
        bureau_tab_eval, bureau_tab_teams, bureau_tab_ranking = st.tabs([
            "📝 Évaluations & Pointage", 
            "⚙️ Gestion des Sessions", 
            "🏆 Classement Officiel (Top 25)"
        ])
        
        # ------------------------------------------
        # SOUS-ONGLET 1 : EVALUATIONS & PRESENCES
        # ------------------------------------------
        with bureau_tab_eval:
            st.markdown("### Grille d'Évaluation Collaborative")
            st.write(f"Évaluateur actif : **{user_name}**. Modifiez directement les présences et les notes, puis validez.")
            
            session_filter = st.selectbox("Filtrer par session", ["Toutes les sessions", "Session 1", "Session 2"])
            
            filtered_candidates = st.session_state.database
            if session_filter != "Toutes les sessions":
                filtered_candidates = [c for c in st.session_state.database if c["session"] == session_filter]
            
            table_data = []
            for c in filtered_candidates:
                existing_notes = c["notes"].get(user_name, {"arg": 0, "ecoute": 0, "equipe": 0, "regles": 0, "langue": 0})
                table_data.append({
                    "Nom": c["name"],
                    "Session": c["session"],
                    "Présence": c.get("presence", "Non pointé"),
                    "Argumentation (/4)": int(existing_notes.get("arg", 0)),
                    "Écoute (/4)": int(existing_notes.get("ecoute", 0)),
                    "Esprit d'équipe (/4)": int(existing_notes.get("equipe", 0)),
                    "Respect des règles (/4)": int(existing_notes.get("regles", 0)),
                    "Maîtrise de la langue (/4)": int(existing_notes.get("langue", 0))
                })
            
            df_editable = pd.DataFrame(table_data)
            
            edited_df = st.data_editor(
                df_editable,
                column_config={
                    "Nom": st.column_config.TextColumn("Candidat", disabled=True),
                    "Session": st.column_config.TextColumn("Session", disabled=True),
                    "Présence": st.column_config.SelectboxColumn("Présence", options=["Non pointé", "Présent", "Absent"], required=True),
                    "Argumentation (/4)": st.column_config.NumberColumn("Arg (/4)", min_value=0, max_value=4, step=1),
                    "Écoute (/4)": st.column_config.NumberColumn("Écoute (/4)", min_value=0, max_value=4, step=1),
                    "Esprit d'équipe (/4)": st.column_config.NumberColumn("Équipe (/4)", min_value=0, max_value=4, step=1),
                    "Respect des règles (/4)": st.column_config.NumberColumn("Règles (/4)", min_value=0, max_value=4, step=1),
                    "Maîtrise de la langue (/4)": st.column_config.NumberColumn("Langue (/4)", min_value=0, max_value=4, step=1),
                },
                use_container_width=True,
                hide_index=True,
                key="editor_grades"
            )
            
            if st.button("💾 Enregistrer les notes et présences"):
                for _, row in edited_df.iterrows():
                    c_obj = next(c for c in st.session_state.database if c["name"] == row["Nom"])
                    c_obj["presence"] = row["Présence"]
                    if user_name not in c_obj["notes"]:
                        c_obj["notes"][user_name] = {}
                    c_obj["notes"][user_name] = {
                        "arg": int(row["Argumentation (/4)"]),
                        "ecoute": int(row["Écoute (/4)"]),
                        "equipe": int(row["Esprit d'équipe (/4)"]),
                        "regles": int(row["Respect des règles (/4)"]),
                        "langue": int(row["Maîtrise de la langue (/4)"])
                    }
                save_data(st.session_state.database)
                st.success("Enregistrement effectué avec succès !")

        # ------------------------------------------
        # SOUS-ONGLET 2 : GESTION DES EQUIPES
        # ------------------------------------------
        with bureau_tab_teams:
            st.markdown("### Paramétrage des Candidats")
            
            mod_cand_name = st.selectbox("Sélectionner un candidat", [c["name"] for c in st.session_state.database], key="mod_select")
            mod_cand = next(c for c in st.session_state.database if c["name"] == mod_cand_name)
            
            with st.form("form_edit_candidate"):
                new_team = st.text_input("Équipe assignée", value=mod_cand["team"])
                new_session = st.selectbox("Session", ["Session 1", "Session 2"], index=0 if mod_cand["session"] == "Session 1" else 1)
                
                submitted_mod = st.form_submit_button("Mettre à jour le dossier")
                
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
                    st.success(f"Mise à jour validée pour {mod_cand['name']} !")
                    st.rerun()

        # ------------------------------------------
        # SOUS-ONGLET 3 : CLASSEMENT & RESULTATS
        # ------------------------------------------
        with bureau_tab_ranking:
            st.markdown("### Classement Général & Sélection du Top 25")
            st.write("Synthèse automatique des notes consolidées de l'ensemble des membres du bureau.")
            
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
                    "Évaluateurs": len(evals)
                })
            
            df_rank = pd.DataFrame(ranking_data)
            df_rank = df_rank.sort_values(by="Moyenne (/20)", ascending=False).reset_index(drop=True)
            df_rank.index += 1
            
            def get_status(idx):
                return "Sélectionné (Top 25)" if idx <= 25 else "Non retenu"
            
            df_rank["Statut"] = [get_status(i) for i in df_rank.index]
            
            st.dataframe(df_rank, use_container_width=True)

st.write("---")
st.markdown("<p style='text-align: center; color: #554F49; font-size: 0.75rem; letter-spacing: 1px;'>LE BARREAU — LYCÉE PIERRE MENDÈS FRANCE</p>", unsafe_allow_html=True)
