import streamlit as st
import pandas as pd
import unicodedata
import json
import os

# Configuration de la page
st.set_page_config(
    page_title="Le Barreau Journal | Lycée Pierre Mendès France",
    page_icon="⚖️",
    layout="wide"
)

# Design épuré, luxueux, aux tons clairs (couleurs claires, élégant, style grand magazine)
st.markdown("""
    <style>
    .stApp {
        background-color: #FDFCF7;
        color: #2C2A29;
    }
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #1A1817;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #C5A059 0%, #9E7B35 100%);
        color: #FFFFFF;
        font-weight: bold;
        border: none;
        border-radius: 6px;
        padding: 10px;
    }
    .stButton>button:hover {
        opacity: 0.9;
    }
    .article-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #E6E2D8;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Fichiers de persistance
ARTICLES_FILE = "journal_articles.csv"

# Initialisation des articles par défaut (si vide)
default_articles = [
    {
        "id": 1,
        "title": "Le procès de Socrate : aux origines de la liberté de penser",
        "category": "À la une : Histoire & Procès Historiques",
        "author": "Kaïs Zarrad",
        "content": "En 399 av. J.-C., Athènes condamne Socrate à mort pour impiété et corruption de la jeunesse. Ce procès fondateur pose les jalons de la liberté d'expression et de la responsabilité morale du citoyen face à la cité.",
        "image_url": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=1000&auto=format&fit=crop",
        "status": "Approuvé"
    },
    {
        "id": 2,
        "title": "Réforme de la justice en France : les nouveaux enjeux de 2026",
        "category": "Actualités Françaises",
        "author": "Adam Chtourou",
        "content": "La législation française introduit de nouvelles mesures pour accélérer les procédures civiles et renforcer l'accessibilité au droit numérique pour les citoyens.",
        "image_url": "https://images.unsplash.com/photo-1505664194779-8beaceb93744?q=80&w=1000&auto=format&fit=crop",
        "status": "Approuvé"
    },
    {
        "id": 3,
        "title": "La régulation mondiale de l'Intelligence Artificielle par l'ONU",
        "category": "Actualités Internationales",
        "author": "Sarra Ben Mahmoud",
        "content": "Face aux défis éthiques globaux, les nations unies unissent leurs forces pour ratifier un traité contraignant sur l'utilisation des algorithmes décisionnels.",
        "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000&auto=format&fit=crop",
        "status": "Approuvé"
    }
]

def load_articles():
    if os.path.exists(ARTICLES_FILE):
        try:
            df = pd.read_csv(ARTICLES_FILE)
            articles = []
            for _, row in df.iterrows():
                articles.append({
                    "id": int(row["id"]),
                    "title": row["title"],
                    "category": row["category"],
                    "author": row["author"],
                    "content": row["content"],
                    "image_url": row["image_url"],
                    "status": row["status"]
                })
            return articles
        except Exception:
            return default_articles
    return default_articles

def save_articles(articles):
    df = pd.DataFrame(articles)
    df.to_csv(ARTICLES_FILE, index=False)

if 'journal_articles' not in st.session_state:
    st.session_state.journal_articles = load_articles()

# États de connexion pour les onglets sécurisés
if 'membres_authenticated' not in st.session_state:
    st.session_state.membres_authenticated = False

if 'bureau_authenticated' not in st.session_state:
    st.session_state.bureau_authenticated = False

# Entête du Journal
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>LE BARREAU JOURNAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7F7C79; text-transform: uppercase; letter-spacing: 2px;'>L'excellence juridique vue par les élèves du Lycée Pierre Mendès France — Édition Mensuelle</p>", unsafe_allow_html=True)
st.write("---")

# Les 5 onglets demandés
tab_alaune, tab_actu, tab_sondages, tab_redaction, tab_bureau = st.tabs([
    "📰 À la une", 
    "🌍 Actualités (France & International)", 
    "📊 Sondages & Jeux", 
    "✍️ Espace Rédaction (Membres)", 
    "🔒 Bureau Exécutif (Validation)"
])

# ----------------------------------------------------
# ONGLET 1 : À LA UNE (Histoire et procès historiques)
# ----------------------------------------------------
with tab_alaune:
    st.markdown("## 📜 Les Grands Procès et l'Histoire du Droit")
    st.write("Retrouvez chaque mois notre grand dossier exclusif rédigé par nos membres sur les affaires qui ont façonné la justice.")
    
    alaune_articles = [a for a in st.session_state.journal_articles if "À la une" in a["category"] and a["status"] == "Approuvé"]
    
    if not alaune_articles:
        st.info("Aucun article à la une pour le moment.")
    else:
        for art in alaune_articles:
            st.markdown(f"<div class='article-card'>", unsafe_allow_html=True)
            st.markdown(f"### {art['title']}")
            st.markdown(f"<p style='color: #8C6D32; font-weight: bold;'>Rédigé par : {art['author']}</p>", unsafe_allow_html=True)
            if art['image_url']:
                st.image(art['image_url'], use_container_width=True)
            st.write(art['content'])
            st.markdown(f"</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# ONGLET 2 : ACTUALITÉS (Françaises et Internationales)
# ----------------------------------------------------
with tab_actu:
    st.markdown("## 🌐 Actualités Juridiques : France & International")
    st.write("Les évolutions majeures du droit décryptées par notre rédaction pour faire rayonner notre communauté.")
    
    actu_articles = [a for a in st.session_state.journal_articles if "Actualités" in a["category"] and a["status"] == "Approuvé"]
    
    if not actu_articles:
        st.info("Aucune actualité publiée pour l'instant.")
    else:
        for art in actu_articles:
            st.markdown(f"<div class='article-card'>", unsafe_allow_html=True)
            st.markdown(f"<span style='background-color: #EFECE6; padding: 4px 8px; border-radius: 4px; font-size: 0.8rem;'>{art['category']}</span>", unsafe_allow_html=True)
            st.markdown(f"### {art['title']}")
            st.markdown(f"<p style='color: #8C6D32; font-weight: bold;'>Rédigé par : {art['author']}</p>", unsafe_allow_html=True)
            if art['image_url']:
                st.image(art['image_url'], use_container_width=True)
            st.write(art['content'])
            st.markdown(f"</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# ONGLET 3 : SONDAGES & JEUX (Mini Scrabble & Avis)
# ----------------------------------------------------
with tab_sondages:
    st.markdown("## 📊 Sondages de la Communauté & Coin Jeux")
    st.write("Donnez votre avis pour façonner nos futurs contenus et détendez-vous avec notre mini-jeu juridique !")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Sondage 1 : Question du mois")
        q1 = st.radio("Pensez-vous que les tribunaux devraient intégrer l'intelligence artificielle pour assister les juges ?", ["Tout à fait", "Plutôt oui", "Plutôt non", "Pas du tout"])
        if st.button("Voter pour la question du mois"):
            st.success("Merci pour votre vote ! Votre voix a bien été prise en compte.")
            
    with col2:
        st.markdown("### Sondage 2 : Vos retours sur le journal")
        aime = st.radio("Appréciez-vous le contenu et le format du Barreau Journal ?", ["Oui", "Non"])
        pourquoi = st.text_area("Pourquoi ? (Vos explications nous aident énormément à progresser)")
        if st.button("Envoyer mon avis"):
            st.success("Merci infiniment pour vos retours constructifs !")

    st.write("---")
    st.markdown("### 🧩 Le Coin Jeux : Mini-Scrabble Juridique")
    st.write("Retrouvez chaque mois un défi de vocabulaire juridique. Retrouvez le mot mystère à partir des lettres proposées !")
    
    lettres = "J - U - R - I - S - P - R - U - D - E - N - C - E"
    st.markdown(f"<h3 style='text-align: center; letter-spacing: 3px; color: #8C6D32;'>{lettres}</h3>", unsafe_allow_html=True)
    
    mot_mystere = st.text_input("Proposez votre mot juridique basé sur ces lettres :")
    if st.button("Vérifier le mot"):
        if len(mot_mystere) > 3:
            st.success(f"Bravo ! '{mot_mystere}' est une excellente proposition pour enrichir votre culture lexicale !")
        else:
            st.warning("Essayez de trouver un terme juridique un peu plus long !")

# ----------------------------------------------------
# ONGLET 4 : ESPACE RÉDACTION (Réservé aux membres - VERROUILLÉ)
# ----------------------------------------------------
with tab_redaction:
    st.markdown("## ✍️ Espace Rédaction des Membres")
    
    if not st.session_state.membres_authenticated:
        st.warning("🔒 Cet espace est strictement réservé aux membres rédacteurs du Barreau.")
        with st.form("login_membres_form"):
            pwd_membres = st.text_input("Entrez le mot de passe Membres", type="password")
            submit_login_membres = st.form_submit_button("Se connecter")
            
            if submit_login_membres:
                # Mot de passe unique pour les membres (modifiable selon vos préférences)
                if pwd_membres == "BarreauMembres2026":
                    st.session_state.membres_authenticated = True
                    st.success("Connexion réussie !")
                    st.rerun()
                else:
                    st.error("Mot de passe incorrect.")
    else:
        st.success("✅ Connecté à l'espace rédaction des membres.")
        if st.button("Se déconnecter de l'espace membres"):
            st.session_state.membres_authenticated = False
            st.rerun()
            
        st.write("---")
        st.write("Rédigez vos articles et soumettez-les directement au comité de relecture du bureau.")
        
        with st.form("form_redaction"):
            auteur = st.text_input("Votre Prénom et Nom")
            titre = st.text_input("Titre de l'article")
            categorie = st.selectbox("Rubrique", [
                "À la une : Histoire & Procès Historiques", 
                "Actualités Françaises", 
                "Actualités Internationales"
            ])
            image_link = st.text_input("Lien de l'image (URL HTTPS)")
            contenu = st.text_area("Contenu complet de l'article")
            
            submit_article = st.form_submit_button("Soumettre au bureau pour validation")
            
            if submit_article:
                if auteur and titre and contenu:
                    new_art = {
                        "id": len(st.session_state.journal_articles) + 1,
                        "title": titre,
                        "category": categorie,
                        "author": auteur,
                        "content": contenu,
                        "image_url": image_link if image_link else "https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=1000&auto=format&fit=crop",
                        "status": "En attente"
                    }
                    st.session_state.journal_articles.append(new_art)
                    save_articles(st.session_state.journal_articles)
                    st.success("Article soumis avec succès ! Il est en attente d'approbation par le bureau exécutif.")
                else:
                    st.error("Veuillez remplir au moins votre nom, le titre et le contenu.")

# ----------------------------------------------------
# ONGLET 5 : BUREAU EXÉCUTIF (Validation des articles - VERROUILLÉ)
# ----------------------------------------------------
with tab_bureau:
    st.markdown("## 🔒 Comité de Relecture (Bureau Exécutif)")
    
    if not st.session_state.bureau_authenticated:
        st.warning("🔒 Cet espace est strictement réservé aux membres du bureau exécutif.")
        with st.form("login_bureau_form"):
            pwd_bureau = st.text_input("Entrez le mot de passe Bureau Exécutif", type="password")
            submit_login_bureau = st.form_submit_button("Connexion Bureau")
            
            if submit_login_bureau:
                # Mot de passe unique pour le bureau exécutif
                if pwd_bureau == "KaisZarrad123pass":
                    st.session_state.bureau_authenticated = True
                    st.success("Connexion réussie !")
                    st.rerun()
                else:
                    st.error("Mot de passe incorrect.")
    else:
        st.success("✅ Connecté au comité de relecture du bureau.")
        if st.button("Se déconnecter du bureau"):
            st.session_state.bureau_authenticated = False
            st.rerun()
            
        st.write("---")
        st.write("Approuvez ou rejetez les articles soumis par les membres avant leur publication officielle.")
        
        pending_arts = [a for a in st.session_state.journal_articles if a["status"] == "En attente"]
        
        if not pending_arts:
            st.info("Aucun article en attente de relecture pour le moment.")
        else:
            for art in pending_arts:
                st.markdown(f"<div class='article-card'>", unsafe_allow_html=True)
                st.markdown(f"### [{art['category']}] {art['title']}")
                st.markdown(f"<p style='color: #8C6D32;'>Auteur : <b>{art['author']}</b></p>", unsafe_allow_html=True)
                st.write(art['content'])
                
                col_app1, col_app2 = st.columns(2)
                with col_app1:
                    if st.button(f"✅ Approuver", key=f"app_{art['id']}"):
                        art["status"] = "Approuvé"
                        save_articles(st.session_state.journal_articles)
                        st.success("Article approuvé et publié !")
                        st.rerun()
                with col_app2:
                    if st.button(f"❌ Rejeter", key=f"rej_{art['id']}"):
                        st.session_state.journal_articles.remove(art)
                        save_articles(st.session_state.journal_articles)
                        st.error("Article rejeté et supprimé.")
                        st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align: center; color: #7F7C79; font-size: 0.8rem;'>© 2026 Le Barreau Journal — Lycée Pierre Mendès France, Tunis.</p>", unsafe_allow_html=True)
