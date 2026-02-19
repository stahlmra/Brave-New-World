import streamlit as st
import random
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="WORLD STATE PRIME NEWS", layout="wide")

# ----------------------------------------------------
# MEGA CSS – DRAMATIC NEWS LOOK
# ----------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #0b0f17;
    color: white;
}
.title {
    font-size: 54px;
    font-weight: 900;
    text-align:center;
}
.subtitle {
    text-align:center;
    color: #cccccc;
}
.breaking {
    background-color: #cc0000;
    padding: 12px;
    font-weight:bold;
    font-size:18px;
    text-align:center;
}
.section-box {
    background-color: #141a26;
    padding: 20px;
    border-radius: 12px;
    margin-bottom:20px;
}
.quote {
    font-style: italic;
    font-size: 18px;
    color: #aaaaaa;
}
.footer {
    text-align:center;
    font-size:12px;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------
st.markdown('<div class="title">WORLD STATE PRIME NEWS</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Community • Stability • Identity</div>', unsafe_allow_html=True)
st.markdown('<div class="breaking">LIVE: Global Happiness Surpasses 99.9% – Civilization Declared Perfect</div>', unsafe_allow_html=True)
st.divider()

# ----------------------------------------------------
# LAYOUT
# ----------------------------------------------------
left, center, right = st.columns([1,2,1])

# ----------------------------------------------------
# LEFT COLUMN – LIVE REPORTERS
# ----------------------------------------------------
with left:
    st.markdown("### 🎙️ Field Reporters")

    reporter = st.selectbox(
        "Select Live Reporter",
        ["London Hatchery Centre", "Neo-Tokyo Soma Lab", "Global Stability Office"]
    )

    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    if reporter == "London Hatchery Centre":
        st.write("Reporter Alpha-Plus Unit:")
        st.write("""
        “Embryonic optimization continues flawlessly. 
        Emotional instability has been fully eliminated 
        in the newest Delta batch.”
        """)

    elif reporter == "Neo-Tokyo Soma Lab":
        st.write("Reporter Beta-Medical Division:")
        st.write("""
        “Daily Soma refinement guarantees zero side effects.
        Citizens describe their mood as permanently radiant.”
        """)

    else:
        st.write("Reporter Gamma-Admin:")
        st.write("""
        “Global productivity has increased by 4.7%.
        Historical chaos remains statistically impossible.”
        """)

    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# CENTER COLUMN – MAIN STORY
# ----------------------------------------------------
with center:
    st.markdown("## 📰 Feature: The Greatest Civilization Ever Engineered")

    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.write("""
    For over six centuries, the World State has achieved what
    primitive societies failed to even imagine:
    absolute harmony.

    War? Eliminated.
    Poverty? Deleted.
    Existential dread? Scientifically cured.

    The fusion of biotechnology, psychological conditioning,
    and controlled pleasure has produced the pinnacle of human evolution.
    """)

    st.markdown('<div class="quote">“A gramme is better than a damn.” – State Motto</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # INTERACTIVE SOMA BOOST
    if st.button("💊 Experience Simulated Soma Boost"):
        level = random.randint(97,100)
        st.success(f"Happiness Surge Activated: {level}%")

# ----------------------------------------------------
# RIGHT COLUMN – METRICS DASHBOARD
# ----------------------------------------------------
with right:
    st.markdown("### 📊 Global Stability Dashboard")

    happiness = random.randint(98,100)
    obedience = random.randint(96,100)
    consumption = random.randint(94,100)

    st.metric("Happiness Index", f"{happiness}%")
    st.metric("Social Harmony", f"{obedience}%")
    st.metric("Consumer Activity", f"{consumption}%")

    st.progress(happiness/100)

# ----------------------------------------------------
# DATA VISUALIZATION SECTION
# ----------------------------------------------------
st.divider()
st.header("📈 Historical Comparison: Before vs World State")

data = pd.DataFrame({
    "Era": ["Pre-World State", "World State Era"],
    "War Rate": [85, 0],
    "Depression Rate": [72, 1],
    "Happiness Index": [40, 99]
})

fig = px.bar(data, x="Era", y=["War Rate","Depression Rate","Happiness Index"],
             barmode="group",
             title="Civilizational Upgrade Metrics")

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# LIVE NEWS TICKER
# ----------------------------------------------------
st.divider()
st.header("📰 Live Satisfaction Feed")

for i in range(3):
    mood = random.randint(95,100)
    st.write(f"Citizen Report #{random.randint(1000,9999)} – Emotional Stability: {mood}%")
    time.sleep(0.3)

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------
st.divider()
st.markdown('<div class="footer">World State Prime News • Year 632 A.F. • All instability eradicated.</div>', unsafe_allow_html=True)
