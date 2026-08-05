import streamlit as st
import requests
import random
import time
import json
import os
from datetime import datetime

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau — Plateforme Interne",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

UNSPLASH_ACCESS_KEY = "FQt3q9yJIf1-4q_v1Kg0fptsuOfsw0qfU-GvbbBb6cE"
DATA_FILE = "articles.json"

# -------------------------------------------------------------------
# GESTION DES ARTICLES ET DONNÉES
# -------------------------------------------------------------------
def charger_articles():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return [
        {
            "titre": "L'Altération du Discernement : Le Conseil Constitutionnel Trace une Nouvelle Ligne Rouge",
            "rubrique": "JURISPRUDENCE PÉNALE",
            "auteur": "Le Pôle Académique",
            "date": datetime.now().strftime("%d %B %Y"),
            "contenu": "L'imputabilité des infractions commises sous l'emprise de substances psychoactives fait l'objet d'un revirement jurisprudentiel majeur...",
            "source_texte": "Conseil Constitutionnel - Décision n° 2026-987 QPC",
            "source_lien": "https://www.conseil-constitutionnel.fr/"
        }
    ]

def sauvegarder_article(nouvel_article):
    articles = charger_articles()
    articles.insert(0, nouvel_article)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

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
    
    .dashboard-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.02);
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

# Gestion mémoire des votes
if 'voted' not in st.session_state:
    st.session_state.voted = False
    st.session_state.vote_choice = None
    st.session_state.count_pour = 125
    st.session_state.count_contre = 84

if 'welcome_shown' not in st.session_state:
    time.sleep(0.5)
    st.toast("Bienvenue sur l'espace officiel et unifié du Barreau.", icon="⚖️")
    st.session_state.welcome_shown = True

# -------------------------------------------------------------------
8# BARRE LATÉRALE
# -------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <h3 style="margin:0; color:#FFFFFF;">LE BARREAU</h3>
        <p style="font-size:0.8rem; margin:5px 0 0 0; color:#E2E8F0;">Plateforme Interne & Journal</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("© 2026 Le Barreau. Bureau Exécutif.")

# -------------------------------------------------------------------
# EN-TÊTE PRINCIPAL
# -------------------------------------------------------------------
st.markdown(f"""
<div class="top-nav">
    <div class="brand-logo">LE BARREAU PORTAL</div>
    <div style="color: #64748B; font-size: 0.95rem; font-weight: 500;">
        Édition Officielle • {datetime.now().strftime('%d %B %Y')}
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# NAVIGATION PAR ONGLETS PUBLICS ET INTERNES
# -------------------------------------------------------------------
tab_une, tab_debat, tab_sources, tab_pres, tab_sec, tab_com, tab_media, tab_acad = st.tabs([
    "📄 À la une", 
    "🗳️ Débat", 
    "📚 Sources", 
    "🏛️ Présidence", 
    "📋 Secrétariat", 
    "📢 Communication", 
    "🎬 Médias", 
    "📚 Académique"
])

# ===================================================================
# 1. À LA UNE (Public)
# ===================================================================
with tab_une:
    articles = charger_articles()
    for art in articles:
        st.markdown(f'<span class="badge-modern">{art["rubrique"]}</span>', unsafe_allow_html=True)
        st.markdown(f'<div class="article-title">{art["titre"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="article-meta">Par {art["auteur"]} • Lecture : 4 min • Édition du {art["date"]}</div>', unsafe_allow_html=True)

        img_hero, photog_hero = get_unsplash_image(["supreme-court", "gavel", "justice-scale", "law-books", "trial"])
        st.image(img_hero, caption=f"Crédit : {photog_hero} / Unsplash", use_container_width=True)

        st.markdown(f'<div class="article-content">{art["contenu"]}</div>', unsafe_allow_html=True)
        
        if art.get("source_texte"):
            st.markdown(f"""
            <div class="source-box">
                <h4>📚 Source Officielle</h4>
                <a href="{art.get('source_lien', '#')}" target="_blank">{art['source_texte']}</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("---")

    # Résultats sondage de la veille
    total_votes = st.session_state.count_pour + st.session_state.count_contre
    pct_pour = int((st.session_state.count_pour / total_votes) * 100)
    pct_contre = 100 - pct_pour

    st.markdown(f"""
    <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-left: 5px solid #0F172A; border-radius: 8px; padding: 20px; margin-top: 30px;">
        <span class="badge-modern">RÉSULTATS DU SONDAGE DE LA VEILLE</span>
        <h3 style="font-family: 'Playfair Display', serif; margin-top: 10px;">Le droit de vote à 16 ans — Verdict</h3>
        <p style="color: #64748B; font-size: 0.9rem;">Total des suffrages exprimés : <b>{total_votes} votes</b></p>
        <div style="margin-bottom: 5px;"><b>👍 POUR :</b> {pct_pour}% ({st.session_state.count_pour} votes)</div>
        <div style="background: #E2E8F0; border-radius: 4px; height: 10px; width: 100%; margin-bottom: 15px;">
            <div style="background: #0F172A; width: {pct_pour}%; height: 10px; border-radius: 4px;"></div>
        </div>
        <div style="margin-bottom: 5px;"><b>👎 CONTRE :</b> {pct_contre}% ({st.session_state.count_contre} votes)</div>
        <div style="background: #E2E8F0; border-radius: 4px; height: 10px; width: 100%;">
            <div style="background: #64748B; width: {pct_contre}%; height: 10px; border-radius: 4px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================================================================
# 2. DÉBAT INTERACTIF (Public)
# ===================================================================
with tab_debat:
    st.markdown('<span class="badge-modern">SCRUTIN OFFICIEL</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Le Débat de la Semaine</div>', unsafe_allow_html=True)
    st.write("Exprimez votre position. Les résultats s'afficheront dès demain sur la page À la une.")
    
    img_deb, photog_deb = get_unsplash_image(["voting", "youth", "debate", "microphone"])
    st.image(img_deb, caption=f"Crédit : {photog_deb} / Unsplash", use_container_width=True)

    if not st.session_state.voted:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Voter POUR", use_container_width=True):
                st.session_state.count_pour += 1
                st.session_state.voted = True
                st.session_state.vote_choice = "POUR"
                st.success("Vote enregistré !")
                st.rerun()
        with c2:
            if st.button("Voter CONTRE", use_container_width=True):
                st.session_state.count_contre += 1
                st.session_state.voted = True
                st.session_state.vote_choice = "CONTRE"
                st.success("Vote enregistré !")
                st.rerun()
    else:
        st.info(f"✅ Vous avez voté **{st.session_state.vote_choice}**.")

# ===================================================================
# 3. SOURCES ET JURISPRUDENCES (Public)
# ===================================================================
with tab_sources:
    st.markdown('<span class="badge-modern">VEILLE DOCUMENTAIRE</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Sources et Jurisprudences Officielles</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="source-box">
        <h4>📚 Références Clés</h4>
        <ul>
            <li><b>Conseil Constitutionnel :</b> <a href="https://www.conseil-constitutionnel.fr/" target="_blank">Portail des décisions</a></li>
            <li><b>Légifrance :</b> <a href="https://www.legifrance.gouv.fr/" target="_blank">Service public de diffusion du droit</a></li>
            <li><b>Conseil d'État :</b> <a href="https://www.conseil-etat.fr/" target="_blank">Jurisprudence administrative</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ===================================================================
# 4. ESPACE PRÉSIDENCE (Sécurisé)
# ===================================================================
with tab_pres:
    st.markdown('<span class="badge-modern">DIRECTION</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Espace Présidence</div>', unsafe_allow_html=True)
    pwd = st.text_input("Mot de passe Présidence :", type="password", key="pwd_pres")
    if pwd == "pres2026":
        st.success("Accès autorisé - Direction")
        st.markdown("""
        <div class="dashboard-card">
            <h4>🎯 Notes Stratégiques & Feuille de Route</h4>
            <p>Superviser les pôles, valider le budget et planifier les grands événements de l'année.</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_area("Ordre du jour de la prochaine réunion exécutive :")
        if st.button("Sauvegarder les notes de direction"):
            st.success("Notes enregistrées avec succès.")
    elif pwd != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 5. ESPACE SECRÉTARIAT GÉNÉRAL (Sécurisé)
# ===================================================================
with tab_sec:
    st.markdown('<span class="badge-modern">ADMINISTRATION</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Espace Secrétariat Général</div>', unsafe_allow_html=True)
    pwd = st.text_input("Mot de passe Secrétariat :", type="password", key="pwd_sec")
    if pwd == "sec2026":
        st.success("Accès autorisé - Secrétariat")
        st.markdown("""
        <div class="dashboard-card">
            <h4>📋 Gestion Administrative & Registres</h4>
            <p>Suivi des présences, rédaction des procès-verbaux (PV) et gestion des adhésions.</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Ajouter un nouveau membre au registre :")
        st.text_area("Compte-rendu de la dernière assemblée :")
        if st.button("Enregistrer au registre officiel"):
            st.success("Mise à jour effectuée.")
    elif pwd != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 6. ESPACE COMMUNICATION (Sécurisé)
# ===================================================================
with tab_com:
    st.markdown('<span class="badge-modern">COMMUNICATION</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Espace Chef Communication</div>', unsafe_allow_html=True)
    pwd = st.text_input("Mot de passe Communication :", type="password", key="pwd_com")
    if pwd == "com2026":
        st.success("Accès autorisé - Communication")
        st.markdown("""
        <div class="dashboard-card">
            <h4>📢 Calendrier Éditorial & Réseaux Sociaux</h4>
            <p>Planification des publications Instagram, affiches de la semaine et relations publiques.</p>
        </div>
        """, unsafe_allow_html=True)
        st.selectbox("Réseau cible", ["Instagram", "LinkedIn", "Affichage Interne"])
        st.text_input("Légende de la publication à venir :")
        if st.button("Valider le plan de communication"):
        	st.success("Plan validé !")
    elif pwd != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 7. ESPACE MÉDIAS (Sécurisé)
# ===================================================================
with tab_media:
    st.markdown('<span class="badge-modern">PRODUCTION MÉDIA</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Espace Chef Média</div>', unsafe_allow_html=True)
    pwd = st.text_input("Mot de passe Média :", type="password", key="pwd_media")
    if pwd == "media2026":
        st.success("Accès autorisé - Pôle Média")
        st.markdown("""
        <div class="dashboard-card">
            <h4>🎬 Photothèque & Tournages</h4>
            <p>Gestion des reportages photos des simulations, montages vidéos et chartes graphiques.</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Lien vers le drive des rushes photos/vidéos :")
        if st.button("Mettre à jour le lien média"):
            st.success("Lien mis à jour.")
    elif pwd != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 8. ESPACE ACADÉMIQUE / RÉDACTION (Sécurisé)
# ===================================================================
with tab_acad:
    st.markdown('<span class="badge-modern">PÔLE RÉDACTIONNEL</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Espace Chef Académique & Publication</div>', unsafe_allow_html=True)
    pwd = st.text_input("Mot de passe Académique :", type="password", key="pwd_acad")
    if pwd == "acad2026":
        st.success("Accès autorisé - Pôle Académique")
        
        with st.form("form_article_acad"):
            n_titre = st.text_input("Titre de l'article / Analyse")
            n_rubrique = st.selectbox("Rubrique", ["JURISPRUDENCE PÉNALE", "DROIT PUBLIC", "TRIBUNE LIBRE", "INTERNATIONAL"])
            n_auteur = st.text_input("Auteur / Pôle", value="Le Pôle Académique")
            n_contenu = st.text_area("Contenu complet de l'article")
            n_source_texte = st.text_input("Nom de la source (ex: Conseil d'État)")
            n_source_lien = st.text_input("Lien URL de la source")
            
            submit = st.form_submit_button("Publier l'article directement à la une")
            
            if submit:
                if n_titre and n_contenu:
                    nouvel_art = {
                        "titre": n_titre,
                        "rubrique": n_rubrique,
                        "auteur": n_auteur,
                        "date": datetime.now().strftime("%d %B %Y"),
                        "contenu": n_contenu.replace("\n", "<br>"),
                        "source_texte": n_source_texte,
                        "source_lien": n_source_lien
                    }
                    sauvegarder_article(nouvel_art)
                    st.success("🎉 Article publié avec succès à la une !")
                else:
                    st.error("Remplissez au moins le titre et le contenu.")
    elif pwd != "":
        st.error("Mot de passe incorrect.")
