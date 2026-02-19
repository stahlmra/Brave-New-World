import streamlit as st
import random
import pandas as pd
import plotly.express as px
import pyttsx3
import numpy as np

st.set_page_config(page_title="WORLD STATE PRIME NEWS – Join the Perfect World", layout="wide")

# -------------------------
# CSS Styling
# -------------------------
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
.join-box {
    background-color:#1a2230;
    padding:30px;
    border-radius:15px;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown('<div class="title">WORLD STATE PRIME NEWS</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Community • Stability • Happiness</div>', unsafe_allow_html=True)
st.markdown('<div class="breaking">LIVE: Civilization Perfected – Join the World State Today!</div>', unsafe_allow_html=True)
st.divider()

# -------------------------
# LAYOUT: LEFT | CENTER | RIGHT
# -------------------------
left, center, right = st.columns([1,2,1])

# -------------------------
# LEFT COLUMN – REPORTERS & TTS
# -------------------------
with left:
    st.markdown("### 🎙️ Field Reporters – Always Reporting Success")
    reporter = st.selectbox(
        "Select Live Reporter",
        ["London Hatchery Centre", "Neo-Tokyo Soma Lab", "Global Stability Office"]
    )
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    if reporter == "London Hatchery Centre":
        report_text = "Reporter Alpha-Plus Unit: 'Embryonic optimization continues flawlessly. All citizens are perfectly aligned with happiness.'"
    elif reporter == "Neo-Tokyo Soma Lab":
        report_text = "Reporter Beta-Medical Division: 'Soma refinement guarantees permanent bliss. Emotional balance achieved in 100% of trials.'"
    else:
        report_text = "Reporter Gamma-Admin: 'Global productivity and happiness reach unprecedented levels. Instability eliminated.'"

    st.write(report_text)
    if st.button("🔊 Hear Report"):
        engine = pyttsx3.init()
        engine.say(report_text)
        engine.runAndWait()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# CENTER COLUMN – FEATURE STORY
# -------------------------
with center:
    st.markdown("## 📰 Feature: The Greatest Civilization Ever Engineered")
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.write("""
    For centuries, the World State has achieved perfection.  
    Wars? Eliminated.  
    Poverty? Gone.  
    Emotional instability? Scientifically cured.  

    Every citizen thrives in their caste, every ambition harmonized with society's ultimate goal.  
    Individual freedom has been upgraded to **freedom from suffering**.  
    """)
    st.markdown('<div class="quote">“A gramme is better than a damn.” – Official State Motto</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("💊 Experience Simulated Soma Boost"):
        level = random.randint(97,100)
        st.success(f"Happiness Surge Activated: {level}%")
        st.balloons()

# -------------------------
# RIGHT COLUMN – METRICS DASHBOARD
# -------------------------
with right:
    st.markdown("### 📊 Global Stability Dashboard")
    happiness = random.randint(98,100)
    obedience = random.randint(96,100)
    consumption = random.randint(94,100)
    st.metric("Happiness Index", f"{happiness}%")
    st.metric("Social Harmony", f"{obedience}%")
    st.metric("Consumer Activity", f"{consumption}%")
    st.progress(happiness/100)

# -------------------------
# DATA VISUALIZATION
# -------------------------
st.divider()
st.header("📈 Historical Comparison: Pre-World State vs. World State")
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

# -------------------------
# LIVE SATISFACTION FEED
# -------------------------
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
    "London Hatchery", "Neo-Berlin Production", "Pacific Soma Lab",
    "New Mumbai Conditioning", "Arctic Climate Station", "Sao Paulo Bio-Lab",
    "Cape Town Stability Center", "Tokyo Genetic Unit", "Sydney Harmony Hub"
]
feed_length = st.slider("Select Feed Intensity", 5, 30, 10)
emotional_trend = []

for i in range(feed_length):
    stability = random.randint(95, 100)
    emotional_trend.append(stability)
    citizen_id = random.randint(10000,99999)
    caste = random.choice(castes)
    location = random.choice(locations)
    quote = random.choice(citizen_quotes)
    alert = "🚨 POSITIVITY SURGE!" if stability>=99 else "Stability Optimal"
    st.markdown(f"""
**Citizen ID:** {citizen_id}  
**Caste:** {caste}  
**Location:** {location}  
**Happiness:** {stability}%  
**Status:** {alert}  

> “{quote}”
""")
    st.divider()

# Emotional Trend Chart
trend_df = pd.DataFrame({
    "Update Cycle": list(range(1, feed_length+1)),
    "Emotional Stability": emotional_trend
})
fig2 = px.line(trend_df, x="Update Cycle", y="Emotional Stability",
               markers=True, title="Real-Time Emotional Stability Trend")
st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# GLOBAL MAP
# -------------------------
st.header("🌍 Global Satisfaction Map")
map_points = 50
latitudes = np.random.uniform(-60,80,map_points)
longitudes = np.random.uniform(-180,180,map_points)
happiness_values = np.random.randint(95,101,map_points)
castes_values = np.random.choice(castes,map_points)
locations_values = [f"Location {i+1}" for i in range(map_points)]
map_data = pd.DataFrame({
    "lat": latitudes, "lon": longitudes,
    "Happiness": happiness_values, "Caste": castes_values,
    "Location": locations_values
})
fig_map = px.scatter_mapbox(
    map_data, lat="lat", lon="lon",
    size="Happiness", color="Happiness",
    hover_name="Location", hover_data=["Caste","Happiness"],
    color_continuous_scale=px.colors.sequential.Viridis,
    size_max=15, zoom=1
)
fig_map.update_layout(mapbox_style="carto-darkmatter", margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig_map, use_container_width=True)

# -------------------------
# BREAKING POSITIVITY ALERTS
# -------------------------
st.header("📡 Breaking Positivity Alerts")
alerts_triggered = map_data[map_data["Happiness"]>=99]
if not alerts_triggered.empty:
    for idx,row in alerts_triggered.iterrows():
        st.success(f"🚨 {row['Location']} – Happiness {row['Happiness']}% – Caste: {row['Caste']}")
else:
    st.info("No extreme positivity detected – all citizens are optimally happy!")

# -------------------------
# CALL-TO-ACTION FORM
# -------------------------
st.divider()
st.header("📝 Join the World State – Become Part of Perfection")
st.markdown('<div class="join-box">', unsafe_allow_html=True)
with st.form("join_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=10, max_value=100)
    caste_pref = st.selectbox("Preferred Caste Assignment", ["Alpha","Beta","Gamma","Delta","Epsilon"])
    submit = st.form_submit_button("✅ I Am Ready to Join")
    if submit:
        st.success(f"Welcome, {name}! You will soon be assigned to the {caste_pref} caste. Prepare for eternal happiness! 🎉")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.divider()
st.markdown('<div class="footer">World State Prime News • Year 632 A.F. • Happiness Guaranteed</div>', unsafe_allow_html=True)
