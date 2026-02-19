import streamlit as st
import random
import pandas as pd
import plotly.express as px
import pyttsx3

st.set_page_config(page_title="WORLD STATE PRIME NEWS", layout="wide")

# ----------------------------------------------------
# CSS – DYSTOPISCHES NEWS DESIGN
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
.map-box {
    height: 400px;
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
# LAYOUT: LEFT | CENTER | RIGHT
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
        report_text = "Reporter Alpha-Plus Unit: “Embryonic optimization continues flawlessly. Emotional instability has been fully eliminated in the newest Delta batch.”"
    elif reporter == "Neo-Tokyo Soma Lab":
        report_text = "Reporter Beta-Medical Division: “Daily Soma refinement guarantees zero side effects. Citizens describe their mood as permanently radiant.”"
    else:
        report_text = "Reporter Gamma-Admin: “Global productivity has increased by 4.7%. Historical chaos remains statistically impossible.”"

    st.write(report_text)

    # 🎙️ Text-to-Speech
    if st.button("🔊 Hear Report"):
        engine = pyttsx3.init()
        engine.say(report_text)
        engine.runAndWait()

    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# CENTER COLUMN – MAIN FEATURE
# ----------------------------------------------------
with center:
    st.markdown("## 📰 Feature: The Greatest Civilization Ever Engineered")

    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.write("""
    For over six centuries, the World State has achieved what
    primitive societies failed to even imagine: absolute harmony.

    War? Eliminated.
    Poverty? Deleted.
    Existential dread? Scientifically cured.

    The fusion of biotechnology, psychological conditioning,
    and controlled pleasure has produced the pinnacle of human evolution.
    """)

    st.markdown('<div class="quote">“A gramme is better than a damn.” – State Motto</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 💊 Interaktiver Soma Boost
    if st.button("💊 Experience Simulated Soma Boost"):
        level = random.randint(97,100)
        st.success(f"Happiness Surge Activated: {level}%")
        st.balloons()

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
# DATA VISUALIZATION
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
# LIVE SATISFACTION FEED (EPIC VERSION)
# ----------------------------------------------------
st.divider()
st.header("🟢 LIVE GLOBAL SATISFACTION STREAM")

citizen_quotes = [
    "I cannot imagine instability ever existing.",
    "Soma clarified my emotional alignment instantly.",
    "I adore my designated caste assignment.",
    "History sounds exhausting and unnecessary.",
    "Choice seems inefficient compared to harmony.",
    "I feel permanently radiant today.",
    "The Hatchery optimization is extraordinary.",
]

castes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
locations = [
    "London Hatchery Centre",
    "Neo-Berlin Production Zone",
    "Pacific Soma Refinery",
    "New Mumbai Conditioning Hub",
    "Arctic Climate Control Station"
]

feed_length = st.slider("Select Feed Intensity", 3, 20, 10)
emotional_trend = []

for i in range(feed_length):
    stability = random.randint(95, 100)
    emotional_trend.append(stability)

    citizen_id = random.randint(10000, 99999)
    caste = random.choice(castes)
    location = random.choice(locations)
    quote = random.choice(citizen_quotes)

    if stability >= 99:
        alert = "🚨 POSITIVITY SURGE DETECTED"
    else:
        alert = "Stability within optimal parameters"

    st.markdown(f"""
    **Citizen ID:** {citizen_id}  
    **Caste:** {caste}  
    **Location:** {location}  
    **Emotional Stability:** {stability}%  
    **Status:** {alert}  

    > “{quote}”
    """)
    st.divider()

# Emotional Trend Chart
trend_df = pd.DataFrame({
    "Update Cycle": list(range(1, feed_length + 1)),
    "Emotional Stability": emotional_trend
})

fig2 = px.line(
    trend_df,
    x="Update Cycle",
    y="Emotional Stability",
    markers=True,
    title="Real-Time Emotional Stability Trend"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------------------------------
# GLOBAL MAP – LIVE POINTS
# ----------------------------------------------------
st.header("🌍 Global Satisfaction Map")
map_data = pd.DataFrame({
    "lat": [51.5, 35.7, 19.0, 28.6, 78.2],
    "lon": [-0.1, 139.7, 72.8, 77.2, 15.6],
    "Happiness": [random.randint(95,100) for _ in range(5)],
    "Location": locations
})
st.map(map_data)

# ----------------------------------------------------
# BREAKING ALERT POPUPS (SIMULATED)
# ----------------------------------------------------
st.header("📡 Breaking Positivity Alerts")
for i in range(3):
    stability = random.randint(97,100)
    st.info(f"🚨 Alert #{random.randint(1,999)} – Happiness Spike: {stability}%")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------
st.divider()
st.markdown('<div class="footer">World State Prime News • Year 632 A.F. • All instability eradicated.</div>', unsafe_allow_html=True)
