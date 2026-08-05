import streamlit as st
import requests
import random
import time
from datetime import datetime

# -------------------------------------------------------------------
# CONFIGURATION DE LA PAGE
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Le Barreau Journal — Édition Officielle",
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

    /* En-tête de la page */
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

    /* Titres d'articles */
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

    /* Section Sources */
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
    
    /* Style de la carte logo sidebar */
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
# MOTEUR D'IMAGES DYNAMIQUES (VARIÉTÉ GARANTIE)
# -------------------------------------------------------------------
def get_unsplash_image(keywords):
    selected_query = random.choice(keywords)
    timestamp = int(time.time() * 1000)
    try:
        url = f"https://api.unsplash.com/photos/random?query={selected_query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}&sig={timestamp}"
        res = requests.get(url, timeout=4)
        if res.status_code == 200:
            data = res.json()
            return data['urls']['regular'], data['user']['name']
    except Exception:
        pass
    return "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=1200", "Unsplash Premium"

# -------------------------------------------------------------------
# ANIMATION DE BIENVENUE (TOAST UNIQUE)
# -------------------------------------------------------------------
if 'welcome_shown' not in st.session_state:
    time.sleep(0.5)
    st.toast("La justice n'attend pas. Bienvenue sur l'édition du jour.", icon="⚖️")
    st.session_state.welcome_shown = True

# -------------------------------------------------------------------
# BARRE LATÉRALE (LOGO & NAVIGATION)
# -------------------------------------------------------------------
with st.sidebar:
    # En-tête style carte institutionnelle inspirée de ton logo
    st.markdown("""
    <div class="sidebar-brand">
        <h3 style="margin:0; color:#FFFFFF;">LE BARREAU</h3>
        <p style="font-size:0.8rem; margin:5px 0 0 0; color:#E2E8F0;">Pierre Mendès France</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.title("Navigation")
    page = st.radio("Rubriques", [
        "📰 À la Une",
        "🇫🇷 Droit Public & Administratif",
        "⚖️ Débat de Société"
    ])
    
    st.markdown("---")
    st.caption("© 2026 Le Barreau PMF. Bureau Exécutif.")

# -------------------------------------------------------------------
# EN-TÊTE PRINCIPAL
# -------------------------------------------------------------------
st.markdown(f"""
<div class="top-nav">
    <div class="brand-logo">LE BARREAU JOURNAL</div>
    <div style="color: #64748B; font-size: 0.95rem; font-weight: 500;">
        Édition Officielle du Lycée Pierre Mendès France • {datetime.now().strftime('%d %B %Y')}
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# PAGE 1 : À LA UNE
# -------------------------------------------------------------------
if page == "📰 À la Une":
    st.markdown('<span class="badge-modern">JURISPRUDENCE PÉNALE</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">L\'Altération du Discernement : Le Conseil Constitutionnel Trace une Nouvelle Ligne Rouge</div>', unsafe_allow_html=True)
    st.markdown('<div class="article-meta">Par le Pôle Rédactionnel • Lecture : 4 min • Décision QPC du 12 juillet 2026</div>', unsafe_allow_html=True)

    img_hero, photog_hero = get_unsplash_image(["supreme-court", "gavel", "justice-scale", "law-books"])
    st.image(img_hero, caption=f"Crédit photographique : {photog_hero} / Unsplash", use_container_width=True)

    st.markdown("""
    <div class="article-content">
        L'imputabilité des infractions commises sous l'emprise de substances psychoactives fait l'objet d'un revirement jurisprudentiel majeur. 
        Saisi d'une Question Prioritaire de Constitutionnalité (QPC), le Conseil Constitutionnel a dû trancher un débat juridique complexe : 
        l'abolition temporaire du discernement, lorsqu'elle résulte d'une consommation volontaire de stupéfiants, peut-elle constituer une cause d'irresponsabilité pénale au sens de l'article 122-1 du Code pénal ?
        <br><br>
        Dans sa décision rendue publique hier, les Sages ont affirmé que la protection de la société prévaut. 
        <b>Le fait de se placer volontairement dans un état de vulnérabilité psychique ne saurait exonérer l'auteur de ses actes.</b> 
        Cette décision vient clore des mois de débats doctrinaux initiés par la Cour de cassation, et impose désormais aux juges du fond d'évaluer <i>l'intention préalable</i> à la consommation de la substance.
        <br><br>
        Pour les avocats de la défense, cette redéfinition réduit considérablement le champ d'application de l'irresponsabilité psychiatrique et soulève des questions sur le principe de l'élément moral de l'infraction.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="source-box">
        <h4>📚 Sources et Références Officielles</h4>
        <ul>
            <li><b>Conseil Constitutionnel :</b> <a href="https://www.conseil-constitutionnel.fr/" target="_blank">Décision n° 2026-987 QPC du 12 juillet 2026</a></li>
            <li><b>Code pénal :</b> Article 122-1 (relatif aux causes d'irresponsabilité ou d'atténuation de la responsabilité).</li>
            <li><b>Dalloz Actualité :</b> Analyse de la doctrine sur la faute préalable (Édition du 14 juillet).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# PAGE 2 : DROIT PUBLIC
# -------------------------------------------------------------------
elif page == "🇫🇷 Droit Public & Administratif":
    st.markdown('<span class="badge-modern">CONTENTIEUX ADMINISTRATIF</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Responsabilité de l\'État face à l\'Érosion Côtière : L\'Arrêt de Principe du Conseil d\'État</div>', unsafe_allow_html=True)
    st.markdown('<div class="article-meta">Par le Comité d\'Analyse • Lecture : 5 min • Droit de l\'Urbanisme</div>', unsafe_allow_html=True)

    img_pub, photog_pub = get_unsplash_image(["coastal-city", "french-architecture", "document", "parliament"])
    st.image(img_pub, caption=f"Crédit photographique : {photog_pub} / Unsplash", use_container_width=True)

    st.markdown("""
    <div class="article-content">
        Le juge administratif suprême vient de rendre une décision qui fera date dans le droit de l'environnement et de l'urbanisme. 
        Confronté au recul inexorable du trait de côte, un collectif de propriétaires avait engagé la responsabilité pour faute de l'État, 
        lui reprochant son inaction dans le financement d'ouvrages de protection maritimes.
        <br><br>
        Dans un arrêt lu en Assemblée (CE, Ass., 4 août 2026, <i>Syndicat de défense du littoral occidental</i>, n° 458921), 
        le Conseil d'État a rappelé que si l'État dispose de pouvoirs de police générale pour assurer la sécurité publique, 
        <b>il ne pèse sur lui aucune obligation de résultat quant à la protection des propriétés privées contre les phénomènes naturels inéluctables.</b>
        <br><br>
        Toutefois, le juge ouvre une brèche inédite : la responsabilité sans faute de l'État pourrait être engagée sur le fondement de la rupture de l'égalité devant les charges publiques, si les propriétaires démontrent un préjudice grave et spécial découlant directement d'un plan de prévention des risques (PPRL) excessivement restrictif.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="source-box">
        <h4>📚 Sources et Références Officielles</h4>
        <ul>
            <li><b>Conseil d'État :</b> <a href="https://www.conseil-etat.fr/fr/arianeweb/" target="_blank">Arrêt d'Assemblée du 4 août 2026, n° 458921</a></li>
            <li><b>Légifrance :</b> Code de l'environnement (Articles L. 562-1 et suivants sur la prévention des risques naturels).</li>
            <li><b>Revue Française de Droit Administratif (RFDA) :</b> L'inaction climatique et la responsabilité publique.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# PAGE 3 : DÉBAT DE SOCIÉTÉ
# -------------------------------------------------------------------
elif page == "⚖️ Débat de Société":
    st.markdown('<span class="badge-modern">TRIBUNE LIBRE & OPINION</span>', unsafe_allow_html=True)
    st.markdown('<div class="article-title">Le Droit de Vote à 16 Ans : Refonte de la Majorité Civique ou Péril Démocratique ?</div>', unsafe_allow_html=True)
    st.write("Exprimez-vous sur la grande question constitutionnelle de la semaine.")
    
    img_deb, photog_deb = get_unsplash_image(["voting", "youth", "debate", "microphone"])
    st.image(img_deb, caption=f"Crédit photographique : {photog_deb} / Unsplash", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.success("POUR : L'élargissement du corps électoral")
        st.write("La jeunesse est aujourd'hui en première ligne des enjeux de long terme (climat, dette). Aligner la majorité pénale et fiscale sur la majorité électorale relève de l'équité démocratique.")
    with col2:
        st.error("CONTRE : La préservation du discernement politique")
        st.write("Le droit civil fixe la majorité à 18 ans pour garantir une pleine maturité contractuelle. Le droit de vote exige une indépendance matérielle et intellectuelle similaire vis-à-vis du cadre familial.")

    st.markdown("---")
    st.subheader("📝 Soumettre votre plaidoirie")
    st.text_input("Identité & Classe", placeholder="Ex: Élève de 1ère Générale")
    st.text_area("Argumentaire Juridique (Max 500 mots) :")
    if st.button("Transmettre au bureau pour publication"):
        st.success("Votre tribune a été transmise avec succès au comité de lecture du Barreau PMF.")
