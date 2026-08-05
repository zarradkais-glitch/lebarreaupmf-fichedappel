import streamlit as st
import datetime
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ==============================================================================
# CONFIGURATION DE LA PAGE STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="Le Barreau PMF - Gestion des Présences",
    page_icon="⚖️",
    layout="wide"
)

# Fichiers de sauvegarde permanente sur le disque
FICHIER_MEMBRES = "membres.json"
FICHIER_HISTORIQUE = "historique_seances.json"

# ==============================================================================
# FONCTIONS DE SAUVEGARDE ET CHARGEMENT PERMANENT (JSON)
# ==============================================================================
def charger_donnees():
    if os.path.exists(FICHIER_MEMBRES):
        with open(FICHIER_MEMBRES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def sauvegarder_donnees(membres):
    with open(FICHIER_MEMBRES, "w", encoding="utf-8") as f:
        json.dump(membres, f, ensure_ascii=False, indent=4)

def sauvegarder_seance(date_seance, responsable, compte_rendu):
    historique = []
    if os.path.exists(FICHIER_HISTORIQUE):
        with open(FICHIER_HISTORIQUE, "r", encoding="utf-8") as f:
            historique = json.load(f)
            
    historique.append({
        "date": str(date_seance),
        "responsable": responsable,
        "details": compte_rendu
    })
    
    with open(FICHIER_HISTORIQUE, "w", encoding="utf-8") as f:
        json.dump(historique, f, ensure_ascii=False, indent=4)

# Initialisation de la session avec les données sauvegardées
if "membres" not in st.session_state:
    st.session_state.membres = charger_donnees()

# ==============================================================================
# FONCTION SMTP (ENVOI D'EMAILS)
# ==============================================================================
def envoyer_email_smtp(destinataire, sujet, corps):
    expediteur = st.secrets.get("GMAIL_USER", "ton.email@gmail.com")
    mot_de_passe = st.secrets.get("GMAIL_PASSWORD", "votre_code_application")

    msg = MIMEMultipart()
    msg['From'] = expediteur
    msg['To'] = destinataire
    msg['Subject'] = sujet
    msg.attach(MIMEText(corps, 'plain', 'utf-8'))

    try:
        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login(expediteur, mot_de_passe)
        serveur.send_message(msg)
        serveur.quit()
        return True, "E-mail envoyé avec succès !"
    except Exception as e:
        return False, str(e)

# ==============================================================================
# EN-TÊTE PRINCIPAL
# ==============================================================================
st.title("⚖️ Le Barreau PMF — Portal Administratif")
st.caption("Gestion officielle des séances, présences et rôles du club.")

# ==============================================================================
# ONGLETS DE NAVIGATION
# ==============================================================================
tab_appel, tab_liste, tab_ajouter, tab_historique = st.tabs([
    "📋 Prise d'Appel", 
    "📊 Registre & Statuts", 
    "➕ Ajouter un Membre",
    "📜 Historique des Séances"
])

# ------------------------------------------------------------------------------
# ONGLET 1 : PRISE D'APPEL AVEC EN-TÊTE PERSONNALISÉ
# ------------------------------------------------------------------------------
with tab_appel:
    st.subheader("📌 Informations de la Séance")
    
    col_resp, col_date = st.columns(2)
    with col_resp:
        responsable_seance = st.text_input("👤 Responsable / Gérant de la séance :", placeholder="ex: Kaïs Zarrad")
    with col_date:
        date_seance = st.date_input("📅 Date de la séance :", value=datetime.date.today())

    st.divider()

    if not st.session_state.membres:
        st.info("💡 Aucun membre n'est encore inscrit dans le registre. Rendez-vous dans l'onglet **'➕ Ajouter un Membre'** pour enregistrer vos premiers membres !")
    else:
        st.subheader("📝 Registre d'Appel")
        with st.form("form_appel"):
            resultats_appel = {}
            
            for idx, membre in enumerate(st.session_state.membres):
                c1, c2 = st.columns([3, 2])
                with c1:
                    st.write(f"**{membre['nom']}** — *{membre['role']}*")
                    st.caption(f"📧 {membre['email']} | Total actuel : {membre['absences']} abs.")
                with c2:
                    statut = st.radio(
                        "Statut",
                        ["Présent(e)", "Absent(e)"],
                        key=f"radio_{idx}",
                        horizontal=True,
                        label_visibility="collapsed"
                    )
                    resultats_appel[membre["id"]] = statut
                st.divider()

            soumis = st.form_submit_button("💾 Valider & Sauvegarder la Séance", type="primary")

        if soumis:
            if not responsable_seance:
                st.error("⚠️ Veuillez indiquer le nom du responsable de la séance avant de valider.")
            else:
                alertes_mails = []
                compte_rendu = []

                for membre in st.session_state.membres:
                    statut = resultats_appel.get(membre["id"])
                    compte_rendu.append({"nom": membre["nom"], "statut": statut})

                    if statut == "Présent(e)":
                        membre["presences"] += 1
                        if membre["presences"] == 5:
                            sujet = "🏆 [Le Barreau] Félicitations pour votre assiduité !"
                            corps = f"Bravo {membre['nom']} !\n\nTu comptabilises 5 présences au Barreau PMF. Tu obtiens la priorité sur les rôles principaux pour les prochains procès !\n\nLe Bureau du Barreau."
                            alertes_mails.append((membre, sujet, corps, "Fidélité"))
                    else:
                        membre["absences"] += 1
                        if membre["absences"] == 1:
                            sujet = "[Le Barreau PMF] Absence à la séance"
                            corps = f"Bonjour {membre['nom']},\n\nTon absence a été notée pour la séance du {date_seance} tenue par {responsable_seance}.\nPense à nous prévenir en cas d'empêchement !"
                            alertes_mails.append((membre, sujet, corps, "Rappel (1 abs.)"))
                        elif membre["absences"] in [2, 3]:
                            sujet = "⚠️ [AVERTISSEMENT] Cumul d'absences au Barreau"
                            corps = f"Bonjour {membre['nom']},\n\nTu cumules {membre['absences']} absences. Ceci constitue un AVERTISSEMENT OFFICIEL.\nÀ la 4ème absence, l'exclusion sera appliquée.\n\nLe Bureau du Barreau."
                            alertes_mails.append((membre, sujet, corps, "Avertissement (2-3 abs.)"))
                        elif membre["absences"] >= 4:
                            sujet = "🚨 [NOTIFICATION OFFICIELLE] Exclusion du Barreau"
                            corps = f"Bonjour {membre['nom']},\n\nAvec {membre['absences']} absences, nous t'informons de ton exclusion du club pour ce semestre.\n\nLa Présidence du Barreau PMF."
                            alertes_mails.append((membre, sujet, corps, "Exclusion (4+ abs.)"))

                # Sauvegarde permanente dans les fichiers JSON
                sauvegarder_donnees(st.session_state.membres)
                sauvegarder_seance(date_seance, responsable_seance, compte_rendu)
                
                st.success(f"✅ Séance du {date_seance} gérée par {responsable_seance} enregistrée avec succès dans la base de données !")

                # Affichage des e-mails à envoyer
                if alertes_mails:
                    st.subheader("📬 Notifications Automatiques")
                    for membre, sujet, corps, type_mail in alertes_mails:
                        with st.expander(f"✉️ {type_mail} ➔ {membre['nom']} ({membre['email']})"):
                            st.text_area("Sujet", sujet, height=60, key=f"sujet_{membre['id']}")
                            st.text_area("Message", corps, height=140, key=f"corps_{membre['id']}")
                            if st.button(f"🚀 Envoyer à {membre['nom']}", key=f"btn_{membre['id']}"):
                                s, msg = envoyer_email_smtp(membre['email'], sujet, corps)
                                if s:
                                    st.success(f"Email envoyé à {membre['email']} !")
                                else:
                                    st.info(f"Notification générée. (Configurez les clés SMTP pour un envoi direct).")

# ------------------------------------------------------------------------------
# ONGLET 2 : REGISTRE & GESTION DES MEMBRES
# ------------------------------------------------------------------------------
with tab_liste:
    st.subheader("📋 Annuaire & Bilan des Membres")
    
    if not st.session_state.membres:
        st.write("Aucun membre inscrit pour le moment.")
    else:
        for idx, membre in enumerate(st.session_state.membres):
            c1, c2, c3, c4, c5 = st.columns([3, 1, 1, 2, 1])
            c1.write(f"**{membre['nom']}**\n*{membre['role']}* | `{membre['email']}`")
            c2.metric("Présences", membre['presences'])
            c3.metric("Absences", membre['absences'])
            
            if membre['absences'] >= 4:
                c4.error("🚨 Exclu(e)")
            elif membre['absences'] >= 2:
                c4.warning("⚠️ Avertissement")
            elif membre['presences'] >= 5:
                c4.success("🌟 Membre d'Élite")
            else:
                c4.info("✅ Actif")
                
            if c5.button("🗑️ Supprimer", key=f"del_{idx}"):
                st.session_state.membres.pop(idx)
                sauvegarder_donnees(st.session_state.membres)
                st.rerun()

            st.divider()

# ------------------------------------------------------------------------------
# ONGLET 3 : AJOUTER UN MEMBRE
# ------------------------------------------------------------------------------
with tab_ajouter:
    st.subheader("➕ Inscrire un membre ou responsable")
    
    roles_disponibles = [
        "Membre",
        "Président",
        "Secrétaire",
        "Chef Communication",
        "Chef Académique",
        "Chef Média",
        "Trésorier"
    ]
    
    with st.form("form_nouveau"):
        nom_saisi = st.text_input("Nom et Prénom :")
        email_saisi = st.text_input("Adresse E-mail :")
        role_saisi = st.selectbox("Rôle dans le club :", roles_disponibles)
        
        bouton_ajouter = st.form_submit_button("Ajouter au Barreau PMF", type="primary")
        
        if bouton_ajouter:
            if nom_saisi and email_saisi:
                nouvel_id = f"m{len(st.session_state.membres) + 1}_{datetime.datetime.now().strftime('%H%M%S')}"
                st.session_state.membres.append({
                    "id": nouvel_id,
                    "nom": nom_saisi,
                    "email": email_saisi,
                    "role": role_saisi,
                    "presences": 0,
                    "absences": 0
                })
                sauvegarder_donnees(st.session_state.membres)
                st.success(f"🎉 {nom_saisi} ({role_saisi}) a été ajouté(e) au Barreau et sauvegardé(e) !")
                st.rerun()
            else:
                st.error("Veuillez renseigner au moins le nom et l'adresse e-mail.")

# ------------------------------------------------------------------------------
# ONGLET 4 : HISTORIQUE DES SÉANCES ARCHIVÉES
# ------------------------------------------------------------------------------
with tab_historique:
    st.subheader("📜 Archives des séances enregistrées")
    if os.path.exists(FICHIER_HISTORIQUE):
        with open(FICHIER_HISTORIQUE, "r", encoding="utf-8") as f:
            historique = json.load(f)
            
        for s in reversed(historique):
            with st.expander(f"🗓️ Séance du {s['date']} — Gérée par : {s['responsable']}"):
                for item in s["details"]:
                    icone = "✅" if item["statut"] == "Présent(e)" else "❌"
                    st.write(f"{icone} **{item['nom']}** : {item['statut']}")
    else:
        st.write("Aucune séance archivée pour le moment.")
