import streamlit as str_app
import random
import time
import json
import os
from datetime import datetime

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
str_app.set_page_config(
    page_title="Le Barreau — Portail Exécutif & Canal Général",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

PROPOSITIONS_FILE = "propositions_bureau.json"
PASSWORDS_FILE = "passwords_bureau.json"

# -------------------------------------------------------------------
# GESTION DES MOTS DE PASSE (PERSISTANTS)
# -------------------------------------------------------------------
DEFAUT_PASSWORDS = {
    "pres": "pres2026",
    "sec": "sec2026",
    "com": "com2026",
    "media": "media2026",
    "acad": "acad2026",
    "tres": "tres2026"
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

# -------------------------------------------------------------------
# GESTION DU STOCKAGE DES PROPOSITIONS (CANAL GÉNÉRAL)
# -------------------------------------------------------------------
def charger_propositions():
    if os.path.exists(PROPOSITIONS_FILE):
        with open(PROPOSITIONS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
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
# GESTION DE LA SÉCURITÉ ET DU TEMPS (EXPIRATION 10 MINUTES)
# -------------------------------------------------------------------
SESSION_TIMEOUT = 600  # 600 secondes = 10 minutes

def verifier_session(role_nom):
    cle_temps = f"time_{role_nom}"
    cle_auth = f"auth_{role_nom}"
    
    if cle_temps in str_app.session_state and cle_auth in str_app.session_state and str_app.session_state[cle_auth]:
        ecoule = time.time() - str_app.session_state[cle_temps]
        if ecoule > SESSION_TIMEOUT:
            str_app.session_state[cle_auth] = False
            str_app.warning("⏱️ Votre session a expiré (plus de 10 minutes d'inactivité). Veuillez ressaisir votre mot de passe.")

# -------------------------------------------------------------------
# DESIGN VERT KAKI ULTRA-LISIBLE & PEP'S (CSS CORRIGÉ)
# -------------------------------------------------------------------
str_app.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    .stApp {
        background-color: #233026; /* Fond général vert très sombre et contrasté */
        color: #FFFFFF;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Forcer TOUS les textes en blanc éclatant ou quasi-blanc pour une lisibilité parfaite */
    h1, h2, h3, h4, h5, h6, p, span, label, div, .stMarkdown, .stCaption {
        color: #FFFFFF !important;
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
        letter-spacing: -0.5px;
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

    .dashboard-card {
        background: #2E3F33;
        border: 1px solid #4A6B53;
        border-top: 4px solid #A3B18B;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
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
        background: #1A241D;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Playfair Display', serif;
        border: 1px solid #4A6B53;
    }

    /* Style des champs de saisie pour un contraste parfait */
    .stTextInput input, .stTextArea textarea {
        background-color: #2E3F33 !important;
        color: #FFFFFF !important;
        border: 1px solid #628A6D !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #2E3F33 !important;
        color: #FFFFFF !important;
        border: 1px solid #628A6D !important;
    }
    
    /* Boutons stylisés */
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

# Animation d'entrée
if 'welcome_exec_shown' not in str_app.session_state:
    time.sleep(0.5)
    str_app.toast("Portail sécurisé du Bureau Exécutif — Le Barreau", icon="⚖️")
    str_app.session_state.welcome_exec_shown = True

# -------------------------------------------------------------------
# BARRE LATÉRALE
# -------------------------------------------------------------------
with str_app.sidebar:
    str_app.markdown("""
    <div class="sidebar-brand">
        <h3 style="margin:0; color:#FFFFFF;">LE BARREAU</h3>
        <p style="font-size:0.8rem; margin:5px 0 0 0; color:#E2E8F0;">Portail Exécutif Unifié</p>
    </div>
    """, unsafe_allow_html=True)
    
    str_app.markdown("---")
    str_app.markdown("### 📡 Canal Général")
    str_app.caption("Consultez et publiez des annonces en temps réel pour validation collégiale.")
    str_app.markdown("---")
    str_app.markdown("### ⏱️ Sécurité Session")
    str_app.caption("Chaque session expire automatiquement après **10 minutes** d'inactivité.")
    str_app.markdown("---")
    str_app.caption("© 2026 Le Barreau. Bureau Exécutif.")

# -------------------------------------------------------------------
# EN-TÊTE PRINCIPAL
# -------------------------------------------------------------------
str_app.markdown(f"""
<div class="top-nav">
    <div class="brand-logo">PORTAIL EXÉCUTIF & CANAL GÉNÉRAL</div>
    <div style="color: #FFFFFF; font-size: 0.95rem; font-weight: 600;">
        {datetime.now().strftime('%d %B %Y')}
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# LES 7 ONGLETS (6 PÔLES + 1 CANAL GÉNÉRAL)
# -------------------------------------------------------------------
tab_canal, tab_pres, tab_sec, tab_com, tab_media, tab_acad, tab_tres = str_app.tabs([
    "🌐 Canal Général & Votes",
    "🏛️ Présidence", 
    "📋 Secrétariat", 
    "📢 Communication", 
    "🎬 Médias", 
    "📚 Académique",
    "💶 Trésorerie"
])

# ===================================================================
# FONCTION HELPER POUR GÉRER LA MODIFICATION DE MOT DE PASSE
# ===================================================================
def render_password_change_section(role_key, role_label):
    passwords_actuels = charger_passwords()
    with str_app.expander(f"🔑 Modifier mon mot de passe ({role_label})"):
        with str_app.form(f"form_change_pwd_{role_key}"):
            ancien = str_app.text_input("Ancien mot de passe :", type="password", key=f"old_{role_key}")
            nouveau1 = str_app.text_input("Nouveau mot de passe :", type="password", key=f"new1_{role_key}")
            nouveau2 = str_app.text_input("Confirmer le nouveau mot de passe :", type="password", key=f"new2_{role_key}")
            btn_submit_pwd = str_app.form_submit_button("Mettre à jour le mot de passe")
            
            if btn_submit_pwd:
                if ancien != passwords_actuels.get(role_key):
                    str_app.error("L'ancien mot de passe est incorrect.")
                elif not nouveau1:
                    str_app.error("Le nouveau mot de passe ne peut pas être vide.")
                elif nouveau1 != nouveau2:
                    str_app.error("Les deux nouveaux mots de passe ne correspondent pas.")
                else:
                    sauvegarder_password(role_key, nouveau1)
                    str_app.success("🎉 Mot de passe mis à jour avec succès !")

# ===================================================================
# 0. CANAL GÉNÉRAL & PUBLICATION RAPIDE / VOTES
# ===================================================================
with tab_canal:
    str_app.markdown('<span class="badge-role">FIL COMMUN DU BUREAU</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Canal Général & Annonces</div>', unsafe_allow_html=True)
    str_app.write("Publiez directement vos annonces, légendes ou propositions ici, et consultez les votes du bureau en temps réel.")
    
    # BOÎTE DE PUBLICATION DIRECTE DEPUIS LE CANAL GÉNÉRAL
    with str_app.expander("➕ Publier une nouvelle annonce / proposition sur le canal", expanded=False):
        with str_app.form("form_pub_rapide"):
            p_pole = str_app.selectbox("Sélectionnez votre pôle émetteur :", [
                "🏛️ PRÉSIDENCE", 
                "📋 SECRÉTARIAT", 
                "📢 COMMUNICATION", 
                "🎬 MÉDIAS", 
                "📚 ACADÉMIQUE", 
                "💶 TRÉSORERIE"
            ])
            p_auteur = str_app.text_input("Votre nom ou rôle exact (ex: Chef Communication)")
            p_titre = str_app.text_input("Titre de l'annonce / projet / légende")
            p_contenu = str_app.text_area("Contenu détaillé de la proposition")
            
            btn_publier = str_app.form_submit_button("Diffuser sur le Canal Général")
            
            if btn_publier and p_titre and p_contenu and p_auteur:
                nouvelle = {
                    "id": str(random.randint(1000, 9999)),
                    "pole": p_pole,
                    "auteur": p_auteur,
                    "titre": p_titre,
                    "contenu": p_contenu,
                    "date": datetime.now().strftime("%d/%m/%Y à %H:%M"),
                    "votes": {}
                }
                sauvegarder_proposition(nouvelle)
                str_app.success("🎉 Annonce publiée avec succès sur le canal général !")
                str_app.rerun()

    str_app.markdown("---")
    str_app.subheader("📋 Fil d'actualité et Votes en cours")
    
    propositions = charger_propositions()
    
    if not propositions:
        str_app.info("Aucune annonce active pour le moment.")
    else:
        votant_nom = str_app.selectbox("Sélectionnez votre identité pour voter :", [
            "Choisissez...", 
            "Présidence", 
            "Secrétariat Général", 
            "Chef Communication", 
            "Chef Média", 
            "Chef Académique", 
            "Trésorier"
        ])
        
        str_app.markdown("---")
        
        for p in propositions:
            votes_actuels = p.get("votes", {})
            str_app.markdown(f"""
            <div class="prop-card">
                <span style="background: #1A241D; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: bold;">{p['pole']}</span>
                <h3 style="margin-top: 10px; font-family: 'Playfair Display', serif; color: #FFFFFF;">{p['titre']}</h3>
                <p style="color: #FFFFFF; font-size: 1.05rem;">{p['contenu']}</p>
                <p style="font-size: 0.85rem; color: #D8F3DC;">Publié par <b>{p['auteur']}</b> le {p['date']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            str_app.write("📊 **Votes actuels :**")
            if votes_actuels:
                cols_v = str_app.columns(len(votes_actuels))
                idx = 0
                for pers, choix in votes_actuels.items():
                    with cols_v[idx]:
                        couleur = "lightgreen" if choix == "POUR" else "lightcoral"
                        str_app.markdown(f"• **{pers}** : :{couleur}[{choix}]")
                    idx += 1
            else:
                str_app.caption("Aucun vote enregistré pour l'instant.")
                
            if votant_nom != "Choisissez...":
                c_v1, c_v2 = str_app.columns(2)
                with c_v1:
                    if str_app.button(f"✅ Voter POUR ({p['id']})", key=f"pour_{p['id']}"):
                        enregistrer_vote(p['id'], "POUR", votant_nom)
                        str_app.success("Votre vote 'POUR' a été pris en compte !")
                        str_app.rerun()
                with c_v2:
                    if str_app.button(f"❌ Voter CONTRE ({p['id']})", key=f"contre_{p['id']}"):
                        enregistrer_vote(p['id'], "CONTRE", votant_nom)
                        str_app.warning("Votre vote 'CONTRE' a été pris en compte.")
                        str_app.rerun()
            else:
                str_app.caption("⚠️ Veuillez sélectionner votre nom ci-dessus pour pouvoir voter.")
                
            str_app.markdown("---")

# ===================================================================
# 1. PRÉSIDENCE
# ===================================================================
with tab_pres:
    verifier_session("pres")
    str_app.markdown('<span class="badge-role">DIRECTION GÉNÉRALE</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Espace Présidence</div>', unsafe_allow_html=True)
    
    passwords = charger_passwords()
    pwd_pres = str_app.text_input("Mot de passe Présidence :", type="password", key="input_pres")
    
    if pwd_pres == passwords["pres"]:
        str_app.session_state["auth_pres"] = True
        if "time_pres" not in str_app.session_state:
            str_app.session_state["time_pres"] = time.time()
            
        str_app.success("Accès autorisé. Session active (10 minutes).")
        
        if str_app.button("🔒 Verrouiller manuellement ma session Présidence", key="lock_pres"):
            str_app.session_state["auth_pres"] = False
            str_app.rerun()
            
        str_app.markdown("---")
        render_password_change_section("pres", "Présidence")
    elif pwd_pres != "":
        str_app.error("Mot de passe incorrect.")

# ===================================================================
# 2. SECRÉTARIAT GÉNÉRAL
# ===================================================================
with tab_sec:
    verifier_session("sec")
    str_app.markdown('<span class="badge-role">ADMINISTRATION & COMPTES-RENDUS</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Espace Secrétariat Général</div>', unsafe_allow_html=True)
    
    passwords = charger_passwords()
    pwd_sec = str_app.text_input("Mot de passe Secrétariat :", type="password", key="input_sec")
    
    if pwd_sec == passwords["sec"]:
        str_app.session_state["auth_sec"] = True
        if "time_sec" not in str_app.session_state:
            str_app.session_state["time_sec"] = time.time()
            
        str_app.success("Accès autorisé. Session active (10 minutes).")
        
        if str_app.button("🔒 Verrouiller ma session Secrétariat", key="lock_sec"):
            str_app.session_state["auth_sec"] = False
            str_app.rerun()
            
        str_app.markdown("---")
        render_password_change_section("sec", "Secrétariat Général")
    elif pwd_sec != "":
        str_app.error("Mot de passe incorrect.")

# ===================================================================
# 3. COMMUNICATION
# ===================================================================
with tab_com:
    verifier_session("com")
    str_app.markdown('<span class="badge-role">RELATIONS PUBLQUES & SOCIALES</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Espace Chef Communication</div>', unsafe_allow_html=True)
    
    passwords = charger_passwords()
    pwd_com = str_app.text_input("Mot de passe Communication :", type="password", key="input_com")
    
    if pwd_com == passwords["com"]:
        str_app.session_state["auth_com"] = True
        if "time_com" not in str_app.session_state:
            str_app.session_state["time_com"] = time.time()
            
        str_app.success("Accès autorisé. Session active (10 minutes).")
        
        if str_app.button("🔒 Verrouiller ma session Communication", key="lock_com"):
            str_app.session_state["auth_com"] = False
            str_app.rerun()
            
        str_app.markdown("---")
        render_password_change_section("com", "Communication")
    elif pwd_com != "":
        str_app.error("Mot de passe incorrect.")

# ===================================================================
# 4. MÉDIAS
# ===================================================================
with tab_media:
    verifier_session("media")
    str_app.markdown('<span class="badge-role">AUDIOVISUEL & GRAPHISME</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Espace Chef Média</div>', unsafe_allow_html=True)
    
    passwords = charger_passwords()
    pwd_media = str_app.text_input("Mot de passe Média :", type="password", key="input_media")
    
    if pwd_media == passwords["media"]:
        str_app.session_state["auth_media"] = True
        if "time_media" not in str_app.session_state:
            str_app.session_state["time_media"] = time.time()
            
        str_app.success("Accès autorisé. Session active (10 minutes).")
        
        if str_app.button("🔒 Verrouiller ma session Média", key="lock_media"):
            str_app.session_state["auth_media"] = False
            str_app.rerun()
            
        str_app.markdown("---")
        render_password_change_section("media", "Médias")
    elif pwd_media != "":
        str_app.error("Mot de passe incorrect.")

# ===================================================================
# 5. ACADÉMIQUE
# ===================================================================
with tab_acad:
    verifier_session("acad")
    str_app.markdown('<span class="badge-role">CONTENU JURIDIQUE & DÉBATS</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Espace Chef Académique</div>', unsafe_allow_html=True)
    
    passwords = charger_passwords()
    pwd_acad = str_app.text_input("Mot de passe Académique :", type="password", key="input_acad")
    
    if pwd_acad == passwords["acad"]:
        str_app.session_state["auth_acad"] = True
        if "time_acad" not in str_app.session_state:
            str_app.session_state["time_acad"] = time.time()
            
        str_app.success("Accès autorisé. Session active (10 minutes).")
        
        if str_app.button("🔒 Verrouiller ma session Académique", key="lock_acad"):
            str_app.session_state["auth_acad"] = False
            str_app.rerun()
            
        str_app.markdown("---")
        render_password_change_section("acad", "Académique")
    elif pwd_acad != "":
        str_app.error("Mot de passe incorrect.")

# ===================================================================
# 6. TRÉSORERIE
# ===================================================================
with tab_tres:
    verifier_session("tres")
    str_app.markdown('<span class="badge-role">FINANCES & BUDGET</span>', unsafe_allow_html=True)
    str_app.markdown('<div class="section-title">Espace Trésorerie</div>', unsafe_allow_html=True)
    
    passwords = charger_passwords()
    pwd_tres = str_app.text_input("Mot de passe Trésorerie :", type="password", key="input_tres")
    
    if pwd_tres == passwords["tres"]:
        str_app.session_state["auth_tres"] = True
        if "time_tres" not in str_app.session_state:
            str_app.session_state["time_tres"] = time.time()
            
        str_app.success("Accès autorisé. Session active (10 minutes).")
        
        if str_app.button("🔒 Verrouiller ma session Trésorerie", key="lock_tres"):
            str_app.session_state["auth_tres"] = False
            str_app.rerun()
            
        str_app.markdown("---")
        render_password_change_section("tres", "Trésorerie")
    elif pwd_tres != "":
        str_app.error("Mot de passe incorrect.")
