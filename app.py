
import streamlit as st
from datetime import date
import calendar

# -----------------------------
# Configuration de la page
# -----------------------------
st.set_page_config(
    page_title="DateSenseAI | Birthday Countdown",
    page_icon="🎂",
    layout="centered"
)

# -----------------------------
# Style visuel
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f3ff, #eff6ff);
}

.block-container {
    max-width: 760px;
    padding-top: 2.5rem;
    padding-bottom: 2rem;
}

.hero {
    text-align: center;
    padding: 1.5rem 0;
}

.hero h1 {
    color: #4338ca;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
}

.hero p {
    color: #475569;
    font-size: 1.05rem;
}

.stButton > button {
    background-color: #4338ca;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.75rem;
    font-weight: 700;
    width: 100%;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #3730a3;
    color: white;
    border: none;
}

.result-card {
    background: white;
    border: 1px solid #e0e7ff;
    border-radius: 22px;
    padding: 2rem 1rem;
    text-align: center;
    margin: 1.5rem 0 1rem 0;
    box-shadow: 0 8px 25px rgba(67, 56, 202, 0.10);
}

.result-emoji {
    font-size: 2.5rem;
}

.result-days {
    color: #4338ca;
    font-size: 3.3rem;
    font-weight: 800;
    margin: 0.5rem 0;
}

.result-caption {
    color: #475569;
    font-size: 1.1rem;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 0.85rem;
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# En-tête
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🎂 DateSenseAI</h1>
    <p>Every birthday deserves a countdown.</p>
    <p>Discover how many days remain until your next birthday.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Saisie de la date
# -----------------------------
st.subheader("🎈 Your birthday")

naissance = st.date_input(
    "Select your date of birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="DD/MM/YYYY"
)

# -----------------------------
# Calcul du compte à rebours
# -----------------------------
if st.button("✨ Calculate my countdown"):

    aujourd_hui = date.today()

    # Déterminer le prochain anniversaire
    annee = aujourd_hui.year

    # Cas du 29 février
    jour_anniversaire = naissance.day
    if naissance.month == 2 and naissance.day == 29:
        jour_anniversaire = 29 if calendar.isleap(annee) else 28

    anniversaire = date(
        annee,
        naissance.month,
        jour_anniversaire
    )

    # Si l'anniversaire est aujourd'hui ou déjà passé,
    # chercher celui de l'année suivante
    if anniversaire <= aujourd_hui:
        annee += 1
        jour_anniversaire = naissance.day

        if naissance.month == 2 and naissance.day == 29:
            jour_anniversaire = 29 if calendar.isleap(annee) else 28

        anniversaire = date(
            annee,
            naissance.month,
            jour_anniversaire
        )

    jours_restants = (anniversaire - aujourd_hui).days
    age_prochain = anniversaire.year - naissance.year

    # Jour de la semaine en français
    jours_fr = [
        "lundi", "mardi", "mercredi", "jeudi",
        "vendredi", "samedi", "dimanche"
    ]

    mois_fr = [
        "janvier", "février", "mars", "avril",
        "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"
    ]

    jour_semaine = jours_fr[anniversaire.weekday()]
    date_fr = (
        f"{jour_semaine} {anniversaire.day} "
        f"{mois_fr[anniversaire.month - 1]} "
        f"{anniversaire.year}"
    )

    # -----------------------------
    # Affichage du résultat
    # -----------------------------
    st.markdown(f"""
    <div class="result-card">
        <div class="result-emoji">🎉</div>
        <div class="result-days">{jours_restants} jours</div>
        <div class="result-caption">
            avant ton prochain anniversaire
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.success(f"📅 Ton prochain anniversaire sera le {date_fr}.")
    st.info(f"🎂 Tu auras {age_prochain} ans !")

    if jours_restants == 1:
        st.balloons()
        st.write("🎁 Plus qu'un jour à attendre !")
    elif jours_restants == 0:
        st.balloons()
        st.write("🎉 Joyeux anniversaire !")

# -----------------------------
# Pied de page
# -----------------------------
st.divider()

st.markdown("""
<div class="footer">
    DateSenseAI · Built with Python and Streamlit<br>
    A learning project exploring dates and machine learning.
</div>
""", unsafe_allow_html=True)

