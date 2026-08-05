import streamlit as st
import requests

# -------------------------------------------------------------------
# CONFIGURATION & DESIGN
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau Journal — 100% AI & Unsplash",
    page_icon="🗞️",
    layout="wide"
)

# Style CSS Sombre, Or & Cyberspace
st.markdown("""
<style>
    .main { background-color: #060913; color: #e2e8f0; }
    h1, h2, h3 { font-family: 'Georgia', serif; color: #ffffff; }
    .news-card {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 4px solid #d4af37;
        padding: 20px;
        border-radius: 4px;
        margin-bottom: 25px;
    }
    .badge-ai {
        background: rgba(0, 242, 254, 0.15);
        color: #00f2fe;
        border: 1px solid rgba(0, 242, 254, 0.4);
        padding: 2px 8px;
        font-size: 0.75rem;
        border-radius: 3px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# FONCTION : RECUPÉRATION D'IMAGE AUTOMATIQUE VIA UNSPLASH
# -------------------------------------------------------------------
def get_unsplash_image(query="justice"):
    """
    Récupère une image pertinente depuis l'API Unsplash.
    Si pas de clé API, utilise la recherche publique Unsplash Source.
    """
    # Option A : Clé API Unsplash officielle (si configurée dans Secrets Streamlit)
    api_key = st.secrets.get("UNSPLASH_ACCESS_KEY", None)
    
    if api_key:
        try:
            url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={api_key}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data['urls']['regular'], data['user']['name']
        except Exception:
            pass

    # Option B : URL Dynamique directe Unsplash (Sans clé API requise)
    clean_query = query.replace(" ", ",").lower()
    fallback_url = f"https://source.unsplash.com/featured/1200x600/?{clean_query}"
    
    # Images HD garanties si Unsplash direct met du temps
    default_images = {
        "justice": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=1200",
        "tech": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1200",
        "europe": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?q=80&w=1200",
        "finance": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=1200"
    }
    
    return default_images.get(query.lower(), default_images["justice"]), "Unsplash Library"

# -------------------------------------------------------------------
# NAVIGATION & INTERFACE
# -------------------------------------------------------------------
st.sidebar.title("🗞️ Le Barreau Journal")
st.sidebar.caption("Journal Juridique Autonome & Moteur Unsplash")

rubrique = st.sidebar.radio("Rubriques", [
    "🔥 À la Une",
    "🇫🇷 Droit Français",
    "🤖 Cyber-Droit & IA",
    "🌐 Droit International"
])

st.title("📰 LE BARREAU JOURNAL")
st.caption("Édition numérique autonome — Actualités juridiques analysées par IA")

# -------------------------------------------------------------------
# AFFICHAGE DES ARTICLES AVEC IMAGES DYNAMIQUES
# -------------------------------------------------------------------

if rubrique in ["🔥 À la Une", "🇫🇷 Droit Français"]:
    st.markdown("---")
    
    # Article 1
    query_keyword = "justice"
    img_url, photographer = get_unsplash_image(query_keyword)
    
    st.markdown("""
    <span class="badge-ai">🤖 AUTOMATISÉ • DROIT CONSTITUTIONNEL</span>
    <h2>Réforme de la Responsabilité Pénale : Le Conseil Constitutionnel Précise sa Doctrine</h2>
    """, unsafe_allow_html=True)
    
    # Affichage de l'image récupérée via Unsplash
    st.image(img_url, caption=f"Crédit photo : {photographer} / Unsplash", use_column_width=True)
    
    st.write("""
    Une décision majeure rendue ce matin redéfinit les contours de l'imputabilité pénale en cas de trouble partiel du discernement. 
    L'analyse croisée du Pôle Juridique met en lumière une évolution importante pour la jurisprudence française et l'exercice de la défense.
    """)

if rubrique in ["🔥 À la Une", "🤖 Cyber-Droit & IA"]:
    st.markdown("---")
    
    # Article 2
    query_keyword = "tech"
    img_url_tech, photographer_tech = get_unsplash_image(query_keyword)
    
    st.markdown("""
    <span class="badge-ai">🤖 AUTOMATISÉ • CYBER-DROIT & IA</span>
    <h2>Régulation des Modèles d'IA Générative : Les Nouvelles Exigences de Transparence</h2>
    """, unsafe_allow_html=True)
    
    st.image(img_url_tech, caption=f"Crédit photo : {photographer_tech} / Unsplash", use_column_width=True)
    
    st.write("""
    Les autorités d'étapes imposent désormais une traçabilité complète des données d'entraînement pour les intelligences artificielles. 
    Les entreprises du secteur s'exposent à des sanctions significatives en cas de non-conformité.
    """)
