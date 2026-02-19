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
# FOOTER
# ----------------------------------------------------
st.divider()
st.markdown('<div class="footer">World State Prime News • Year 632 A.F. • All instability eradicated.</div>', unsafe_allow_html=True)

st.header("🌍 Global Satisfaction Map – Mega Edition")

# Generiere viele zufällige Punkte
locations = [
    "London Hatchery Centre", "Neo-Berlin Production Zone", "Pacific Soma Refinery",
    "New Mumbai Conditioning Hub", "Arctic Climate Control Station", "Sao Paulo Bio-Lab",
    "Cape Town Stability Center", "Tokyo Genetic Unit", "Sydney Harmony Hub",
    "Moscow Admin Office", "Toronto Soma Lab", "Beijing Optimization Centre",
    "Paris Productivity Zone", "Dubai Happiness Hub", "Singapore Conditioning Unit",
    "Seoul Genetic Refinery", "Mexico City Control Hub", "Istanbul Stability Office",
    "Bangkok Emotion Lab", "Cairo Harmony Station", "Buenos Aires Bio-Lab",
    "Lagos Optimization Centre", "Jakarta Conditioning Hub", "Berlin Happiness Unit",
    "Rome Admin Office", "Madrid Stability Centre", "Lisbon Genetic Lab",
    "Stockholm Emotional Refinery", "Helsinki Harmony Hub", "Oslo Productivity Zone",
    "Vienna Bio-Lab", "Warsaw Optimization Centre", "Athens Stability Office",
    "Budapest Happiness Unit", "Prague Conditioning Hub", "Zurich Genetic Refinery",
    "Brussels Emotion Lab", "Amsterdam Harmony Station", "Copenhagen Bio-Lab",
    "Reykjavik Optimization Centre", "Havana Happiness Hub", "Lima Conditioning Unit",
    "Bogota Genetic Lab", "Santiago Emotion Refinery", "Rio de Janeiro Stability Station",
    "Kuala Lumpur Harmony Hub", "Manila Bio-Lab", "Bangladesh Optimization Unit",
    "Mumbai Happiness Lab", "Beijing Conditioning Centre", "Tokyo Genetic Refinery"
]

# Zufällige lat/lon für Demo
import numpy as np
latitudes = np.random.uniform(-60, 80, len(locations))
longitudes = np.random.uniform(-180, 180, len(locations))
happiness_values = np.random.randint(95, 101, len(locations))
castes_values = np.random.choice(["Alpha","Beta","Gamma","Delta","Epsilon"], len(locations))

map_data = pd.DataFrame({
    "lat": latitudes,
    "lon": longitudes,
    "Location": locations,
    "Happiness": happiness_values,
    "Caste": castes_values
})

# Streamlit Map
st.map(map_data[["lat","lon"]])

# Interaktive Plotly Map für Tooltip + Alerts
st.markdown("### 🌐 Interactive Happiness Map")
fig_map = px.scatter_mapbox(
    map_data,
    lat="lat",
    lon="lon",
    size="Happiness",
    color="Happiness",
    hover_name="Location",
    hover_data=["Happiness","Caste"],
    color_continuous_scale=px.colors.sequential.Viridis,
    size_max=15,
    zoom=1
)
fig_map.update_layout(mapbox_style="carto-darkmatter")
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig_map, use_container_width=True)

# ----------------------------------------------------
# BREAKING POSITIVITY ALERTS
# ----------------------------------------------------
st.header("📡 Breaking Positivity Alerts – Mega Edition")
alerts_triggered = map_data[map_data["Happiness"] >= 99]

if not alerts_triggered.empty:
    for idx, row in alerts_triggered.iterrows():
        st.success(f"🚨 Breaking Positivity Alert: {row['Location']} – Happiness {row['Happiness']}% – Caste: {row['Caste']}")
else:
    st.info("No extreme positivity detected at this moment – global stability remains optimal.")
