import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Espace Candidat | Le Barreau - PMF",
    page_icon="⚖️",
    layout="centered"
)

# Code HTML/CSS complet injecté via st.markdown
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Espace Candidat | Le Barreau - PMF</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #120F0D;
            --card-bg: #1A1613;
            --card-border: #2C2420;
            --accent-gold: #D4AF37;
            --accent-champagne: #E6D5C3;
            --text-main: #F5F2EF;
            --text-muted: #A89F96;
            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow-x: hidden;
        }

        h1, h2, h3, .font-serif {
            font-family: 'Playfair Display', serif;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            width: 100%;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 2.5rem;
            color: var(--accent-champagne);
            margin-bottom: 10px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        header p {
            color: var(--text-muted);
            font-size: 0.95rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            transition: var(--transition);
        }

        .input-group {
            margin-bottom: 25px;
            text-align: left;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: var(--accent-champagne);
            font-size: 0.9rem;
            letter-spacing: 0.5px;
        }
        input[type="text"] {
            width: 100%;
            padding: 14px 18px;
            background: #120F0D;
            border: 1px solid var(--card-border);
            border-radius: 8px;
            color: var(--text-main);
            font-size: 1rem;
            font-family: 'Plus Jakarta Sans', sans-serif;
            transition: var(--transition);
        }
        input[type="text"]:focus {
            outline: none;
            border-color: var(--accent-gold);
        }

        .btn {
            display: inline-block;
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #D4AF37 0%, #AA8225 100%);
            color: #120F0D;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: var(--transition);
            text-align: center;
            text-decoration: none;
            letter-spacing: 0.5px;
        }
        .btn:hover {
            opacity: 0.95;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3);
        }

        .error-msg {
            color: #E06D6D;
            font-size: 0.85rem;
            margin-top: 15px;
            display: none;
        }

        #dashboard-section {
            display: none;
        }

        .welcome-header {
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 20px;
            margin-bottom: 25px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 15px;
        }
        .welcome-header h2 {
            font-size: 1.8rem;
            color: var(--accent-champagne);
        }
        .badge {
            background: rgba(212, 175, 55, 0.1);
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .info-card {
            background: #120F0D;
            border: 1px solid var(--card-border);
            padding: 20px;
            border-radius: 8px;
        }
        .info-card h4 {
            color: var(--text-muted);
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
            font-weight: 500;
        }
        .info-card p {
            color: var(--text-main);
            font-size: 1rem;
            font-weight: 500;
        }

        .document-box {
            background: #120F0D;
            border: 1px solid var(--card-border);
            padding: 25px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            flex-wrap: wrap;
            gap: 15px;
        }
        .document-info h4 {
            color: var(--accent-champagne);
            font-size: 1.1rem;
            margin-bottom: 5px;
        }
        .document-info p {
            color: var(--text-muted);
            font-size: 0.85rem;
        }

        .btn-secondary {
            background: transparent;
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold);
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
            cursor: pointer;
            transition: var(--transition);
            text-decoration: none;
            font-size: 0.9rem;
        }
        .btn-secondary:hover {
            background: rgba(212, 175, 55, 0.1);
        }

        .actions-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
            border-top: 1px solid var(--card-border);
            padding-top: 20px;
        }
        .contact-link {
            color: var(--accent-champagne);
            text-decoration: none;
            font-size: 0.9rem;
            transition: var(--transition);
        }
        .contact-link:hover {
            color: var(--accent-gold);
            text-decoration: underline;
        }
        .btn-text {
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 0.9rem;
            font-family: 'Plus Jakarta Sans', sans-serif;
            transition: var(--transition);
        }
        .btn-text:hover {
            color: var(--text-main);
        }

        footer.main-footer {
            text-align: center;
            padding: 20px;
            color: var(--text-muted);
            font-size: 0.8rem;
            border-top: 1px solid var(--card-border);
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>Le Barreau</h1>
            <p>Lycée Pierre Mendès France — Sessions de Recrutement 2026</p>
        </header>

        <div class="card">
            <!-- SECTION CONNEXION -->
            <div id="login-section">
                <h2 style="color: var(--accent-champagne); margin-bottom: 10px; font-size: 1.8rem;">Espace Candidat</h2>
                <p style="color: var(--text-muted); margin-bottom: 30px; font-size: 0.95rem;">Entrez vos prénom et nom exacts pour accéder aux détails de votre session.</p>
                
                <form id="login-form" onsubmit="handleLogin(event)">
                    <div class="input-group">
                        <label for="fullName">Prénom et Nom</label>
                        <input type="text" id="fullName" placeholder="Ex: Mehdi Besbes" required autocomplete="off">
                    </div>
                    <button type="submit" class="btn">Accéder à mon espace</button>
                    <p id="error-message" class="error-msg">Nom introuvable. Veuillez vérifier l'orthographe ou contacter le bureau.</p>
                </form>
            </div>

            <!-- SECTION TABLEAU DE BORD -->
            <div id="dashboard-section">
                <div class="welcome-header">
                    <div>
                        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px;">Bienvenue,</p>
                        <h2 id="candidate-name-display">Nom du Candidat</h2>
                    </div>
                    <div class="badge" id="session-badge">Session 1</div>
                </div>

                <div class="info-grid">
                    <div class="info-card">
                        <h4>Sujet de Session</h4>
                        <p id="info-topic">-</p>
                    </div>
                    <div class="info-card">
                        <h4>Date & Horaire</h4>
                        <p id="info-date">-</p>
                    </div>
                    <div class="info-card">
                        <h4>Lieu exact</h4>
                        <p id="info-location">-</p>
                    </div>
                    <div class="info-card">
                        <h4>Juges / Évaluateurs</h4>
                        <p id="info-judges">-</p>
                    </div>
                </div>

                <div class="document-box">
                    <div class="document-info">
                        <h4 id="doc-title">Background Guide officiel</h4>
                        <p>Consultez ou téléchargez le support de préparation complet pour votre session.</p>
                    </div>
                    <a href="#" id="doc-link" class="btn-secondary" target="_blank">Consulter le PDF</a>
                </div>

                <div class="actions-footer">
                    <a href="mailto:lebarreau@ert.tn" class="contact-link">✉ Contacter le bureau : lebarreau@ert.tn</a>
                    <button class="btn-text" onclick="handleLogout()">← Se déconnecter</button>
                </div>
            </div>
        </div>
    </div>

    <footer class="main-footer">
        © 2026 Le Barreau — Lycée Pierre Mendès France, Tunis. Tous droits réservés.
    </footer>

    <script>
        const database = [
            { name: "Mehdi Besbes", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Yasmine Ben Ali", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Yessine Bouchoucha", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Lydia Meddeb", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Kenza Smat", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Yasmine Oudi", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Rahma Snoussi", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Selim Darghouth", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Farah El Asmi", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Nermine Maya Adhoum", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Zyne Zampol", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Yassine Albouchi", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Ines Ben Naceur", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Farah Alaya", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Sohane Wawrzynowski", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Sarra Chaouch", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },
            { name: "Baya Hadj Ali", session: "Session 1", topic: "Est-ce que le droit international est encore légitime de nos jours ?", date: "Mercredi 9 septembre de 15h à 16h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Kaïs Zarrad et Adam Chtourou", docName: "Background Guide - Droit International", docUrl: "#" },

            { name: "Mehdi Zenkri", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Tasnim Louati", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Farah Borgi", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Bechir El Ouadhane", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Maher Ben Ouirane", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Nour Mahjoub", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Yasmine Kasraoui", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Salima Mourani", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Ramy Bouhamed", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Amine Ouerghi", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Yasmine Bousrour", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Lyne Naouali", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Sara Sancho", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Myriam Abbes", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Lina Hermassi", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Hosni Rahmatoallah", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Yasmine Mahjoub", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Sarra Khedher", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" },
            { name: "Behia", session: "Session 2", topic: "Faut-il limiter la liberté d'expression en France ?", date: "Mercredi 9 septembre de 16h à 17h", location: "Salle F109 (Entrées Rue Bel Air)", judges: "Sarra Ben Mahmoud et Mayara Hamaoui", docName: "Background Guide - Liberté d'Expression", docUrl: "#" }
        ];

        function normalizeString(str) {
            return str.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase().trim();
        }

        function handleLogin(event) {
            event.preventDefault();
            const inputVal = document.getElementById('fullName').value;
            const normalizedInput = normalizeString(inputVal);
            const errorMsg = document.getElementById('error-message');

            const candidate = database.find(c => normalizeString(c.name) === normalizedInput);

            if (candidate) {
                errorMsg.style.display = 'none';
                document.getElementById('candidate-name-display').innerText = candidate.name;
                document.getElementById('session-badge').innerText = candidate.session;
                document.getElementById('info-topic').innerText = candidate.topic;
                document.getElementById('info-date').innerText = candidate.date;
                document.getElementById('info-location').innerText = candidate.location;
                document.getElementById('info-judges').innerText = candidate.judges;
                document.getElementById('doc-title').innerText = candidate.docName;
                document.getElementById('doc-link').href = candidate.docUrl;

                document.getElementById('login-section').style.display = 'none';
                document.getElementById('dashboard-section').style.display = 'block';

                localStorage.setItem('barreau_candidate', candidate.name);
            } else {
                errorMsg.style.display = 'block';
            }
        }

        function handleLogout() {
            localStorage.removeItem('barreau_candidate');
            document.getElementById('dashboard-section').style.display = 'none';
            document.getElementById('login-section').style.display = 'block';
            document.getElementById('fullName').value = '';
        }

        window.onload = function() {
            const savedName = localStorage.getItem('barreau_candidate');
            if (savedName) {
                document.getElementById('fullName').value = savedName;
                const fakeEvent = { preventDefault: () => {} };
                handleLogin(fakeEvent);
            }
        };
    </script>
</body>
</html>
"""

# Affichage du code HTML dans Streamlit
st.markdown(html_code, unsafe_allow_html=True)
