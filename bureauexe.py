import streamlit as str_app
import time
import json
import os
from datetime import datetime, timedelta

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
str_app.set_page_config(
    page_title="Le Barreau — Portail Exécutif Unifié",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

PROPOSITIONS_FILE = "propositions_bureau.json"
PASSWORDS_FILE = "passwords_bureau.json"

# -------------------------------------------------------------------
# INITIALISATION DES RÔLES & MDP
# -------------------------------------------------------------------
DEFAUT_PASSWORDS = {
    "Présidence": "pres2026",
    "Secrétariat Général": "sec2026",
    "Chef Communication": "com2026",
    "Chef Média": "media2026",
    "Chef Académique": "acad2026",
    "Trésorier": "tres2026"
}

ROLE_POLE_MAP = {
    "Présidence": "🏛️ PRÉSIDENCE",
    "Secrétariat Général": "📋 SECRÉTARIAT",
    "Chef Communication": "📢 COMMUNICATION",
    "Chef Média": "🎬 MÉDIAS",
    "Chef Académique": "📚 ACADÉMIQUE",
    "Trésorier": "💶 TRÉSORERIE"
}

def charger_passwords():
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return DEFAUT_PASSWORDS
    return DEFAUT_PASSWORDS

def sauvegarder_password(role_key, nouveau_mdp):
    pwds = charger_passwords()
    pwds[role_key] = nouveau_mdp
    with open(PASSWORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(pwds, f, ensure_ascii=False, indent=4)

def charger_propositions():
    if os.path.exists(PROPOSITIONS_FILE):
        with open(PROPOSITIONS_FILE, "r", encoding="utf-8") as f:
            try:
                props = json.load(f)
            except json.JSONDecodeError:
                props = []
                
        maintenant = datetime.now()
        props_valides = []
        for p in props:
            if "date_raw" in p:
                try:
                    date_pub = datetime.strptime(p["date_raw"], "%Y-%m-%d %H:%M:%S")
                    if maintenant - date_pub < timedelta(hours=24):
                        props_valides.append(p)
                except ValueError:
                    continue
                    
        return props_valides
    return []

def sauvegarder_proposition(nouvelle_prop):
    props = charger_propositions()
    props.insert(0, nouvelle_prop)
    with open(PROPOSITIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(props, f, ensure_ascii=False, indent=4)

def enregistrer_vote(prop_id, choix, auteur_vote):
    props = charger_propositions()
    for p in props:
        if p["id"] == prop_id:
            if "votes" not in p:
                p["votes"] = {}
            p["votes"][auteur_vote] = choix
            break
    with open(PROPOSITIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(props, f, ensure_ascii=False, indent=4)

# -------------------------------------------------------------------
# GESTION SÉCURITÉ SESSION (10 MINUTES D'INACTIVITÉ)
# -------------------------------------------------------------------
SESSION_TIMEOUT = 600

if "logged_in_role" not in str_app.session_state:
    str_app.session_state.logged_in_role = None
if "last_activity" not in str_app.session_state:
    str_app.session_state.last_activity = time.time()

if str_app.session_state.logged_in_role:
    if time.time() - str_app.session_state.last_activity > SESSION_TIMEOUT:
        str_app.session_state.logged_in_role = None
        str_app.warning("⏱️ Votre session a expiré après 10 minutes d'inactivité.")
    else:
        str_app.session_state.last_activity = time.time()

# -------------------------------------------------------------------
# DESIGN & STYLING CSS (CORRECTION TOTALE DES MENUS DÉROULANTS)
# -------------------------------------------------------------------
str_app.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    .stApp {
        background-color: #233026;
        color: #FFFFFF;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    h1, h2, h3, h4, h5, h6, p, span, label, div, .stMarkdown, .stCaption, [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] {
        background-color: #1A241D !important;
        border-right: 1px solid #4A6B53;
    }

    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        padding: 10px 0px 20px 0px;
        border-bottom: 2px solid #4A6B53;
        margin-bottom: 30px;
    }
    
    .brand-logo {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #FFFFFF !important;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #FFFFFF !important;
        margin-bottom: 10px;
        margin-top: 10px;
    }

    .prop-card {
        background: #2E3F33;
        border: 1px solid #4A6B53;
        border-left: 5px solid #F4D03F;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    }
    
    .badge-role {
        background: #4A6B53;
        color: #FFFFFF !important;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 6px 12px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .sidebar-brand {
        background: #233026;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Playfair Display', serif;
        border: 1px solid #4A6B53;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #2E3F33 !important;
        color: #FFFFFF !important;
        border: 1px solid #628A6D !important;
    }

    /* CORRECTION DES BOÎTES DE SÉLECTION STREAMLIT POUR UN AFFICHAGE LISIBLE */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    div[data-baseweb="select"] span {
        color: #000000 !important;
    }

    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
        background-color: #FFFFFF !important;
    }

    li[role="option"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    li[role="option"]:hover {
        background-color: #E0E0E0 !important;
        color: #000000 !important;
    }
    
    .stButton button {
        background-color: #4A6B53;
        color: #FFFFFF;
        border: 1px solid #628A6D;
        font-weight: 600;
    }
    .stButton button:hover {
        background-color: #628A6D;
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# BARRE LATÉRALE
# -------------------------------------------------------------------
with str_app.sidebar:
    str_app.markdown("""
    <div class="sidebar-brand">
        <h3 style="margin:0; color:#FFFFFF;">LE BARREAU</h3>
        <p style="font-size:0.8rem; margin:5px 0 0 0; color:#FFFFFF;">Portail Exécutif</p>
    </div>
    """, unsafe_allow_html=True)
    
    str_app.markdown("---")
    if str_app.session_state.logged_in_role:
        str_app.markdown(f"🟢 Connecté en tant que :\n**{str_app.session_state.logged_in_role}**")
    else:
        str_app.markdown("🔴 Aucun utilisateur connecté.")
    str_app.markdown("---")
    str_app.markdown("### ⏱️ Règle des 24h")
    str_app.markdown("Toutes les annonces et votes expirent automatiquement après **24 heures**.")
    str_app.markdown("---")
    str_app.caption("© 2026 Le Barreau. Bureau Exécutif.")

# -------------------------------------------------------------------
# EN-TÊTE PRINCIPAL
# -------------------------------------------------------------------
str_app.markdown(f"""
<div class="top-nav">
    <div class="brand-logo">LE BARREAU — PORTAIL EXÉCUTIF</div>
    <div style="color: #FFFFFF; font-size: 0.95rem; font-weight: 600;">
        {datetime.now().strftime('%d %B %Y')}
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# LES 2 ONGLETS UNIQUES
# -------------------------------------------------------------------
tab_canal, tab_login = str_app.tabs([
    "🌐 Canal Général & Votes",
    "🔑 Connexion & Publication"
])

# ===================================================================
# 1. CANAL GÉNÉRAL & VOTES
# ===================================================================
with tab_canal:
    str_app.markdown('<span class="badge-role">FIL D\'ACTUALITÉ & COLLÉGIALITÉ</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Canal Général des Annonces</div>', unsafe_allow_html=True)
    str_app.markdown("Consultez les annonces de chaque pôle et participez aux votes proposés (**un seul vote par utilisateur et par annonce**). Les publications disparaissent au bout de **24h**.")
    
    propositions = charger_propositions()
    
    if not propositions:
        str_app.info("𭕡 Aucune annonce active pour le moment. Rendez-vous dans l'onglet *Connexion & Publication* pour en poster une avec un vote.")
    else:
        str_app.markdown("---")
        for p in propositions:
            votes_actuels = p.get("votes", {})
            type_vote = p.get("type_vote", "POUR/CONTRE")
            options_personnalisees = p.get("options_vote", ["POUR", "CONTRE"])
            
            str_app.markdown(f"""
            <div class="prop-card">
                <span style="background: #1A241D; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: bold;">{p['pole']}</span>
                <h3 style="margin-top: 10px; font-family: 'Playfair Display', serif; color: #FFFFFF;">{p['titre']}</h3>
                <p style="color: #FFFFFF; font-size: 1.05rem;">{p['contenu']}</p>
                <p style="font-size: 0.85rem; color: #D8F3DC;">Publié par <b>{p['auteur']}</b> le {p['date_aff']} | 🗳️ Type de vote : <b>{type_vote}</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            str_app.markdown("📊 **Résultats des votes :**")
            if votes_actuels:
                cols_v = str_app.columns(max(len(votes_actuels), 1))
                idx = 0
                for pers, choix in votes_actuels.items():
                    with cols_v[idx]:
                        str_app.markdown(f"• **{pers}** : `{choix}`")
                    idx += 1
            else:
                str_app.caption("Aucun vote enregistré pour l'instant.")
                
            if str_app.session_state.logged_in_role:
                user_actuel = str_app.session_state.logged_in_role
                deja_vote = user_actuel in votes_actuels
                
                if deja_vote:
                    str_app.info(f"✅ Vous avez voté (**{votes_actuels[user_actuel]}**) avec votre profil ({user_actuel}).")
                else:
                    str_app.markdown("👉 **Faites votre choix :**")
                    cols_choix = str_app.columns(len(options_personnalisees))
                    for i, opt in enumerate(options_personnalisees):
                        with cols_choix[i]:
                            if str_app.button(f"Voter {opt}", key=f"vote_{p['id']}_{opt}_{user_actuel}"):
                                enregistrer_vote(p['id'], opt, user_actuel)
                                str_app.success(f"Votre vote '{opt}' a bien été pris en compte !")
                                str_app.rerun()
            else:
                str_app.warning("🔒 Connectez-vous dans l'onglet **Connexion & Publication** pour pouvoir voter avec votre profil.")
                
            str_app.markdown("---")

# ===================================================================
# 2. CONNEXION & PUBLICATION
# ===================================================================
with tab_login:
    str_app.markdown('<span class="badge-role">ESPACE SÉCURISÉ DU MEMBRE</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Connexion & Publication d\'Annonce avec Vote</div>', unsafe_allow_html=True)
    
    passwords = charger_passwords()
    
    if not str_app.session_state.logged_in_role:
        str_app.write("Veuillez sélectionner votre rôle et saisir votre mot de passe pour accéder à votre espace de publication.")
        
        with str_app.form("form_login"):
            role_choisi = str_app.selectbox("Sélectionnez votre rôle :", list(DEFAUT_PASSWORDS.keys()))
            mdp_saisi = str_app.text_input("Mot de passe :", type="password")
            btn_login = str_app.form_submit_button("Se connecter")
            
            if btn_login:
                if mdp_saisi == passwords.get(role_choisi):
                    str_app.session_state.logged_in_role = role_choisi
                    str_app.session_state.last_activity = time.time()
                    str_app.success(f"🎉 Connexion réussie en tant que {role_choisi} !")
                    str_app.rerun()
                else:
                    str_app.error("❌ Mot de passe incorrect.")
    else:
        role_actif = str_app.session_state.logged_in_role
        str_app.success(f"🟢 Vous êtes actuellement connecté en tant que : **{role_actif}**")
        
        c_l1, c_l2 = str_app.columns(2)
        with c_l1:
            if str_app.button("🔒 Verrouiller / Se déconnecter manuellement"):
                str_app.session_state.logged_in_role = None
                str_app.rerun()
                
        str_app.markdown("---")
        
        with str_app.expander("🔑 Modifier mon mot de passe"):
            with str_app.form("form_change_pwd"):
                ancien_p = str_app.text_input("Ancien mot de passe", type="password")
                nouveau_p1 = str_app.text_input("Nouveau mot de passe", type="password")
                nouveau_p2 = str_app.text_input("Confirmer le nouveau mot de passe", type="password")
                btn_pwd = str_app.form_submit_button("Mettre à jour le mot de passe")
                
                if btn_pwd:
                    if ancien_p != passwords.get(role_actif):
                        str_app.error("L'ancien mot de passe est incorrect.")
                    elif not nouveau_p1:
                        str_app.error("Le mot de passe ne peut pas être vide.")
                    elif nouveau_p1 != nouveau_p2:
                        str_app.error("Les nouveaux mots de passe ne correspondent pas.")
                    else:
                        sauvegarder_password(role_actif, nouveau_p1)
                        str_app.success("🎉 Mot de passe mis à jour avec succès !")
        
        str_app.markdown("---")
        str_app.markdown(f"### 📢 Publier une annonce et configurer le vote ({role_actif})")
        str_app.write("Rédigez votre annonce et définissez le format de vote que les membres devront utiliser.")
        
        with str_app.form("form_pub_directe"):
            titre_prop = str_app.text_input("Titre de l'annonce / projet / proposition")
            contenu_prop = str_app.text_area("Contenu détaillé")
            
            str_app.markdown("---")
            str_app.markdown("**⚙️ Configuration du vote associé :**")
            type_vote_choisi = str_app.selectbox(
                "Type de vote pour cette annonce :", 
                ["Classique (POUR / CONTRE)", "Personnalisé (Ex: Favorable / Réservé / Contre)", "Approbation simple (VALIDER)"]
            )
            
            options_personnalisees_saisies = str_app.text_input(
                "Options de vote personnalisées (séparées par des virgules)", 
                value="POUR, CONTRE" if type_vote_choisi.startswith("Classique") else "Favorable, Réservé, Contre" if type_vote_choisi.startswith("Personnalisé") else "VALIDE"
            )
            
            btn_pub = str_app.form_submit_button("Diffuser l'annonce et son vote sur le Canal Général")
            
            if btn_pub:
                if not titre_prop or not contenu_prop:
                    str_app.error("Veuillez remplir le titre et le contenu de l'annonce.")
                else:
                     options_finales = [opt.strip() for opt in options_personnalisees_saisies.split(",") if opt.strip()]
                     maintenant_dt = datetime.now()
                     
                     nouvelle = {
                        "id": str(int(time.time() * 1000)),
                        "pole": ROLE_POLE_MAP.get(role_actif, "📄 BUREAU"),
                        "auteur": role_actif,
                        "titre": titre_prop,
                        "contenu": contenu_prop,
                        "type_vote": type_vote_choisi,
                        "options_vote": options_finales,
                        "date_raw": maintenant_dt.strftime("%Y-%m-%d %H:%M:%S"),
                        "date_aff": maintenant_dt.strftime("%d/%m/%Y à %H:%M"),
                        "votes": {}
                    }
                     sauvegarder_proposition(nouvelle)
                     str_app.success("🎉 Annonce et système de vote publiés avec succès ! Rendez-vous sur l'onglet 'Canal Général & Votes'.")
