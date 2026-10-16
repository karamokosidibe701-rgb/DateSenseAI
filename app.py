
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="DateSenseAI",
    page_icon="🎂",
    layout="centered"
)

st.title("🎂 DateSenseAI")
st.subheader("Combien de jours avant ton prochain anniversaire ?")

st.write(
    "Entre ta date de naissance pour découvrir "
    "ton compte à rebours personnalisé."
)

naissance = st.date_input(
    "Ta date de naissance",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="DD/MM/YYYY"
)

if st.button("Calculer mon compte à rebours"):
    aujourd_hui = date.today()

    # Calculer le prochain anniversaire
    try:
        anniversaire = date(
            aujourd_hui.year,
            naissance.month,
            naissance.day
        )
    except ValueError:
        # Cas d'une naissance le 29 février
        anniversaire = date(aujourd_hui.year, 2, 28)

    # Si l'anniversaire est aujourd'hui ou déjà passé,
    # chercher celui de l'année suivante
    if anniversaire <= aujourd_hui:
        try:
            anniversaire = date(
                aujourd_hui.year + 1,
                naissance.month,
                naissance.day
            )
        except ValueError:
            anniversaire = date(aujourd_hui.year + 1, 2, 28)

    jours_restants = (anniversaire - aujourd_hui).days

    st.success(f"🎉 Il te reste {jours_restants} jour(s) !")

    st.write(
        "Ton prochain anniversaire sera le "
        f"{anniversaire.strftime('%d/%m/%Y')}."
    )

st.caption(
    "DateSenseAI — Un projet Python autour des dates "
    "et du machine learning."
)
