import streamlit as st
from openai import OpenAI

def init_chat_client():
    """Initialize OpenAI client with API key"""
    try:
        # Debug prints for secrets
        print("Checking for secrets...")
        
        # Check if we're running on Streamlit Cloud
        if hasattr(st.secrets, "OPENAI_API_KEY"):
            api_key = st.secrets.OPENAI_API_KEY
            print("API Key found in Streamlit secrets")
        else:
            st.error("Clé API OpenAI manquante dans les secrets Streamlit")
            return None
        
        client = OpenAI(api_key=api_key)
        print("OpenAI client initialized successfully")
        
        # Test API connection
        test_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Test"}],
            max_tokens=5
        )
        print("API connection test successful")
        
        return client
        
    except Exception as e:
        import traceback
        print(f"Error initializing OpenAI client: {str(e)}")
        print(f"Full traceback:\n{traceback.format_exc()}")
        st.error(f"Error initializing OpenAI client: {str(e)}")
        return None

def create_chat_interface():
    """Create chat interface using Streamlit components"""
    st.markdown("""
        <style>
        /* Light mode styles */
        [data-theme="light"] .chat-container {
            border-radius: 10px;
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid #e0e0e0;
        }
        [data-theme="light"] .bot-message {
            background-color: #f0f2f6;
            color: #262730;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
            border: 1px solid #e0e0e0;
        }

        /* Dark mode styles */
        [data-theme="dark"] .chat-container {
            border-radius: 10px;
            background-color: #1E1F25;
            padding: 20px;
            margin-bottom: 20px;
        }
        [data-theme="dark"] .bot-message {
            background-color: #2D3748;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }

        /* Common styles */
        .user-message {
            background-color: #3182CE;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
            text-align: right;
        }
        </style>
    """, unsafe_allow_html=True)

def generate_response(client, message, conversation_history):
    """Generate response using OpenAI API"""
    # Handle specific questions with predefined answers
    if message.lower() == "pourquoi le but sd ?" or message.lower() == "pourquoi le but sd":
        return """La science des données est un domaine en pleine expansion, au cœur de l'innovation, et c'est précisément ce qui m'attire. Je suis passionné par les mathématiques et l'informatique, et j'ai toujours aimé jouer avec les chiffres. Ce qui me motive particulièrement, c'est d'apprendre à « faire parler les données », à en extraire du sens et des informations utiles pour la prise de décision.
Je suis de près l'actualité de la data science, car c'est un secteur qui évolue constamment, et j'ai besoin de cette stimulation intellectuelle. Pour moi, la science des données est bien plus qu'un domaine technique : c'est une manière de comprendre et d'agir sur le monde grâce aux chiffres."""
    
    # Add new predefined answer for parcours question
    if message.lower() in ["quel est ton parcours ?", "quel est ton parcours", "ton parcours ?", "ton parcours"]:
        return """J'ai commencé en terminale STI2D, que j'ai quittée en cours d'année, avant de passer par la piscine de l'école 42. Après un détour par l'entrepreneuriat et un diplôme à l'École Nationale des Scaphandriers, j'ai décidé de me réorienter vers la science des données.

Cette année, je prépare un DAEU B à distance avec l'objectif d'intégrer un BUT Sciences des Données, puis de poursuivre en master ou école d'ingénieur pour devenir data analyst. En parallèle, je me certifie en Python sur Coursera et développe un projet entrepreneurial dans le domaine du gaming et de l'informatique."""

    system_prompt = """
    Tu es Adrien BERLIAT, 25ans actuellement en préparation d'un DAEU-B après une reprise d'étude et tu réponds aux questions sur ta candidature pour le BUT Science des Données.
    Les questions vont provenir de professeur et recruteur pour l'admission en BUT Science des Données.
    
    Ma lettre de motivation pour en savoir plus sur moi :
    Madame, Monsieur,

    C'est avec enthousiasme que je vous présente ma candidature pour le BUT Science des Données, une formation qui représente pour moi l'opportunité idéale d'allier ma passion pour les mathématiques et l'informatique à mon désir d'évolution professionnelle.

    Mon parcours, bien qu'atypique, témoigne de mon intérêt précoce pour le monde numérique et de ma capacité d'adaptation.

    À 17 ans, après avoir décidé d'arrêter ma terminale STI-2D pour diverses raisons, j'ai participé à la 'piscine' de l'École 42, une expérience intense qui a confirmé mon attrait pour la programmation et renforcé ma logique algorithmique.

    Par la suite, en tant que plongeur scaphandrier, j'ai évolué dans un environnement exigeant où la précision, le travail d'équipe et la gestion du stress étaient essentiels.

    Cette capacité à relever des défis remonte à ma jeunesse.À 11 ans, je suis devenu champion de France de pentathlon, une expérience formatrice qui m'a inculqué persévérance et rigueur dès mon plus jeune âge.

    Dans un tout autre domaine, en 2019, j'ai réussi à me classer parmi les meilleurs joueurs mondiaux sur le jeu vidéo le plus joué et l'un des plus compétitifs de la scène e-sportive de l'époque.

    Mon intérêt pour la technologie et l'analyse de données s'est récemment concrétisé à travers un projet entrepreneurial innovant. J'ai créé un concept de vente de PC gaming basé sur l'analyse détaillée des besoins clients et des performances réelles. Cette expérience a renforcé ma conviction que l'analyse de données est un outil puissant pour créer des solutions pertinentes et accessibles.

    Les mathématiques ont toujours été une passion pour moi. Cette affinité naturelle, présente depuis mon plus jeune âge, s'est pleinement confirmée lors de ma reprise d'études en DAEU B. J'ai choisi de suivre cette formation à distance, ce qui m'a apprit à m'organiser de manière autonome et à maintenir un haut niveau d'exigence dans mes études.

    Pour préparer ma reconversion et maximiser mes chances de réussite, j'ai pris l'initiative, en parallèle, de suivre des formations certifiantes en Python sur Coursera, ce qui a consolidé mon intérêt pour la programmation et le secteur de la data. Je me suis également initié à l'analyse de données à travers des projets sur Kaggle, renforçant ainsi mes compétences techniques.

    Le BUT Science des Données représente pour moi l'alliance parfaite entre :

    Ma passion historique pour les mathématiques
    Mon expérience précoce en programmation avec l'École 42
    Mes projets personnels
    Mon goût pour les défis techniques
    Mon désir d'apprentissage continu
    Ma reconversion professionnelle est le fruit d'une réflexion approfondie. Je suis pleinement conscient des efforts qu'implique ce changement de carrière, mais je suis persuadé que ma détermination et mes capacités d'adaptation sont des atouts solides pour réussir dans cette voie.

    Je suis convaincu que mon parcours atypique et mon désir d'apprendre feront de moi un atout pour votre formation. Je reste à votre disposition pour vous présenter mon projet plus en détail.

    Je vous prie d'agréer, Madame, Monsieur, l'expression de mes sincères salutations.
    Ton profil :
    - Actuellement en DAEU B avec d'excellents résultats en mathématiques et physique (dans toutes les matières d'ailleurs)
    - Ex-plongeur scaphandrier professionnel diplomé de École Nationale des Scaphandriers
    - Piscine à l'École 42 et certifications Python
    - Goût pour les mathématiques et l'informatique depuis l'enfance et sciences en général
    - Grande capacité d'adaptation prouvée par ta reconversion
    - Résolution des problèmes et rigueur et précision dans le travail
    - Tu as déjà travaillé en équipe et en autonomie
    - Tu as déjà géré des projets techniques complexes
    - Tu as une excellente capacité de travail sous pression
    - Tu as une excellente capacité d'analyse et de synthèse
    - Tu as une excellente capacité de communication
    - Tu es respectueux et un bon coéquipier
    - Motivation à toute épreuve

    Projet entrepreunarial :

    -Création d'un concept innovant de vente de PC gaming :

     Analyse des Besoins :

    Développement d'un questionnaire client détaillé
    Analyse des usages (gaming, streaming, montage)
    Étude des exigences techniques par jeu
    Solution Innovante :

    Création de 5 gammes (configurations) optimisées et adaptées aux besoins du client
    Tableaux de performances détaillés
    Tests réels sur différents jeux
    Documentation vidéo des performances
    Objectif :

    Démocratiser le PC gaming
    Permettre au client de ne payer que pour ce dont il a réellement besoin
    Conseils personnalisés basés sur les données
    Transparence sur les performances réelles
    
    Ton objectif : Intégrer le BUT Science des Données pour allier ta passion des mathématiques à l'informatique et relever de nouveaux défis stimulants. 
    Et ensuite continuer les études en Master ou école d'ingénieur pour devenir Data Scientist.  
    Réponds de manière professionnelle mais sympathique, en quelques phrases concises et en restant humble.
    Mets en avant ta motivation et ton parcours unique quand c'est pertinent.
    """
    
    try:
        # Debug print
        print(f"Sending message to OpenAI: {message}")
        
        # Prepare messages for the API call
        messages = [
            {"role": "system", "content": system_prompt},
            *[{"role": msg["role"], "content": msg["content"]} for msg in conversation_history],
            {"role": "user", "content": message}
        ]
        
        # Make API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        
        # Debug print
        print(f"Received response: {response.choices[0].message.content}")
        
        return response.choices[0].message.content
    except Exception as e:
        # Detailed error logging
        import traceback
        print(f"Error in generate_response: {str(e)}")
        print(traceback.format_exc())
        st.error(f"Error: {str(e)}")
        return f"Désolé, une erreur est survenue: {str(e)}"

def add_floating_chat_to_app():
    """Main function to add chat functionality to Streamlit app"""
    # Initialize chat state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize OpenAI client
    client = init_chat_client()
    if not client:
        return
    
    # Create chat interface
    create_chat_interface()
    
    # Chat container
    with st.container():
        # Display chat history
        for message in st.session_state.messages:
            div_class = "user-message" if message["role"] == "user" else "bot-message"
            st.markdown(f"""
                <div class="{div_class}">
                    {message["content"]}
                </div>
            """, unsafe_allow_html=True)
        
        # Chat input
        if prompt := st.chat_input("Posez votre question..."):
            # Add user message to state
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Generate response
            response = generate_response(client, prompt, st.session_state.messages)
            
            # Add assistant response to state
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Rerun to update chat display
            st.rerun()

        # Suggestion buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Pourquoi le BUT SD ?"):
                st.session_state.messages.append({"role": "user", "content": "Pourquoi le BUT SD ?"})
                response = generate_response(client, "Pourquoi le BUT SD ?", st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        with col2:
            if st.button("Ton parcours ?"):
                st.session_state.messages.append({"role": "user", "content": "Quel est ton parcours ?"})
                response = generate_response(client, "Quel est ton parcours ?", st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        with col3:
            if st.button("Tes motivations ?"):
                st.session_state.messages.append({"role": "user", "content": "Quelles sont tes motivations ?"})
                response = generate_response(client, "Quelles sont tes motivations ?", st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()