import streamlit as st
import random
import time
from datetime import datetime

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau — Portail Exécutif",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------------
# DESIGN EDITORIAL INTERNE
# -------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    .stApp {
        background-color: #F4F6F9;
        color: #1A1D20;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        padding: 10px 0px 20px 0px;
        border-bottom: 2px solid #CBD5E1;
        margin-bottom: 30px;
    }
    
    .brand-logo {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: #0F172A;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 10px;
        margin-top: 10px;
    }

    .dashboard-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #0F172A;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.02);
    }
    
    .badge-role {
        background: #0F172A;
        color: #FFFFFF;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 6px 12px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .sidebar-brand {
        background: #334155;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Playfair Display', serif;
    }
</style>
""", unsafe_allow_html=True)

# Animation d'entrée
if 'welcome_exec_shown' not in st.session_state:
    time.sleep(0.5)
    st.toast("Portail sécurisé du Bureau Exécutif — Le Barreau", icon="🔒")
    st.session_state.welcome_exec_shown = True

# -------------------------------------------------------------------
# BARRE LATÉRALE
# -------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <h3 style="margin:0; color:#FFFFFF;">LE BARREAU</h3>
        <p style="font-size:0.8rem; margin:5px 0 0 0; color:#CBD5E1;">Espace Exécutif Réservé</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔐 Accès par Pôle")
    st.caption("Sélectionnez votre pôle dans l'onglet principal ci-contre et entrez votre code d'accès personnel.")
    st.markdown("---")
    st.caption("© 2026 Le Barreau. Bureau Exécutif.")

# -------------------------------------------------------------------
# EN-TÊTE PRINCIPAL
# -------------------------------------------------------------------
st.markdown(f"""
<div class="top-nav">
    <div class="brand-logo">PORTAIL EXÉCUTIF DU BUREAU</div>
    <div style="color: #64748B; font-size: 0.95rem; font-weight: 500;">
        Gestion interne • {datetime.now().strftime('%d %B %Y')}
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# LES 5 ONGLETS EXCLUSIFS DU BUREAU
# -------------------------------------------------------------------
tab_pres, tab_sec, tab_com, tab_media, tab_acad = st.tabs([
    "🏛️ Présidence", 
    "📋 Secrétariat Général", 
    "📢 Communication", 
    "🎬 Médias", 
    "📚 Académique"
])

# ===================================================================
# 1. PRÉSIDENCE
# ===================================================================
with tab_pres:
    st.markdown('<span class="badge-role">DIRECTION GÉNÉRALE</span>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Espace Présidence</div>', unsafe_allow_html=True)
    
    pwd_pres = st.text_input("Mot de passe Présidence :", type="password", key="input_pres")
    
    if pwd_pres == "pres2026":
        st.success("Accès autorisé. Bienvenue, Direction.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="dashboard-card">
                <h4>🎯 Pilotage Stratégique</h4>
                <p>Supervision globale des pôles, arbitrage des décisions et validation des partenariats institutionnels.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="dashboard-card">
                <h4>📊 Indicateurs Clés</h4>
                <p>• État des effectifs : Actif<br>• Prochaine réunion exécutive : Planifiée<br>• Budget global : Validé</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        st.subheader("📝 Notes et Directives de la Présidence")
        st.text_area("Rédiger une directive interne pour les chefs de pôle :")
        if st.button("Diffuser la directive"):
            st.success("Directive enregistrée et transmise au bureau.")
            
    elif pwd_pres != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 2. SECRÉTARIAT GÉNÉRAL
# ===================================================================
with tab_sec:
    st.markdown('<span class="badge-role">ADMINISTRATION & COMPTES-RENDUS</span>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Espace Secrétariat Général</div>', unsafe_allow_html=True)
    
    pwd_sec = st.text_input("Mot de passe Secrétariat :", type="password", key="input_sec")
    
    if pwd_sec == "sec2026":
        st.success("Accès autorisé. Bienvenue, Secrétariat Général.")
        
        st.markdown("""
        <div class="dashboard-card">
            <h4>📋 Gestion des Registres et PV</h4>
            <p>Consignation des procès-verbaux de réunions, gestion du répertoire des membres et suivi des présences.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.text_input("Ajouter un nouveau membre au registre officiel :", placeholder="Nom, Prénom, Pôle")
        st.text_area("Rédiger le Compte-Rendu (PV) de la dernière réunion :")
        
        if st.button("Archiver dans les registres"):
            st.success("Le document a été archivé avec succès dans la base administrative.")
            
    elif pwd_sec != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 3. COMMUNICATION
# ===================================================================
with tab_com:
    st.markdown('<span class="badge-role">RELATIONS PUBLQUES & SOCIALES</span>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Espace Chef Communication</div>', unsafe_allow_html=True)
    
    pwd_com = st.text_input("Mot de passe Communication :", type="password", key="input_com")
    
    if pwd_com == "com2026":
        st.success("Accès autorisé. Bienvenue, Pôle Communication.")
        
        st.markdown("""
        <div class="dashboard-card">
            <h4>📢 Planificateur de Campagnes</h4>
            <p>Coordination des publications sur les réseaux sociaux, annonces des événements et visibilité du club.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.selectbox("Plateforme cible", ["Instagram", "LinkedIn", "Affichage Interne / Affiches"])
        st.text_input("Titre de la publication / Annonce :")
        st.text_area("Légende / Texte de communication :")
        
        if st.button("Valider la campagne"):
            st.success("Campagne planifiée avec succès.")
            
    elif pwd_com != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 4. MÉDIAS
# ===================================================================
with tab_media:
    st.markdown('<span class="badge-role">AUDIOVISUEL & GRAPHISME</span>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Espace Chef Média</div>', unsafe_allow_html=True)
    
    pwd_media = st.text_input("Mot de passe Média :", type="password", key="input_media")
    
    if pwd_media == "media2026":
        st.success("Accès autorisé. Bienvenue, Pôle Média.")
        
        st.markdown("""
        <div class="dashboard-card">
            <h4>🎬 Gestion des Rushes et Visuels</h4>
            <p>Centralisation des photos de simulations, montages vidéos, graphismes et chartes visuelles du club.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.text_input("Lien de partage du Drive Média (Rushes / Photos) :", placeholder="https://drive.google.com/...")
        st.text_area("Notes de tournage ou instructions graphiques :")
        
        if st.button("Mettre à jour la base média"):
            st.success("Informations média mises à jour.")
            
    elif pwd_media != "":
        st.error("Mot de passe incorrect.")

# ===================================================================
# 5. ACADÉMIQUE
# ===================================================================
with tab_acad:
    st.markdown('<span class="badge-role">CONTENU JURIDIQUE & DÉBATS</span>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Espace Chef Académique</div>', unsafe_allow_html=True)
    
    pwd_acad = st.text_input("Mot de passe Académique :", type="password", key="input_acad")
    
    if pwd_acad == "acad2026":
        st.success("Accès autorisé. Bienvenue, Pôle Académique.")
        
        st.markdown("""
        <div class="dashboard-card">
            <h4>📚 Conception des Sujets et Fiches d'Arrêts</h4>
            <p>Préparation des cas pratiques, sélection des jurisprudences de référence et élaboration des sujets de débat.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.text_input("Intitulé du nouveau sujet de débat / cas pratique :")
        st.selectbox("Type de contenu académique", ["Sujet de Débat / Scrutin", "Fiche de Jurisprudence", "Cas Pratique Officiel"])
        st.text_area("Argumentaire ou description de la ressource juridique :")
        
        if st.button("Enregistrer la ressource académique"):
            st.success("Ressource enregistrée dans la base du pôle académique.")
            
    elif pwd_acad != "":
        st.error("Mot de passe incorrect.")
