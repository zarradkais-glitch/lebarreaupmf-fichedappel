import streamlit as st
import requests
import random
from datetime import datetime

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau Journal — Édition Officielle",
    page_icon="⚖️",
    layout="wide"
)

UNSPLASH_ACCESS_KEY = "FQt3q9yJIf1-4q_v1Kg0fptsuOfsw0qfU-GvbbBb6cE"

# -------------------------------------------------------------------
# DESAIGN EDITORIAL MODERN (INSPIRATION MAQUETTE YORKNEW)
# -------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    /* Arrière-plan clair et épuré */
    .stApp {
        background-color: #F8F9FA;
        color: #1A1D20;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Barre de navigation haute moderne */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px 30px 0px;
        border-bottom: 1px solid #E9ECEF;
        margin-bottom: 30px;
    }
    
    .brand-logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: #0F172A;
    }

    /* Hero Section type landing page */
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1.15;
        color: #0F172A;
        margin-bottom: 15px;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 25px;
        max-width: 600px;
        line-height: 1.6;
    }

    /* Cartes Modernes Flottantes */
    .card-modern {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid #E2E8F0;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 20px;
    }

    .badge-modern {
        background: #F1F5F9;
        color: #334155;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 6px 12px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Bloc d'Impact Sombre (inspiration section noire de la maquette) */
    .dark-section {
        background: #0F172A;
        color: #FFFFFF;
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
    }

    /* Boutons arrondis au style moderne */
    .stButton>button {
        border-radius: 30px !important;
        background-color: #0F172A !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# RECUPERATION D'IMAGES
# -------------------------------------------------------------------
def get_unsplash_image(query="architecture"):
    try:
        url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        res = requests.get(url, timeout=4)
        if res.status_code == 200:
            data = res.json()
            return data['urls']['regular'], data['user']['name']
    except Exception:
        pass
    return "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200", "Unsplash Library"

# -------------------------------------------------------------------
# INTERACTION DE BIENVENUE (BALLONS AU PREMIER CHARGEMENT)
# -------------------------------------------------------------------
if 'welcome_shown' not in st.session_state:
    st.balloons()
    st.session_state.welcome_shown = True

# -------------------------------------------------------------------
# EN-TÊTE ÉPURÉ
# -------------------------------------------------------------------
st.markdown("""
<div class="top-nav">
    <div class="brand-logo">⚖️ LE BARREAU JOURNAL</div>
    <div style="color: #64748B; font-size: 0.9rem;">Édition Officielle du Lycée Pierre Mendès France</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# SIDEBAR / PARAMÈTRES
# -------------------------------------------------------------------
st.sidebar.title("Navigation & Interactions")
page = st.sidebar.radio("Pages", [
    "🏠 Accueil & À la Une",
    "🗳️ Le Débat du Jour",
    "📜 Archives & Jurisprudence"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎈 Animations")
if st.sidebar.button("Lancer les ballons de bienvenue"):
    st.balloons()

if st.sidebar.button("Effet célébration (Neige)"):
    st.snow()

# -------------------------------------------------------------------
# PAGE 1 : ACCUEIL STYLE MAQUETTE MODERN LANDING
# -------------------------------------------------------------------
if page == "🏠 Accueil & À la Une":

    # Hero Section
    col_hero1, col_hero2 = st.columns([1.2, 1])

    with col_hero1:
        st.markdown('<span class="badge-modern">ÉDITION DU JOUR</span>', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">L\'actualité juridique décryptée par la jeunesse.</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="hero-subtitle">
            Une plateforme autonome d'analyse légale, de jurisprudence et de débats sociétaux rédigée et structurée pour offrir une clarté absolue sur les grands enjeux contemporains.
        </div>
        """, unsafe_allow_html=True)

    with col_hero2:
        img_hero, photographer = get_unsplash_image("modern-architecture")
        st.image(img_hero, caption=f"Photo par {photographer}", use_container_width=True)

    st.markdown("---")

    # Grille d'Articles Style "Cards"
    st.subheader("📰 À la une cette semaine")

    col1, col2, col3 = st.columns(3)

    with col1:
        img_a1, _ = get_unsplash_image("courtroom")
        st.image(img_a1, use_container_width=True)
        st.markdown("""
        <div class="card-modern">
            <span class="badge-modern">Droit Français</span>
            <h4 style="margin-top: 10px;">Réforme de la Responsabilité Pénale</h4>
            <p style="color: #64748B; font-size: 0.9rem;">Le Conseil Constitutionnel précise sa doctrine quant à l'imputabilité des infractions en cas de trouble partiel.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        img_a2, _ = get_unsplash_image("technology")
        st.image(img_a2, use_container_width=True)
        st.markdown("""
        <div class="card-modern">
            <span class="badge-modern">Cyber-Droit</span>
            <h4 style="margin-top: 10px;">Transparence des Algorithmes</h4>
            <p style="color: #64748B; font-size: 0.9rem;">Analyse des nouvelles directives européennes encadrant l'utilisation de l'intelligence artificielle dans le secteur public.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        img_a3, _ = get_unsplash_image("city-building")
        st.image(img_a3, use_container_width=True)
        st.markdown("""
        <div class="card-modern">
            <span class="badge-modern">International</span>
            <h4 style="margin-top: 10px;">Enjeux du Droit Maritime</h4>
            <p style="color: #64748B; font-size: 0.9rem;">Les récentes décisions d'arbitrage concernant les voies de transit commercial transcontinental.</p>
        </div>
        """, unsafe_allow_html=True)

    # Section Sombre d'Impact (Comme sur le bas de la maquette)
    st.markdown("""
    <div class="dark-section">
        <h2 style="font-family: 'Playfair Display', serif; margin-top:0;">Rejoignez le réseau du Barreau Journal</h2>
        <p style="color: #94A3B8; max-width: 600px;">
            Participez aux rédactions, soumettez vos tribunes ou votez chaque semaine sur les débats juridiques qui façonnent notre quotidien.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# PAGE 2 : LE DÉBAT INTERACTIF
# -------------------------------------------------------------------
elif page == "🗳️ Le Débat du Jour":
    st.markdown('<span class="badge-modern">GRAND DÉBAT DU BARREAU</span>', unsafe_allow_html=True)
    st.markdown("# Faut-il accorder une personnalité juridique autonome à l'Intelligence Artificielle ?")
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        if st.button("👍 OUI — Pour la création d'un statut d'Agent Autonome", use_container_width=True):
            st.balloons()
            st.success("Votre vote pour le OUI a été pris en compte !")

    with col_v2:
        if st.button("👎 NON — Garder la responsabilité humaine", use_container_width=True):
            st.info("Votre vote pour le NON a été pris en compte !")

    st.markdown("---")
    st.subheader("✍️ Publier une tribune ou un avis")
    st.text_input("Votre Nom / Classe :", placeholder="ex: Kaïs Zarrad")
    st.text_area("Votre argumentaire juridique :")
    if st.button("Soumettre la contribution"):
        st.success("Votre contribution a été enregistrée avec succès !")

# -------------------------------------------------------------------
# PAGE 3 : ARCHIVES
# -------------------------------------------------------------------
elif page == "📜 Archives & Jurisprudence":
    st.markdown("# 📚 Jurisprudence & Sources Officielle")
    st.write("Retrouvez ici l'intégralité des arrêts analysés et les liens vers les textes de loi de référence (Légifrance, Conseil d'État, EUR-Lex).")
