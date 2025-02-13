import streamlit as st
import time
from theme import toggle_theme
from components.quiz import display_quiz  # Correction de l'import
from presentation import display_presentation
from floating_chat import add_floating_chat_to_app
from PIL import Image
import random
from projet_gaming import display_project_concept
from lettre_motivation_content import get_lettre_motivation_content, get_note_importante
from styles.main import get_main_styles
from animations.matrix import get_matrix_styles, display_data_animation

# Remplacer la fonction scroll_to_section par :
def scroll_to_section(title_id):
    js = f'''
    <script>
        function scrollToTitle() {{
            const title = document.getElementById("{title_id}");
            if (title) {{
                title.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }}
        // Exécuter après un court délai pour s'assurer que le DOM est chargé
        setTimeout(scrollToTitle, 100);
    </script>
    '''
    st.markdown(js, unsafe_allow_html=True)

def write_text_slowly(text):
    """Fonction pour l'effet machine à écrire"""
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"### {text[:i]}▌")
        time.sleep(0.03)
    placeholder.markdown(f"### {text}")

def display_navigation():
    """Affiche le menu de navigation dans la sidebar."""
    options = [
        "🏠 Accueil",
        "👤 Présentation",
        "🔧 Projet",
        "✨ Quiz",
        "📈 Parcours",
        "✉️ Motivation"
    ]
    return st.radio("", options, index=0)

def display_fullscreen_letter():
    """Affiche la lettre en plein écran"""
    overlay_container = st.container()
    with overlay_container:
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            try:
                lettre = Image.open(".assets/lettre_recommandation.jpg")
                st.image(lettre, use_container_width=True)
                if st.button("❌ Fermer", key="close_fullscreen"):
                    st.session_state.lettre_agrandie = False
                    st.rerun()
            except Exception as e:
                st.error("Impossible d'afficher la lettre en plein écran")
                print(f"Erreur: {e}")

def main():
    st.set_page_config(
        page_title="Candidature BUT Science des Données",
        layout="wide"
    )

    # Apply styles
    st.markdown(get_main_styles(), unsafe_allow_html=True)
    
    if 'animation_shown' not in st.session_state:
        st.markdown(get_matrix_styles(), unsafe_allow_html=True)
        display_data_animation()
        st.session_state.animation_shown = True

    # Sidebar
    with st.sidebar:
        col1, col2 = st.columns([4, 1])
        with col2:
            toggle_theme()
        
        st.title("🎯 Navigation")
        selection = display_navigation()  # Store the return value
    
    # Content
    if st.session_state.get('lettre_agrandie', False):
        display_fullscreen_letter()
    
    # Main content based on selection
    if selection == "🏠 Accueil":
        display_home()
    elif selection == "👤 Présentation":
        display_presentation()
    elif selection == "🔧 Projet":
        display_project_concept()
    elif selection == "✨ Quiz":
        title_html = """
            <div style="
                margin-top: 20px;
                margin-bottom: 30px;
                scroll-margin-top: 60px;
            ">
                <h1 id="quiz-title">Découvrez si nous matchons ! ❤️</h1>
            </div>
        """
        st.markdown(title_html, unsafe_allow_html=True)
        scroll_to_section("quiz-title")
        display_quiz()
    elif selection == "📈 Parcours":
        st.markdown('<h1 id="parcours-title" class="custom-title">Mon Parcours</h1>', unsafe_allow_html=True)
        scroll_to_section("parcours-title")
    elif selection == "✉️ Motivation":
        st.markdown('<h1 id="motivation-title" class="custom-title">Ma Motivation</h1>', unsafe_allow_html=True)
        scroll_to_section("motivation-title")

    # Footer
    st.markdown("---")
    st.markdown("*Application interactive créé pour accompagner ma candidature au BUT Science des Données*")

if __name__ == "__main__":
    main()
