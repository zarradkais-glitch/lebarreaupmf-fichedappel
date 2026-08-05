import streamlit as st
import requests
import random
import time

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau Journal — Quotidien Juridique IA",
    page_icon="🗞️",
    layout="wide"
)

UNSPLASH_ACCESS_KEY = "FQt3q9yJIf1-4q_v1Kg0fptsuOfsw0qfU-GvbbBb6cE"

# -------------------------------------------------------------------
# DESIGN CSS HAUTE COUTURE (CYBER-LUXE)
# -------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;600&display=swap');

    .stApp {
        background-color: #04070d;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    /* En-tête Presse Prestigieuse */
    .journal-header {
        text-align: center;
        border-bottom: 2px solid #d4af37;
        padding-bottom: 15px;
        margin-bottom: 25px;
        background: linear-gradient(180deg, rgba(212, 175, 55, 0.05) 0%, rgba(0,0,0,0) 100%);
    }

    .journal-title {
        font-family: 'Cinzel', serif;
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: 4px;
        color: #ffffff;
        text-transform: uppercase;
        margin: 0;
        text-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
    }

    .journal-title span {
        color: #d4af37;
    }

    .journal-sub {
        font-size: 0.8rem;
        letter-spacing: 3px;
        color: #00f2fe;
        text-transform: uppercase;
        margin-top: 5px;
        font-weight: 600;
    }

    /* Cartes d'Actualités Futuristes */
    .news-card-hero {
        background: rgba(10, 16, 30, 0.85);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
    }

    .badge-cyber {
        background: rgba(0, 242, 254, 0.12);
        color: #00f2fe;
        border: 1px solid rgba(0, 242, 254, 0.4);
        padding: 4px 10px;
        font-size: 0.7rem;
        border-radius: 3px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .badge-gold {
        background: rgba(212, 175, 55, 0.15);
        color: #d4af37;
        border: 1px solid rgba(212, 175, 55, 0.5);
        padding: 4px 10px;
        font-size: 0.7rem;
        border-radius: 3px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    /* HUD Metrics Box */
    .hud-box {
        background: rgba(6, 11, 22, 0.9);
        border: 1px solid rgba(212, 175, 55, 0.25);
        border-radius: 6px;
        padding: 12px;
        text-align: center;
        margin: 15px 0;
    }

    .hud-title {
        font-size: 0.65rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .hud-value {
        font-family: 'Cinzel', serif;
        font-size: 1.2rem;
        color: #d4af37;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# MOTEUR D'IMAGES DYNAMIQUES & VARIÉES
# -------------------------------------------------------------------
def fetch_dynamic_image(query_keywords):
    """
    Récupère une image toujours nouvelle et variée depuis Unsplash
    grâce à la rotation aléatoire des termes.
    """
    selected_query = random.choice(query_keywords)
    try:
        url = f"https://api.unsplash.com/photos/random?query={selected_query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        response = requests.get(url, timeout=4)
        if response.status_code == 200:
            data = response.json()
            return data['urls']['regular'], data['user']['name']
    except Exception:
        pass

    # Fallback HD varié si réseau indisponible
    backup_urls = [
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=1200",
        "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1200",
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1200"
    ]
    return random.choice(backup_urls), "Banque Unsplash Premium"

# -------------------------------------------------------------------
# EN-TÊTE ET RUBRIQUES
# -------------------------------------------------------------------
st.markdown("""
<div class="journal-header">
    <div class="journal-title">LE BARREAU <span>JOURNAL</span></div>
    <div class="journal-sub">L'Élite de l'Analyse Juridique, Géopolitique & Cyberspace</div>
</div>
""", unsafe_allow_html=True)

# Barre latérale dynamique
st.sidebar.markdown("### 🏛️ Navigation Presse")
rubrique = st.sidebar.radio("Sélectionner la Rubrique", [
    "🔥 À la Une (Édition Quotidienne)",
    "🇫🇷 Droit Français & Jurisprudence",
    "🤖 Cyber-Droit & Intelligence Artificielle",
    "🌐 Droit International & Stratégie"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚡ Statistiques Média IA")
st.sidebar.metric(label="Articles générés / 24h", value="14")
st.sidebar.metric(label="Précision des analyses", value="99.4%")

# Bouton d'actualisation manuelle du flux visuel
if st.sidebar.button("🔄 Rafraîchir les images & le flux"):
    st.rerun()

# -------------------------------------------------------------------
# CONTENU DYNAMIQUE DES ARTICLES
# -------------------------------------------------------------------

if rubrique in ["🔥 À la Une (Édition Quotidienne)", "🤖 Cyber-Droit & Intelligence Artificielle"]:
    st.markdown("""
    <div>
        <span class="badge-cyber">🤖 IA & CYBER-DROIT • ANALYSE STRATÉGIQUE</span>
        <h1 style="font-family: 'Cinzel', serif; color: #ffffff; margin-top: 10px;">L’IA à la Barre : Vers une Souveraineté Juridique Algorithmique</h1>
    </div>
    """, unsafe_allow_html=True)

    # Récupération d'image dynamique avec plusieurs mots-clés riches
    img1, photog1 = fetch_dynamic_image(["cyberpunk", "artificial-intelligence", "future-city", "tech-data"])
    st.image(img1, caption=f"Photographie : {photog1} / Unsplash", use_container_width=True)

    # Dashboard HUD de métriques rapides
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="hud-box"><div class="hud-title">Taux de Précision IA</div><div class="hud-value">94.8%</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="hud-box"><div class="hud-title">Impact Éthique</div><div class="hud-value" style="color:#00f2fe;">CRITIQUE</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="hud-box"><div class="hud-title">Statut Législatif</div><div class="hud-value" style="color:#ffffff;">EN DÉBAT</div></div>', unsafe_allow_html=True)

    st.write("""
    L'émergence des modèles algorithmiques prédictifs au sein des tribunaux internationaux soulève des questions juridiques inédites. 
    Les cabinets d'avocats de premier plan doivent aujourd'hui réévaluer la responsabilité pénale des systèmes autonomes tout en intégrant ces outils dans la préparation de leurs argumentaires. Le Barreau livre une analyse exhaustive des récents textes européens.
    """)
    st.markdown("---")

if rubrique in ["🔥 À la Une (Édition Quotidienne)", "🇫🇷 Droit Français & Jurisprudence"]:
    st.markdown("""
    <div>
        <span class="badge-gold">🇫🇷 DROIT FRANÇAIS • JURISPRUDENCE</span>
        <h1 style="font-family: 'Cinzel', serif; color: #ffffff; margin-top: 10px;">Réforme de la Responsabilité Pénale : Décision du Conseil Constitutionnel</h1>
    </div>
    """, unsafe_allow_html=True)

    img2, photog2 = fetch_dynamic_image(["courtroom", "law-book", "justice-scale", "architecture-classic"])
    st.image(img2, caption=f"Photographie : {photog2} / Unsplash", use_container_width=True)

    st.write("""
    Dans un arrêt marquant rendu cette semaine, le Conseil Constitutionnel est venu préciser la doctrine sur l'imputabilité des infractions en cas d'altération du discernement. 
    Cette décision redefine les lignes de défense traditionnelles et impose une rigueur d'analyse renouvelée pour l'ensemble des acteurs du prétoire.
    """)
    st.markdown("---")

if rubrique in ["🔥 À la Une (Édition Quotidienne)", "🌐 Droit International & Stratégie"]:
    st.markdown("""
    <div>
        <span class="badge-cyber">🌐 GÉOPOLITIQUE • TRAITÉS INTERNATIONAUX</span>
        <h1 style="font-family: 'Cinzel', serif; color: #ffffff; margin-top: 10px;">Arbitrage International et Grands Enjeux Maritimes</h1>
    </div>
    """, unsafe_allow_html=True)

    img3, photog3 = fetch_dynamic_image(["cargo-ship", "international-flags", "skyscraper", "global-business"])
    st.image(img3, caption=f"Photographie : {photog3} / Unsplash", use_container_width=True)

    st.write("""
    Les tensions relatives aux routes commerciales transcontinentales réactivent les tribunaux d'arbitrage internationaux. 
    Les juristes spécialisés en droit international public observent une mutation rapide des clauses d'arbitrage forcé au sein des accords bilatéraux.
    """)
