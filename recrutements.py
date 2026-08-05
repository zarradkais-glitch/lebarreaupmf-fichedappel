import streamlit as st
import unicodedata

# Configuration de la page
st.set_page_config(
    page_title="Espace Candidat | Le Barreau - PMF",
    page_icon="⚖️",
    layout="centered"
)

# Application de styles CSS personnalisés
st.markdown("""
    <style>
    .stApp {
        background-color: #120F0D;
        color: #F5F2EF;
    }
    .custom-card {
        background-color: #1A1613;
        border: 1px solid #2C2420;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
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

# Base de données des candidats
database = [
    { "name": "Mehdi Besbes", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Yasmine Ben Ali", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Yessine Bouchoucha", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Lydia Meddeb", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Kenza Smat", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Yasmine Oudi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Rahma Snoussi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Selim Darghouth", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Farah El Asmi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Nermine Maya Adhoum", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Zyne Zampol", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Yassine Albouchi", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Ines Ben Naceur", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Farah Alaya", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Sohane Wawrzynowski", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Sarra Chaouch", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },
    { "name": "Baya Hadj Ali", "session": "Session 1", "topic": "Est-ce que le droit international est encore légitime de nos jours ?", "date": "Mercredi 9 septembre de 15h à 16h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Kaïs Zarrad et Adam Chtourou", "docName": "Background Guide - Droit International" },

    { "name": "Mehdi Zenkri", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Tasnim Louati", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Farah Borgi", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Bechir El Ouadhane", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Maher Ben Ouirane", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Nour Mahjoub", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Yasmine Kasraoui", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Salima Mourani", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Ramy Bouhamed", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Amine Ouerghi", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Yasmine Bousrour", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Lyne Naouali", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Sara Sancho", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Myriam Abbes", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Lina Hermassi", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Hosni Rahmatoallah", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Yasmine Mahjoub", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Sarra Khedher", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" },
    { "name": "Behia", "session": "Session 2", "topic": "Faut-il limiter la liberté d'expression en France ?", "date": "Mercredi 9 septembre de 16h à 17h", "location": "Salle F109 (Entrée Rue Bel Air)", "judges": "Sarra Ben Mahmoud et Mayara Hamaoui", "docName": "Background Guide - Liberté d'Expression" }
]

def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower().strip()

# Gestion de la session Streamlit
if 'candidate' not in st.session_state:
    st.session_state.candidate = None

# En-tête
st.markdown("<h1 style='text-align: center;'>Le Barreau</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #A89F96; text-transform: uppercase; letter-spacing: 1px;'>Lycée Pierre Mendès France — Sessions de Recrutement 2026</p>", unsafe_allow_html=True)
st.write("")

# Affichage conditionnel (Connexion vs Tableau de bord)
if st.session_state.candidate is None:
    with st.form("login_form"):
        st.markdown("### Espace Candidat")
        st.write("Entrez vos prénom et nom exacts pour accéder aux détails de votre session.")
        
        full_name_input = st.text_input("Prénom et Nom", placeholder="Ex: Mehdi Besbes")
        submitted = st.form_submit_button("Accéder à mon espace")
        
        if submitted:
            norm_input = normalize(full_name_input)
            found = next((c for c in database if normalize(c["name"]) == norm_input), None)
            
            if found:
                st.session_state.candidate = found
                st.rerun()
            else:
                st.error("Nom introuvable. Veuillez vérifier l'orthographe ou contacter le bureau.")
else:
else:
    c = st.session_state.candidate
    
    st.markdown(f"### Bienvenue, {c['name']}")
    st.info(f"📍 **{c['session']}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Sujet de Session**\n{c['topic']}")
        st.markdown(f"**Lieu exact**\n{c['location']}")
    with col2:
        st.markdown(f"**Date & Horaire**\n{c['date']}")
        st.markdown(f"**Juges / Évaluateurs**\n{c['judges']}")
    
    st.write("---")
    st.markdown(f"📄 **Support :** {c['docName']}")
    
    # Gestion dynamique du PDF selon la session
    if "Droit International" in c['docName']:
        pdf_filename = "guide_droit_international.pdf"
    else:
        pdf_filename = "guide_liberte_expression.pdf"
    
    # Bouton de téléchargement direct du PDF
    try:
        with open(pdf_filename, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button(
                label="📥 Télécharger le Background Guide (PDF)",
                data=PDFbyte,
                file_name=pdf_filename,
                mime='application/octet-stream'
            )
    except FileNotFoundError:
        st.warning(f"Le fichier {pdf_filename} est en cours de mise en ligne par le bureau.")
    
    st.write("")
    if st.button("← Se déconnecter"):
        st.session_state.candidate = None
        st.rerun()
st.markdown("<p style='text-align: center; color: #A89F96; font-size: 0.8rem;'>© 2026 Le Barreau — Lycée Pierre Mendès France, Tunis.</p>", unsafe_allow_html=True)
