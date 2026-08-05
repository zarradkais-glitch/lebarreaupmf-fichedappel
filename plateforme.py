import streamlit as st

# ==============================================================================
# CONFIGURATION ET DESIGN NAVY & GOLD
# ==============================================================================
st.set_page_config(
    page_title="Le Barreau PMF — Bibliothèque Juridique",
    page_icon="⚖️",
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    h1, h2, h3 { color: #0F172A !important; font-family: 'Georgia', serif; }
    .stButton>button {
        background-color: #0F172A; color: #D4AF37;
        border: 1px solid #D4AF37; border-radius: 5px; font-weight: bold;
    }
    .stButton>button:hover { background-color: #D4AF37; color: #0F172A; }
    .card-gold {
        padding: 20px; border-radius: 8px; background-color: #FFFFFF;
        border-left: 5px solid #D4AF37; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# BARRE LATÉRALE AVEC MON LOGO DU BARREAU PMF
# ==============================================================================
with st.sidebar:
    # Affiche le logo du club téléversé
    try:
        st.image("logo_barreau.png", use_column_width=True)
    except:
        st.title("⚖️ Le Barreau PMF")
        
    st.divider()
    
    categorie = st.radio(
        "Navigation :",
        [
            "🏛️ Accueil & Philosophie",
            "⚖️ Les Fondamentaux du Droit",
            "📚 Bibliothèque des Grandes Affaires",
            "🎤 Figure d'Éloquence & Plaidoirie",
            "🧪 Le Laboratoire d'Argumentation"
        ]
    )

# ==============================================================================
# 1. ACCUEIL
# ==============================================================================
if categorie == "🏛️ Accueil & Philosophie":
    st.title("🏛️ Le Barreau PMF — Plateforme Juridique Interactive")
    
    st.markdown("""
    <div class="card-gold">
        <h3>Bienvenue dans le Portail d'Excellence du Barreau PMF</h3>
        <p>Cette plateforme est une académie d'apprentissage du raisonnement, de la rigueur et de l'éloquence. 
        Elle est conçue pour développer l'esprit critique de chaque membre et préparer aux joutes verbales et procès fictifs.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 2. LES FONDAMENTAUX DU DROIT (AVEC PYRAMIDE DE KELSEN & ASSEMBLÉE)
# ==============================================================================
elif categorie == "⚖️ Les Fondamentaux du Droit":
    st.title("⚖️ Les Fondamentaux du Droit")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("La Hiérarchie des Normes")
        st.write("Élaborée par Hans Kelsen, cette théorie classe les normes juridiques sous forme de pyramide : chaque norme doit respecter la norme qui lui est supérieure.")
        try:
            st.image("pyramide_kelsen.jpg", caption="La Pyramide de Kelsen et les blocs du droit", use_column_width=True)
        except:
            st.info("🖼️ Image `pyramide_kelsen.jpg` à ajouter sur GitHub")

    with col2:
        st.subheader("Le Pouvoir Législatif & Les Institutions")
        st.write("Les lois sont votées par le Parlement. L'Assemblée nationale joue un rôle central dans la confection de la loi et le contrôle du gouvernement.")
        try:
            st.image("assemblee_nationale.jpg", caption="L'Assemblée Nationale (Palais Bourbon)", use_column_width=True)
        except:
            st.info("🖼️ Image `assemblee_nationale.jpg` à ajouter sur GitHub")

# ==============================================================================
# 3. BIBLIOTHÈQUE DES GRANDES AFFAIRES (AVEC DREYFUS & NUREMBERG)
# ==============================================================================
elif categorie == "📚 Bibliothèque des Grandes Affaires":
    st.title("📚 La Bibliothèque des Grandes Affaires")
    
    st.subheader("1. L'Affaire Dreyfus (1894 - 1906)")
    col_a1, col_a2 = st.columns([1, 2])
    with col_a1:
        try:
            st.image("affaire_dreyfus.png", caption="Capitaine Alfred Dreyfus", use_column_width=True)
        except:
            st.info("🖼️ Image `affaire_dreyfus.png` manquante")
    with col_a2:
        st.markdown("""
        * **Les Faits :** Le capitaine Alfred Dreyfus est accusé à tort de haute trahison.
        * **L'Enjeu Juridique :** L'importance des droits de la défense, de l'impartialité et des preuves irréfutables face à l'arbitraire.
        * **Impact :** Une erreur judiciaire majeure qui a refaçonné le débat public et l'exigence de justice.
        """)
        
    st.divider()
    
    st.subheader("2. Le Procès de Nuremberg (1945 - 1946)")
    col_b1, col_b2 = st.columns([1, 2])
    with col_b1:
        try:
            st.image("proces_nuremberg.png", caption="Banc des accusés à Nuremberg", use_column_width=True)
        except:
            st.info("🖼️ Image `proces_nuremberg.png` manquante")
    with col_b2:
        st.markdown("""
        * **Les Faits :** Jugement international des dirigeants du 3ème Reich après la Seconde Guerre mondiale.
        * **L'Enjeu Juridique :** Consécration des notions de *Crime contre l'Humanité* et de *Jurisprudence internationale*.
        * **Impact :** Acte fondateur du droit pénal international et de la Justice universelle.
        """)

# ==============================================================================
# 4. FIGURES D'ÉLOQUENCE & PLAIDOIRIE (BADINTER & HALIMI)
# ==============================================================================
elif categorie == "🎤 Figure d'Éloquence & Plaidoirie":
    st.title("🎤 Les Grandes Figures de la Plaidoirie")
    
    col_h1, col_h2 = st.columns(2)
    
    with col_h1:
        st.subheader("Me Gisèle Halimi")
        try:
            st.image("gisele_halimi.png", caption="Gisèle Halimi en robe d'avocate", use_column_width=True)
        except:
            st.info("🖼️ Image `gisele_halimi.png` manquante")
        st.write("**Combats majeurs :** Le procès de Bobigny (1972), la défense des droits des femmes et la transformation du procès en tribune politique et sociale.")

    with col_h2:
        st.subheader("Me Robert Badinter")
        try:
            st.image("robert_badinter.jpg", caption="Robert Badinter", use_column_width=True)
        except:
            st.info("🖼️ Image `robert_badinter.jpg` manquante")
        st.write("**Combats majeurs :** L'abolition de la peine de mort (1981), l'éthique de la justice et la force du discours de conviction devant le Parlement.")

# ==============================================================================
# 5. LE LABORATOIRE D'ARGUMENTATION
# ==============================================================================
elif categorie == "🧪 Le Laboratoire d'Argumentation":
    st.title("🧪 Le Laboratoire de l'Argumentation")
    st.success("Module d'entraînement interactif du Barreau PMF.")
    
    st.subheader("Détecter un Sophisme")
    st.markdown("> *« L'accusé ne peut pas prouver où il était à 20h00, donc il est coupable. »*")
    choix = st.radio("Quel est le vice de ce raisonnement ?", ["Attaque ad hominem", "Inversion de la charge de la preuve", "Faux dilemme"])
    if st.button("Vérifier"):
        if choix == "Inversion de la charge de la preuve":
            st.balloons()
            st.success("Correct ! C'est à l'accusation d'apporter la preuve de la culpabilité.")
