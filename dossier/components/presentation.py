import streamlit as st
import streamlit.components.v1 as components

def display_presentation():
    presentation_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
        <style>
            body {
                background-color: #0e1117;
                color: #fff;
                font-family: system-ui, -apple-system, sans-serif;
                margin: 0;
                padding: 1rem;
            }

            .profile-container {
                max-width: 1000px;
                margin: 0 auto;
            }

            .profile-header {
                text-align: center;
                margin-bottom: 2rem;
                padding: 1rem;
                border-radius: 12px;
                background: linear-gradient(180deg, rgba(30, 41, 59, 0.5) 0%, rgba(30, 41, 59, 0) 100%);
            }

            .section-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 2rem;
            }

            @media (max-width: 1200px) {
                .section-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
            }

            @media (max-width: 768px) {
                .section-grid {
                    grid-template-columns: 1fr;
                }
            }

            .section {
                background-color: #1a1d23;
                border-radius: 12px;
                padding: 1.5rem;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                border: 1px solid rgba(255, 255, 255, 0.1);
                min-height: 250px;
                display: flex;
                flex-direction: column;
            }

            .section:hover {
                transform: translateY(-4px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
                border-color: rgba(96, 165, 250, 0.4);
            }

            .section-header {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                margin-bottom: 1rem;
                padding-bottom: 0.75rem;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }

            .icon {
                width: 1.75rem;
                height: 1.75rem;
                padding: 0.375rem;
                border-radius: 8px;
                background: rgba(96, 165, 250, 0.1);
            }

            .section-title {
                font-size: 1.25rem;
                font-weight: 600;
                color: #fff;
                margin: 0;
            }

            .content-list {
                list-style: none;
                padding: 0;
                margin: 0;
            }

            .content-item {
                display: flex;
                align-items: center;
                padding: 0.5rem 0;
                color: #cbd5e1;
                transition: all 0.2s ease;
            }

            .content-item::before {
                content: "▹";
                color: #60a5fa;
                margin-right: 0.75rem;
            }

            .content-item:hover {
                color: #fff;
                transform: translateX(4px);
            }

            .badge {
                background: rgba(96, 165, 250, 0.1);
                color: #60a5fa;
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.875rem;
                margin-left: auto;
            }

            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            .animate-slide {
                animation: slideIn 0.5s ease-out forwards;
            }
        </style>
    </head>
    <body>
        <div id="profile-root"></div>
        <script type="text/babel">
            const sections = [
                {
                    icon: "👤",
                    title: "À propos de moi",
                    items: [
                        "25 ans, originaire du Sud de la France (Perpignan)",
                        "Passionné de technologie et d'innovation",
                        "Amateur de musique classique, particulièrement le piano",
                        "Sportif et ancien champion de pentathlon"
                    ]
                },
                {
                    icon: "🌟",
                    title: "Centres d'intérêt",
                    items: [
                        "Exploration de Paris et de sa scène culturelle",
                        "Concerts de musique classique",
                        "Veille technologique",
                        "Sport et bien-être"
                    ]
                },
                {
                    icon: "📚",
                    title: "Formation en cours",
                    items: [
                        "DAEU B - Équivalent Bac Scientifique",
                        "Spécialisation en Mathématiques",
                        "Excellent niveau académique"
                    ],
                    badge: "En cours"
                },
                {
                    icon: "💼",
                    title: "Expérience Professionnelle",
                    items: [
                        "Plongeur Scaphandrier en Travaux Publics",
                        "Gestion de projets techniques complexes",
                        "Travail en équipe et sous pression"
                    ]
                },
                {
                    icon: "🎯",
                    title: "Points Forts",
                    items: [
                        "Capacité d'adaptation",
                        "Résolution des problèmes",
                        "Rigueur et précision dans le travail"
                        "Détermination et persévérance"
                        "Esprit d'équipe"
                        
                    ]
                },
                {
                    icon: "🚀",
                    title: "Ambition",
                    items: [
                        "Me préparer à un Master ou une école d'ingénieur",
                        "Évoluer professionnellement dans un domaine innovant",
                        "Apprendre à utiliser la Data pour concrétiser des projets",
                        "Combiner mathématiques et programmation",
                        "Relever de nouveaux défis stimulants"
                    ]
                }
            ];

            const Section = ({ icon, title, items, badge, delay }) => (
                <div 
                    className="section animate-slide" 
                    style={{ animationDelay: `${delay}s` }}
                >
                    <div className="section-header">
                        <span className="icon">{icon}</span>
                        <h3 className="section-title">{title}</h3>
                        {badge && <span className="badge">{badge}</span>}
                    </div>
                    <ul className="content-list">
                        {items.map((item, i) => (
                            <li key={i} className="content-item">
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>
            );

            const Profile = () => (
                <div className="profile-container">
                    <div className="profile-header animate-slide">
                        <h2 style={{ fontSize: '2rem', margin: '0', background: 'linear-gradient(135deg, #60A5FA, #818CF8)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
                            Qui suis-je ?
                        </h2>
                    </div>
                    <div className="section-grid">
                        {sections.map((section, index) => (
                            <Section 
                                key={index} 
                                {...section} 
                                delay={index * 0.1}
                            />
                        ))}
                    </div>
                </div>
            );

            ReactDOM.render(<Profile />, document.getElementById('profile-root'));
        </script>
    </body>
    </html>
    """
    
    # Pour éviter les marges par défaut de Streamlit
    st.markdown("""
        <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Modifiez la dernière ligne de la fonction display_presentation
    components.html(presentation_html, height=1200, scrolling=False)  # Increased height from 900 to 1200

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    display_presentation()