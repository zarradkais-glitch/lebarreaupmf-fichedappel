import streamlit as st
import requests
import random
from datetime import datetime

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau Journal — Grand Quotidien Juridique",
    page_icon="⚖️",
    layout="wide"
)

UNSPLASH_ACCESS_KEY = "FQt3q9yJIf1-4q_v1Kg0fptsuOfsw0qfU-GvbbBb6cE"

# -------------------------------------------------------------------
# DESIGN INSTITUTIONNEL HAUTE RECOMMANDATION (BARREAU & INSTITUTION)
# -------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&family=Inter:wght@300;400;600;700&display=swap');

    .stApp {
        background-color: #0b0e14;
        color: #cbd5e1;
        font-family: 'Inter', sans-serif;
    }

    /* Header Presse Institutionnelle */
    .journal-header {
        border-bottom: 3px double #d4af37;
        padding-bottom: 20px;
        margin-bottom: 30px;
        text-align: center;
        background: radial-gradient(circle, rgba(212,175,55,0.08) 0%, rgba(11,14,20,1) 100%);
    }

    .journal-title {
        font-family: 'Merriweather', serif;
        font-size: 3.2rem;
        font-weight: 700;
        letter-spacing: 2px;
        color: #ffffff;
        text-transform: uppercase;
        margin: 0;
    }

    .journal-subtitle {
        font-size: 0.85rem;
        letter-spacing: 4px;
        color: #d4af37;
        text-transform: uppercase;
        margin-top: 8px;
        font-weight: 600;
    }

    /* Badges de Sources et Rigueur */
    .source-tag {
        background: rgba(212, 175, 55, 0.15);
        color: #f1c40f;
        border: 1px solid #d4af37;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 2px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .meta-info {
        font-size: 0.8rem;
        color: #94a3b8;
        font-style: italic;
        margin-bottom: 15px;
    }

    /* Style des Encadrés de Débat */
    .opinion-box-for {
        background: rgba(16, 185, 129, 0.08);
        border-left: 4px solid #10b981;
        padding: 20px;
        border-radius: 4px;
        margin-bottom: 15px;
    }

    .opinion-box-against {
        background: rgba(239, 68, 68, 0.08);
        border-left: 4px solid #ef4444;
        padding: 20px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# RECUPERATION D'IMAGES HD REELLES
# -------------------------------------------------------------------
def get_unsplash_image(query="law"):
    try:
        url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        res = requests.get(url, timeout=4)
        if res.status_code == 200:
            data = res.json()
            return data['urls']['regular'], data['user']['name']
    except Exception:
        pass
    return "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=1200", "Unsplash Premium"

# -------------------------------------------------------------------
# EN-TÊTE DU JOURNAL
# -------------------------------------------------------------------
st.markdown(f"""
<div class="journal-header">
    <div class="journal-title">LE BARREAU JOURNAL</div>
    <div class="journal-subtitle">Organe d'Analyse Juridique & d'Actualité — Édition du {datetime.now().strftime('%d %B %Y')}</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# NAVIGATION PRINCIPALE (AVEC ONGLET INTERACTIF)
# -------------------------------------------------------------------
st.sidebar.title("🏛️ Sommaire & Rubriques")
page = st.sidebar.radio("Consulter :", [
    "📜 Articles & Analyses Approfondies",
    "🗳️ Le Débat du Jour (Interactif)",
    "📚 Sources & Jurisprudence Officielle"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Statistiques de Rédaction")
st.sidebar.caption("• Flux de Veille : Conseil d'État, Cour de Cassation, JOUE")
st.sidebar.caption("• Comité de Relecture : Le Barreau PMF")

# -------------------------------------------------------------------
# PAGE 1 : ARTICLES RIGOUREUX ET DEVELOPPÉS
# -------------------------------------------------------------------
if page == "📜 Articles & Analyses Approfondies":

    st.markdown('<span class="source-tag">SOURCE : CONSEIL D\'ÉTAT & LÉGIFRANCE</span>', unsafe_allow_html=True)
    st.markdown("# La Régulation des Systèmes d'Intelligence Artificielle en Droit Public : Entre Sécurité et Libertés Individuelles")
    st.markdown('<div class="meta-info">Par le Pôle d\'Analyse Juridique • Publié le 5 Août 2026 • Temps de lecture : 6 min</div>', unsafe_allow_html=True)
    
    img1, photog1 = get_unsplash_image("courtroom-justice")
    st.image(img1, caption=f"Crédit photo : {photog1} / Unsplash", use_container_width=True)

    st.markdown("""
    ### 1. Le Contexte Juridique et Institutionnel
    L'intégration croissante des algorithmes de décision au sein des administrations publiques impose un réexamen approfondi des principes fondamentaux du droit administratif. Conformément aux directeurs fixés par les nouvelles exigences européennes (*AI Act*), la transparence algorithmique n'est plus une simple recommandation éthique, mais une **obligation juridique opposable**.

    ### 2. Analyse en Droit Comparé et Jurisprudence
    La problématique majeure réside dans l'opacité décisionnelle (*l'effet boîte noire*). La jurisprudentielle française, s'appuyant sur l'article L. 311-3-1 du Code des relations entre le public et administration (CRPA), exige que toute décision administrative individuelle prise sur le fondement d'un traitement algorithmique comporte une explication claire des règles appliquées.

    > **Extrait de référence :** *« Tout usager a le droit d'exiger la communication des paramètres généraux et des pondérations ayant conduit au traitement automatisé de son dossier. »*

    ### 3. Portée Pratique et Orientations Futures
    Les cabinets d'avocats ainsi que les juridictions administratives doivent adapter leurs compétences face à l'émergence du contentieux de l'algorithme. Les enjeux de responsabilité civile et pénale de l'État en cas de biais discriminatoire non détecté représentent le nouveau chantier jurisprudentiel des années à venir.
    """)
    st.markdown("---")

# -------------------------------------------------------------------
# PAGE 2 : LE DEBAT DU JOUR (INTERACTIF + VOTES)
# -------------------------------------------------------------------
elif page == "🗳️ Le Débat du Jour (Interactif)":

    st.markdown('<span class="source-tag">LE GRAND DÉBAT DU QUOTIDIEN</span>', unsafe_allow_html=True)
    st.markdown("# Sujet du Jour : Faut-il accorder une personnalité juridique autonome à l'IA ?")
    st.write("Chaque jour, Le Barreau Journal soumet une question de droit prospectif au vote et à la réflexion des élèves et professeurs.")

    # Graphique et Vote Interactif
    st.subheader("📊 Participez au Vote en Direct")
    
    # Session state pour stocker les votes localement dans la session
    if 'vote_oui' not in st.session_state:
        st.session_state.vote_oui = 42
    if 'vote_non' not in st.session_state:
        st.session_state.vote_non = 58

    col_vote1, col_vote2 = st.columns(2)
    with col_vote1:
        if st.button("👍 OUI (Pour la création d'un statut d'Agent Autonome)", use_container_width=True):
            st.session_state.vote_oui += 1
            st.success("Votre vote pour le OUI a été enregistré !")
            
    with col_vote2:
        if st.button("👎 NON (Maintenir la responsabilité exclusive de l'humain)", use_container_width=True):
            st.session_state.vote_non += 1
            st.error("Votre vote pour le NON a été enregistré !")

    # Affichage des Résultats
    total_votes = st.session_state.vote_oui + st.session_state.vote_non
    pourcentage_oui = round((st.session_state.vote_oui / total_votes) * 100, 1)
    pourcentage_non = round((st.session_state.vote_non / total_votes) * 100, 1)

    st.markdown("### Résultats actuels de la communauté :")
    st.progress(pourcentage_oui / 100)
    st.caption(f"Pour : **{pourcentage_oui}%** ({st.session_state.vote_oui} votes) | Contre : **{pourcentage_non}%** ({st.session_state.vote_non} votes) | Total : {total_votes} participants")

    st.markdown("---")

    # Confrontation des Arguments (Thèse / Antithèse)
    st.subheader("⚖️ Confrontation des Doctrines Juridiques")

    col_t1, col_t2 = st.columns(2)

    with col_t1:
        st.markdown("""
        <div class="opinion-box-for">
            <h4 style="color:#10b981; margin-top:0;">THÈSE : Pour un statut de "Personne Robot"</h4>
            <p><b>Argument majeur :</b> Face à l'autonomie d'apprentissage des IA émergentes, imputer la responsabilité aux seuls concepteurs devient techniquement inefficace lors de dommages imprévisibles.</p>
            <ul>
                <li>Création d'un fonds de garantie obligatoire financé par les éditeurs d'IA.</li>
                <li>Imputabilité directe des préjudices patrimoniaux.</li>
                <li>Inspiration du modèle de la responsabilité des personnes morales en droit des sociétés.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_t2:
        st.markdown("""
        <div class="opinion-box-against">
            <h4 style="color:#ef4444; margin-top:0;">ANTITHÈSE : Conserver l'Anthropocentrisme du Droit</h4>
            <p><b>Argument majeur :</b> Le Droit est une construction humaine destinée aux humains. Diluer la responsabilité de l'homme derrière une machine constitue un risque éthique majeur.</p>
            <ul>
                <li>Risque d'impunité pour les géants de la Tech et développeurs.</li>
                <li>L'IA manque d’élément moral (intention ou conscience) indispensable à la punition.</li>
                <li>Le droit actuel (responsabilité des du fait des choses / du fait d'autrui) est suffisant.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Espace de contribution des lecteurs
    st.markdown("---")
    st.subheader("✍️ Proposer une Tribune / Commentaire d'Elève")
    nom_contributeur = st.text_input("Votre Nom et Classe / Fonction :", placeholder="ex: Kaïs Zarrad — Membre du Barreau PMF")
    commentaire = st.text_area("Votre argument juridique ou opinion étayée :")
    
    if st.button("Publier ma contribution au Débat"):
        if nom_contributeur and commentaire:
            st.success("Votre contribution a été envoyée au Comité de Rédaction pour validation !")
        else:
            st.warning("Veuillez remplir tous les champs avant de soumettre.")

# -------------------------------------------------------------------
# PAGE 3 : SOURCES ET RESSORT OFFICIEL
# -------------------------------------------------------------------
elif page == "📚 Sources & Jurisprudence Officielle":
    st.markdown("# 📚 Base de Veille & Liens Institutionnels")
    st.write("Le Barreau Journal appuie l'ensemble de ses analyses sur des sources officielles vérifiables :")

    c_s1, c_s2 = st.columns(2)
    with c_s1:
        st.markdown("""
        * ⚖️ **[Légifrance](https://www.legifrance.gouv.fr/)** — Service public de la diffusion du droit.
        * 🏛️ **[Conseil d'État](https://www.conseil-etat.fr/)** — Jurisprudence administrative et avis constitutionnels.
        * 👨‍⚖️ **[Cour de Cassation](https://www.courdecassation.fr/)** — Arrêts de la chambre criminelle et civile.
        """)
    with c_s2:
        st.markdown("""
        * 🇪🇺 **[EUR-Lex](https://eur-lex.europa.eu/)** — Journal Officiel de l'Union Européenne.
        * 🌐 **[Cour Européenne des Droits de l'Homme](https://www.echr.coe.int/)** — Arrêts CEDH.
        * 📜 **[Journal Officiel](https://www.journal-officiel.gouv.fr/)** — Décrets et Lois publiés.
        """)
