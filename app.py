import streamlit as st
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ==============================================================================
# CONFIGURATION DE LA PAGE STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="Le Barreau - Gestion des Présences",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Le Barreau — Gestion des Présences & Absences")
st.caption("Plateforme administrative officielle pour les responsables et gérants du club.")

# ==============================================================================
# INITIALISATION DE LA BASE DE DONNÉES EN SESSION
# ==============================================================================
if "membres" not in st.session_state:
    st.session_state.membres = [
        {"id": "m1", "nom": "Yassine Ben Ali", "email": "yassine@example.com", "role": "Avocat", "presences": 4, "absences": 1},
        {"id": "m2", "nom": "Sara Mansouri", "email": "sara@example.com", "role": "Procureure", "presences": 2, "absences": 1},
        {"id": "m3", "nom": "Médhi Gharbi", "email": "medhi@example.com", "role": "Juge", "presences": 0, "absences": 3},
        {"id": "m4", "nom": "Lilia Bouazizi", "email": "lilia@example.com", "role": "Avocate", "presences": 5, "absences": 0},
    ]

# ==============================================================================
# FONCTION D'ENVOI D'E-MAIL (SMTP)
# ==============================================================================
def envoyer_email_smtp(destinataire, sujet, corps):
    """Envoie un véritable e-mail via le serveur SMTP de Gmail."""
    # Récupération sécurisée des identifiants (ou depuis st.secrets)
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
# ONGLETS DE NAVIGATION
# ==============================================================================
tab_appel, tab_liste, tab_ajouter = st.tabs(["📋 Prise d'Appel", "📊 Registre & Statuts", "➕ Ajouter un Membre"])

# ------------------------------------------------------------------------------
# ONGLET 1 : PRISE D'APPEL DE LA SÉANCE
# ------------------------------------------------------------------------------
with tab_appel:
    st.subheader(f"Séance du {datetime.date.today().strftime('%d/%m/%Y')}")
    st.info("Cochez ou sélectionnez le statut de chaque membre pour valider la présence.")

    with st.form("form_appel"):
        resultats_appel = {}
        
        for idx, membre in enumerate(st.session_state.membres):
            col1, col2, col3 = st.columns([2, 2, 3])
            with col1:
                st.write(f"**{membre['nom']}**")
                st.caption(f"Rôle : {membre['role']} | Cumul : {membre['absences']} abs.")
            with col2:
                statut = st.radio(
                    "Statut",
                    ["Présent(e)", "Absent(e)"],
                    key=f"radio_{idx}",
                    horizontal=True,
                    label_visibility="collapsed"
                )
                resultats_appel[membre["id"]] = statut
            with col3:
                st.write("") # Espace visuel

            st.divider()

        soumis = st.form_submit_button("💾 Valider et Enregistrer l'Appel", type="primary")

    if soumis:
        alertes_mails = []
        
        for membre in st.session_state.membres:
            statut = resultats_appel.get(membre["id"])
            if statut == "Présent(e)":
                membre["presences"] += 1
                # Félicitations / Avantages assiduité
                if membre["presences"] == 5:
                    sujet = "🏆 [Le Barreau] Félicitations pour votre assiduité !"
                    corps = (
                        f"Bravo {membre['nom']} !\n\n"
                        f"Tu comptabilises désormais 5 présences au Barreau.\n"
                        "Grâce à ton engagement, tu obtiens une priorité sur le choix des rôles principaux pour le prochain procès simulé !\n\n"
                        "Le Bureau du Barreau."
                    )
                    alertes_mails.append((membre, sujet, corps, "Fidélité"))
            else:
                membre["absences"] += 1
                # Alertes absences
                if membre["absences"] == 1:
                    sujet = "[Le Barreau] Absence à la séance d'aujourd'hui"
                    corps = f"Bonjour {membre['nom']},\n\nNous avons constaté ton absence à la séance du jour. Pense à prévenir le bureau en cas d'empêchement !"
                    alertes_mails.append((membre, sujet, corps, "Rappel 1 abs."))
                elif membre["absences"] in [2, 3]:
                    sujet = "⚠️ [AVERTISSEMENT] Cumul d'absences au Barreau"
                    corps = (
                        f"Bonjour {membre['nom']},\n\n"
                        f"Tu cumules actuellement {membre['absences']} absences.\n"
                        "Conformément au règlement du club, ceci constitue un AVERTISSEMENT OFFICIEL.\n"
                        "Rappel : à partir de 4 absences, une exclusion automatique sera prononcée.\n\n"
                        "Le Bureau du Barreau."
                    )
                    alertes_mails.append((membre, sujet, corps, "Avertissement (2 abs.)"))
                elif membre["absences"] >= 4:
                    sujet = "🚨 [NOTIFICATION OFFICIELLE] Exclusion du club Le Barreau"
                    corps = (
                        f"Bonjour {membre['nom']},\n\n"
                        f"Tu as atteint un total de {membre['absences']} absences.\n"
                        "Nous avons le regret de t'informer de ton exclusion des activités du Barreau pour ce semestre.\n\n"
                        "La Présidence du Barreau."
                    )
                    alertes_mails.append((membre, sujet, corps, "Exclusion (4+ abs.)"))

        st.success("✅ Appel enregistré avec succès !")
        
        # Affichage et envoi des e-mails générés
        if alertes_mails:
            st.subheader("📬 E-mails automatiques à envoyer")
            for membre, sujet, corps, type_mail in alertes_mails:
                with st.expander(f"✉️ {type_mail} ➔ {membre['nom']} ({membre['email']})"):
                    st.text_area("Sujet", sujet, height=60, key=f"sujet_{membre['id']}")
                    st.text_area("Corps du message", corps, height=150, key=f"corps_{membre['id']}")
                    
                    if st.button(f"🚀 Envoyer l'email à {membre['nom']}", key=f"btn_{membre['id']}"):
                        succes, msg = envoyer_email_smtp(membre['email'], sujet, corps)
                        if succes:
                            st.success(f"E-mail envoyé à {membre['email']} !")
                        else:
                            st.warning(f"Envoi simulé (Pour un envoi réel, configurez vos identifiants SMTP). Erreur : {msg}")

# ------------------------------------------------------------------------------
# ONGLET 2 : REGISTRE ET STATUTS
# ------------------------------------------------------------------------------
with tab_liste:
    st.subheader("📋 Registre Général des Membres")
    
    # Affichage sous forme de cartes / métriques
    for membre in st.session_state.membres:
        c1, c2, c3, c4 = st.columns([2, 1, 1, 2])
        c1.write(f"**{membre['nom']}** ({membre['role']})")
        c2.metric("Présences", membre['presences'])
        c3.metric("Absences", membre['absences'])
        
        if membre['absences'] >= 4:
            c4.error("🚨 Statut : Exclu(e)")
        elif membre['absences'] >= 2:
            c4.warning("⚠️ Statut : Sous avertissement")
        elif membre['presences'] >= 5:
            c4.success("🌟 Statut : Membre d'Élite")
        else:
            c4.info("✅ Statut : Actif")
            
        st.divider()

# ------------------------------------------------------------------------------
# ONGLET 3 : AJOUTER UN MEMBRE
# ------------------------------------------------------------------------------
with tab_ajouter:
    st.subheader("➕ Inscrire un nouveau membre au Barreau")
    with st.form("form_nouveau"):
        nouveau_nom = st.text_input("Nom et Prénom")
        nouveau_email = st.text_input("Adresse E-mail")
        nouveau_role = st.selectbox("Rôle principal", ["Avocat(e)", "Procureur(e)", "Juge", "Membre"])
        
        valider_ajout = st.form_submit_button("Ajouter le membre")
        
        if valider_ajout:
            if nouveau_nom and nouveau_email:
                nouvel_id = f"m{len(st.session_state.membres) + 1}"
                st.session_state.membres.append({
                    "id": nouvel_id,
                    "nom": nouveau_nom,
                    "email": nouveau_email,
                    "role": nouveau_role,
                    "presences": 0,
                    "absences": 0
                })
                st.success(f"Membre {nouveau_nom} ajouté avec succès !")
                st.rerun()
            else:
                st.error("Veuillez remplir tous les champs.")
