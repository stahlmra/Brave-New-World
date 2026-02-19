import streamlit as st
import random

st.set_page_config(page_title="World State News Network", layout="wide")

# -------------------------
# Fake Styling (News Look)
# -------------------------
st.markdown("""
<style>
.main-title {
    font-size:40px;
    font-weight:bold;
}
.sub-title {
    font-size:18px;
    color:gray;
}
.headline {
    font-size:24px;
    font-weight:bold;
}
.article-box {
    padding:20px;
    border-radius:10px;
    background-color:#111111;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.markdown('<div class="main-title">WORLD STATE NEWS NETWORK</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Stability • Community • Identity</div>', unsafe_allow_html=True)
st.divider()

# -------------------------
# Sidebar
# -------------------------
section = st.sidebar.radio(
    "Navigation",
    ["Home", "Society", "Technology", "Soma Reports", "Opinion", "Citizen Satisfaction Index"]
)

# -------------------------
# HOME
# -------------------------
if section == "Home":
    st.header("Top Stories")

    st.markdown("### The Genius of Social Stability")
    st.write("""
    For over six centuries, the World State has ensured peace,
    happiness and stability. Unlike the chaotic past,
    modern citizens enjoy perfect harmony.
    
    Individual conflict has been replaced with collective joy.
    """)
    if st.button("Read Full Article – Stability"):
        st.session_state.article = "stability"

    st.markdown("### Why Individuality Was the Greatest Threat")
    st.write("""
    History has proven that excessive individuality leads to war,
    suffering and instability. The caste system guarantees balance.
    """)
    if st.button("Read Full Article – Individuality"):
        st.session_state.article = "individuality"

    st.markdown("### Soma: The Scientific Breakthrough of Happiness")
    st.write("""
    A gramme is better than a damn.
    Citizens report 99.8% emotional satisfaction.
    """)
    if st.button("Read Full Article – Soma"):
        st.session_state.article = "soma"

# -------------------------
# ARTICLE VIEW
# -------------------------
if "article" in st.session_state:

    st.divider()
    st.subheader("Full Article")

    if st.session_state.article == "stability":
        st.write("""
        Stability is the foundation of civilization.
        Through genetic engineering and intelligent social conditioning,
        society has eliminated unemployment, depression and war.

        The caste system ensures that every citizen loves their role.
        Conflict is obsolete.
        """)
        st.write("""
        Compared to the unstable past,
        the World State represents the highest stage of human evolution.
        """)

    elif st.session_state.article == "individuality":
        st.write("""
        Individuality once caused revolutions, wars and inequality.
        By limiting personal ambition, the World State removed chaos.
        Identity is now collective — and therefore peaceful.
        """)

    elif st.session_state.article == "soma":
        st.write("""
        Soma is the greatest pharmaceutical innovation in history.
        It provides emotional balance without side effects.

        No hangover.
        No addiction.
        No suffering.

        Happiness is guaranteed.
        """)

# -------------------------
# SOCIETY
# -------------------------
elif section == "Society":
    st.header("The Perfect Caste Structure")

    caste = st.selectbox("Choose a Caste", ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

    caste_info = {
        "Alpha": "Leaders and intellectual elite. Maximum cognitive capacity.",
        "Beta": "Specialists and administrators. Highly efficient.",
        "Gamma": "Skilled workforce maintaining society.",
        "Delta": "Operational backbone of production.",
        "Epsilon": "Optimized for essential physical labor."
    }

    st.write(caste_info[caste])

# -------------------------
# TECHNOLOGY
# -------------------------
elif section == "Technology":
    st.header("Scientific Advancement")

    st.write("""
    Human reproduction is now efficient and controlled.
    Emotional instability has been engineered out.
    Mass production ensures universal comfort.
    """)

# -------------------------
# SOMA REPORTS
# -------------------------
elif section == "Soma Reports":
    st.header("Daily Soma Distribution")

    st.write("Take your daily dose for maximum happiness.")
    if st.button("Take Soma"):
        happiness = random.randint(90, 100)
        st.success(f"Emotional Stability Increased to {happiness}%")

# -------------------------
# OPINION
# -------------------------
elif section == "Opinion":
    st.header("Editorial: Why the Old World Failed")

    st.write("""
    Democracy created division.
    Religion created conflict.
    Art created dissatisfaction.

    The World State replaced all inefficiencies with engineered contentment.
    True freedom is freedom from pain.
    """)

# -------------------------
# CITIZEN INDEX
# -------------------------
elif section == "Citizen Satisfaction Index":
    st.header("Citizen Satisfaction Index")

    score = random.randint(95, 100)
    st.metric("Global Happiness Level", f"{score}%")
    st.progress(score / 100)

    st.write("Historical average: 99.3% happiness since Year 632 A.F.")
