import streamlit as st
def toggle_theme():
    """
    Bascule entre le mode jour et nuit dans une application Streamlit.
    Gère les styles CSS pour une expérience utilisateur cohérente.
    Mode sombre activé par défaut.
    """
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    
    # Configuration des thèmes
    THEMES = {
        "dark": {
            "bg_color": "#0e1117",
            "text_color": "white",
            "sidebar_bg": "#1a1d23",
            "input_bg": "#25282e",
            "border_color": "white"
        },
        "light": {
            "bg_color": "white",
            "text_color": "black",
            "sidebar_bg": "#f0f0f0",
            "input_bg": "white",
            "border_color": "black"
        }
    }
    
    # Modifier le bouton pour inclure le texte "Thème"
    if st.button(f"Thème {'🌙' if st.session_state.dark_mode else '☀️'}", 
                key="unique_theme_toggle_btn",
                help="Changer le thème"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()
    
    # Sélection du thème actif
    current_theme = THEMES["dark"] if st.session_state.dark_mode else THEMES["light"]
    
    # Création du CSS dynamique
    css = f"""
    <style>
    /* Styles globaux */
    body, .stApp {{
        background-color: {current_theme["bg_color"]};
        color: {current_theme["text_color"]};
    }}
    
    /* Styles de la barre latérale */
    .stSidebar, .stSidebarContent {{
        background-color: {current_theme["sidebar_bg"]} !important;
        color: {current_theme["text_color"]} !important;
        padding-top: 0 !important;  /* Réduit l'espace en haut */
    }}
    
    /* Style spécifique pour le menu de navigation */
    div[data-testid="stSidebarNav"] {{
        background-color: {current_theme["bg_color"]} !important;
    }}
    
    div[data-testid="stSidebarNav"] > ul {{
        background-color: {current_theme["bg_color"]} !important;
    }}

    div[data-testid="stSidebarNav"] section {{
        background-color: {current_theme["bg_color"]} !important;
    }}
    
    /* Masquer les éléments vides */
    .element-container:has(.stRadio) > div:empty {{
        display: none !important;
    }}
    
    /* Style du conteneur radio principal */
    .stRadio {{
        background: none !important;
        margin-top: -1rem !important;  /* Remonte légèrement tout le menu */
    }}
    
    /* Styles pour le groupe de boutons radio */
    .stRadio > div[role="radiogroup"] {{
        display: flex !important;
        flex-direction: column !important;
        gap: 4px !important;  /* Réduit l'espace entre les boutons */
        padding: 0 !important;
        background: none !important;
        margin-bottom: 1rem !important;  /* Ajoute un espace après le dernier bouton */
    }}
    
    /* Style des boutons individuels */
    .stRadio > div[role="radiogroup"] > label {{
        background-color: {current_theme["sidebar_bg"]} !important;
        color: {current_theme["text_color"]} !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 4px !important;
        margin: 0 !important;
        padding: 12px !important;
        transition: all 0.2s ease !important;
        height: 45px !important;
        display: flex !important;
        align-items: center !important;
        width: 100% !important;
        box-sizing: border-box !important;
        cursor: pointer !important;
    }}
    
    /* Style au survol */
    .stRadio > div[role="radiogroup"] > label:hover {{
        border-color: rgba(96, 165, 250, 0.4) !important;
        transform: translateX(4px);
        background-color: rgba(255, 255, 255, 0.05) !important;
    }}

    /* Style pour l'option sélectionnée */
    .stRadio > div[role="radiogroup"] > label[data-checked="true"] {{
        border-color: #60a5fa !important;
        background-color: rgba(96, 165, 250, 0.1) !important;
    }}
    
    /* Styles des conteneurs principaux */
    .st-emotion-cache-h4xjwg,
    .st-emotion-cache-15ecox0 {{
        background-color: {current_theme["bg_color"]} !important;
        color: {current_theme["text_color"]} !important;
    }}
    
    /* Supprimer le label superflu */
    .st-emotion-cache-1qg05tj,
    .st-emotion-cache-1dx5vew0 {{
        display: none !important;
    }}

    /* Styles de texte */
    h1, h2, h3, h4, h5, h6, p, span, div {{
        color: {current_theme["text_color"]} !important;
    }}
    
    /* Styles des éléments d'interface */
    .stTextInput,
    .stButton>button,
    .stSelectbox,
    .stRadio {{
        background-color: {current_theme["input_bg"]} !important;
        color: {current_theme["text_color"]} !important;
        border-color: {current_theme["border_color"]} !important;
    }}
    
    /* Styles des widgets DataFrames et tables */
    .dataframe {{
        color: {current_theme["text_color"]} !important;
    }}
    
    /* Styles des liens */
    a {{
        color: {current_theme["text_color"]} !important;
        text-decoration: underline;
    }}

    /* Supprimer l'espace vide en haut */
    .block-container {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}

    /* Supprimer tous les espacements superflus */
    .element-container {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    
    /* Ajuster l'espacement des séparateurs */
    .stMarkdown {{
        margin-top: 1rem !important;
        margin-bottom: 1rem !important;
    }}

    /* Style du bouton de thème */
    .stButton {{
        margin-top: 0 !important;
        margin-bottom: 1rem !important;
    }}

    .stButton > button {{
        width: 100% !important;
        margin: 0 !important;
        padding: 0.5rem !important;
    }}

    /* Ajustement du conteneur radio */
    .element-container:has(.stRadio) {{
        margin-top: -2rem !important;
    }}

    /* Style spécifique pour le menu de navigation */
    .stRadio > div[role="radiogroup"] {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}

    /* Supprimer les espaces vides */
    .element-container:empty {{
        display: none !important;
    }}

    /* Ajuster l'espacement global de la sidebar */
    section[data-testid="stSidebar"] > div {{
        padding-top: 1rem !important;
    }}

    /* Style amélioré pour le bouton de thème */
    .stButton > button {{
        background-color: {current_theme["sidebar_bg"]} !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: {current_theme["text_color"]} !important;
        width: 100% !important;
        padding: 0.75rem !important;
        margin: 0 0 1rem 0 !important;
        border-radius: 4px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }}

    .stButton > button:hover {{
        border-color: rgba(96, 165, 250, 0.4) !important;
        transform: translateX(4px);
        background-color: rgba(255, 255, 255, 0.05) !important;
    }}

    /* Ajuster la position du bouton */
    .stButton {{
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }}

    /* Style pour le bouton de thème */
    div[data-testid="column"]:has(button:contains("Thème")) button {{
        padding: 0 1rem !important;
        width: 160px !important;  /* Augmenté la largeur */
        height: 40px !important;
        border-radius: 20px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;  /* Aligner le contenu à gauche */
        font-size: 0.9em !important;
        gap: 8px !important;
        white-space: nowrap !important;  /* Empêche le texte de passer à la ligne */
    }}

    /* Style pour le contenu du bouton */
    div[data-testid="column"]:has(button:contains("Thème")) button p {{
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        margin: 0 !important;
    }}

    /* Style pour la colonne contenant le bouton */
    div[data-testid="column"]:has(button:contains("Thème")) {{
        width: 160px !important;  /* Forcer la largeur de la colonne */
        flex: none !important;    /* Empêcher la flexbox de réduire la taille */
    }}

    /* Supprimer les styles qui peuvent interférer */
    .st-emotion-cache-kvoai1,
    .st-emotion-cache-4rq2ow {{
        display: none !important;
    }}

    /* Style pour la colonne contenant le bouton */
    div[data-testid="column"]:has(button:contains("Thème")) {{
        display: flex !important;
        justify-content: flex-end !important;
        width: auto !important;
    }}
    </style>
    """
    
    # Application du CSS
    st.markdown(css, unsafe_allow_html=True)