
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="DateSenseAI | Birthday Countdown",
    page_icon="🎂",
    layout="centered"
)

# Style visuel
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f3ff, #eff6ff);
}
.block-container {
    max-width: 750px;
    padding-top: 3rem;
}
.hero {
    text-align: center;
    padding: 2rem 1rem;
}
.hero h1 {
    color: #4338ca;
    font-size: 3rem;
    margin-bottom: 0.4rem;
}
.hero p {
    color: #475569;
    font-size: 1.1rem;
}
.result {
    background: white;
    border: 1px solid #e0e7ff;
    border-radius: 20px;
    padding: 2rem 1rem;
    text-align: center;
    margin-top: 1rem;
    box-shadow: 0 8px 25px rgba(67, 56, 202, 0.08);
}
.days {
    color: #4338ca;
    font-size: 3.2rem;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🎂 DateSenseAI</h1>
    <p>Every birthday deserves a countdown.</p>
    <p>Discover how many days remain until your next birthday.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🎈 Your birthday")

naissance = st.date_input(
    "Select your date of birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="DD/MM/YYYY"
)

if st.button("✨ Calculate my countdown", use_container_width=True):
    today = date.today()

    try:
        birthday = date(today.year, naissance.month, naissance.day)
    except ValueError:
        birthday = date(today.year, 2, 28)

    if birthday <= today:
        try:
            birthday = date(today.year + 1, naissance.month, naissance.day)
        except ValueError:
            birthday = date(today.year + 1, 2, 28)

    days_left = (birthday - today).days
    age_next = birthday.year - naissance.year

    st.markdown(f"""
    <div class="result">
        <div style="font-size: 2.5rem;">🎉</div>
        <div class="days">{days_left} days</div>
        <div style="color: #475569; font-size: 1.1rem;">
            until your next birthday
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.success(
        f"Your next birthday is on {birthday.strftime('%d/%m/%Y')}."
    )
    st.info(f"You will turn {age_next} years old!")

st.divider()

st.caption(
    "DateSenseAI | Built with Python and Streamlit | A learning project"
)

