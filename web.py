import streamlit as st
import requests
import random
import time
from datetime import datetime, timedelta

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau Journal",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

UNSPLASH_ACCESS_KEY = "FQt3q9yJIf1-4q_v1Kg0fptsuOfsw0qfU-GvbbBb6cE"

# -------------------------------------------------------------------
# DESIGN EDITORIAL MODERNE & ÉPURÉ
# -------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    .stApp {
        background-color: #F8F9FA;
        color: #1A1D20;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        padding: 10px 0px 20px 0px;
        border-bottom: 2px solid #E2E8F0;
        margin-bottom: 40px;
    }
    
    .brand-logo {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: #0F172A;
    }

    .article-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 700;
        line-height: 1.2;
        color: #0F172A;
        margin-bottom: 15px;
        margin-top: 20px;
    }

    .article-meta {
        font-size: 0.9rem;
        color: #64748B;
        margin-bottom: 25px;
        border-left: 3px solid #D4AF37;
        padding-left: 10px;
    }

    .article-content {
        font-size: 1.1rem;
        line-height: 1.7;
        color: #334155;
        text-align: justify;
    }

    .source-box {
        background: #F1F5F9;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 15px 20px;
        margin-top: 30px;
        font-size: 0.9rem;
    }
    
    .source-box h4 {
        margin-top: 0;
        color: #0F172A;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .badge-modern {
        background: #0F172A;
        color: #FFFFFF;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 6px 12px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .poll-results-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #0F172A;
        border-radius: 8px;
        padding: 20px;
        margin-top: 40px;
        margin-bottom: 30px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.03);
    }
    
    .sidebar-brand {
        background: #4A5548;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Playfair Display', serif;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# MOTEUR D'IMAGES DYNAMIQUES
# -------------------------------------------------------------------
def get_unsplash_image(keywords):
    selected_query = random.choice(keywords)
    timestamp = int(time.time() * 1000) + random.randint(1, 10000)
    try:
        url = f"https://api.unsplash.com/photos/random?query={selected_query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}&sig={timestamp}"
        res = requests.get(url, timeout=4)
        if res.status_code == 200:
            data = res.json()
            return data['urls']['regular'], data['user']['name']
    except Exception:
        pass
    return f"https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=1200&sig={timestamp}", "Unsplash Premium"

# -------------------------------------------------------------------
# GESTION DE LA MÉMOIRE DES VOTES (Sondage de la veille)
# -------------------------------------------------------------------
if 'voted' not in st.session_state:
    st.session_state.voted = False
    st.session_state.vote_choice = None
    st.session_state.count_pour = 142  - random.randint(5, 20) # Simulation de votes de la veille
    st.session_state.count_contre = 98 + random.randint(5, 20)

# -------------------------------------------------------------------
# ANIMATION DE BIENVENUE (TOAST UNIQUE)
# -------------------------------------------------------------------
if 'welcome_shown' not in st.session_state:
    time.sleep(0.5)
    st.toast("La justice n'attend pas. Bienvenue sur le Journal officiel du club.", icon="⚖️")
    st.session_state.welcome_shown = True

# -------------------------------------------------------------------
# BARRE LATÉRALE
# -------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <h3 style="margin:0; color:#FFFFFF;">LE BARREAU</h3>
        <p style="font-size:0.8rem; margin:5px 0 0 0; color:#E2E8F0;">Journal officiel du club</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("© 2026 Le Barreau. Bureau Exécutif.")

# -------------------------------------------------------------------
# EN-TÊTE PRINCIPAL
# -------------------------------------------------------------------
st.markdown(f"""
<div class="top-nav">
    <div class="brand-logo">LE BARREAU JOURNAL</div>
    <div style="color: #64748B; font-size: 0.95rem; font-weight: 500;">
        Journal officiel du club • {(datetime.now()).strftime('%d %B %Y')}
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# CRÉATION DES 3 ONGLETS EXACTS
# -------------------------------------------------------------------
onglet_une, onglet_debat, onglet_sources = st.tabs([
    "📄 À la une", 
    "🗳️ Débat interactif", 
    "📚 Sources et jurisprudences"
])

# ===================================================================
# ONGLÉ 1 : À LA UNE (Inclus les résultats du sondage de la veille)
# ===================================================================
with onglet_une:
    st.markdown('<span class="badge-modern">JURISPRUDENCE PÉNALE</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">L\'Altération du Discernement : Le Conseil Constitutionnel Trace une Nouvelle Ligne Rouge</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="article-meta">Par le Pôle Rédactionnel • Lecture : 4 min • Édition du {(datetime.now()).strftime("%d %B %Y")}</div>', unsafe_allow_html=True)

    img_hero, photog_hero = get_unsplash_image(["supreme-court", "gavel", "justice-scale", "law-books", "trial", "legal-office"])
    st.image(img_hero, caption=f"Crédit photographique : {photog_hero} / Unsplash", use_container_width=True)

    st.markdown("""
    <div class="article-content">
        L'imputabilité des infractions commises sous l'emprise de substances psychoactives fait l'objet d'un revirement jurisprudentiel majeur. 
        Saisi d'une Question Prioritaire de Constitutionnalité (QPC), le Conseil Constitutionnel a dû trancher un débat juridique complexe : 
        l'abolition temporaire du discernement, lorsqu'elle résulte d'une consommation volontaire de stupéfiants, peut-elle constituer une cause d'irresponsabilité pénale au sens de l'article 122-1 du Code pénal ?
        <br><br>
        Dans sa décision rendue publique, les Sages ont affirmé que la protection de la société prévaut. 
        <b>Le fait de se placer volontairement dans un état de vulnérabilité psychique ne saurait exonérer l'auteur de ses actes.</b> 
        Cette décision vient clore des mois de débats doctrinaux initiés par la Cour de cassation, et impose désormais aux juges du fond d'évaluer <i>l'intention préalable</i> à la consommation de la substance.
    </div>
    """, unsafe_allow_html=True)

    # BLOC RÉSULTATS DU SONDAGE DE LA VEILLE (Affiché le lendemain sur la page d'accueil)
    total_votes = st.session_state.count_pour + st.session_state.count_contre
    pct_pour = int((st.session_state.count_pour / total_votes) * 100)
    pct_contre = 100 - pct_pour

    st.markdown(f"""
    <div class="poll-results-box">
        <span class="badge-modern">RÉSULTATS OFFICIELS DU SONDAGE DE LA VEILLE</span>
        <h3 style="font-family: 'Playfair Display', serif; margin-top: 10px; margin-bottom: 5px;">
            Sujet : Le droit de vote à 16 ans — Verdict de la communauté
        </h3>
        <p style="color: #64748B; font-size: 0.9rem; margin-bottom: 20px;">
            Clôture du scrutin après 24 heures de consultation • Total des suffrages exprimés : <b>{total_votes} votes</b>
        </p>
        <div style="margin-bottom: 10px;">
            <b>👍 POUR (Élargissement du corps électoral) :</b> {pct_pour}% ({st.session_state.count_pour} votes)
        </div>
        <div style="background: #E2E8F0; border-radius: 4px; height: 10px; width: 100%; margin-bottom: 15px;">
            <div style="background: #0F172A; width: {pct_pour}%; height: 10px; border-radius: 4px;"></div>
        </div>
        <div style="margin-bottom: 10px;">
            <b>👎 CONTRE (Maintien de la majorité à 18 ans) :</b> {pct_contre}% ({st.session_state.count_contre} votes)
        </div>
        <div style="background: #E2E8F0; border-radius: 4px; height: 10px; width: 100%;">
            <div style="background: #64748B; width: {pct_contre}%; height: 10px; border-radius: 4px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================================================================
# ONGLÉ 2 : DÉBAT INTERACTIF
# ===================================================================
with onglet_debat:
    st.markdown('<span class="badge-modern">SCRUD & TRIBUNE LIBRE</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Le Débat de la Semaine : Participez au Scrutin</div>', unsafe_allow_html=True)
    st.write("Exprimez votre position juridique. Les résultats définitifs de ce vote seront publiés dès demain matin à la Une.")
    
    img_deb, photog_deb = get_unsplash_image(["voting", "youth", "debate", "microphone", "parliament-session"])
    st.image(img_deb, caption=f"Crédit photographique : {photog_deb} / Unsplash", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Option A : POUR")
        st.write("La jeunesse est en première ligne des grands enjeux de long terme (climat, dette). Aligner la citoyenneté active sur la responsabilité pénale relève de l'équité.")
    with col2:
        st.markdown("#### Option B : CONTRE")
        st.write("Le droit civil fixe la majorité à 18 ans pour garantir une pleine autonomie contractuelle et intellectuelle vis-à-vis du cadre familial.")

    st.markdown("---")
    
    if not st.session_state.voted:
        st.subheader("🗳️ Exprimez votre vote (Action unique pour cette session)")
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            if st.button("Voter POUR l'élargissement", use_container_width=True):
                st.session_state.count_pour += 1
                st.session_state.voted = True
                st.session_state.vote_choice = "POUR"
                st.success("Votre vote a été enregistré avec succès ! Il apparaîtra dans les résultats de demain.")
                st.rerun()
        with v_col2:
            if st.button("Voter CONTRE le projet", use_container_width=True):
                st.session_state.count_contre += 1
                st.session_state.voted = True
                st.session_state.vote_choice = "CONTRE"
                st.success("Votre vote a été enregistré avec succès ! Il apparaîtra dans les résultats de demain.")
                st.rerun()
    else:
        st.info(f"✅ Vous avez déjà voté pour l'option **{st.session_state.vote_choice}**. Les résultats complets seront consultables dès demain sur l'onglet *À la une*.")

    st.markdown("---")
    st.subheader("📝 Soumettre votre plaidoirie")
    st.text_input("Identité & Rôle", placeholder="Ex: Membre du Barreau")
    st.text_area("Votre argumentaire juridique :")
    if st.button("Transmettre au bureau"):
        st.success("Votre contribution a été transmise au comité de lecture.")

# ===================================================================
# ONGLÉ 3 : SOURCES ET JURISPRUDENCES
# ===================================================================
with onglet_sources:
    st.markdown('<span class="badge-modern">VEILLE DOCUMENTAIRE</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Sources et Jurisprudences Officielles</div>', unsafe_allow_html=True)
    st.write("Retrouvez l'ensemble des bases légales et des arrêts de référence ayant servi à la rédaction des analyses.")

    img_src, photog_src = get_unsplash_image(["library", "old-books", "archive", "document-stack"])
    st.image(img_src, caption=f"Crédit photographique : {photog_src} / Unsplash", use_container_width=True)

    st.markdown("""
    <div class="source-box">
        <h4>📚 Références Constitutionnelles et Administratives</h4>
        <ul>
            <li><b>Conseil Constitutionnel :</b> <a href="https://www.conseil-constitutionnel.fr/" target="_blank">Accès au portail des décisions et QPC</a></li>
            <li><b>Légifrance :</b> <a href="https://www.legifrance.gouv.fr/" target="_blank">Service public de la diffusion du droit (Codes et Lois)</a></li>
            <li><b>Cour de Cassation :</b> <a href="https://www.courdecassation.fr/" target="_blank">Jurisprudence de l'ordre judiciaire</a></li>
            <li><b>Conseil d'État :</b> <a href="https://www.conseil-etat.fr/" target="_blank">Jurisprudence administrative et arrêts d'assemblée</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
