import streamlit as st

st.set_page_config(
    page_title="OBE Detective",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 OBE Detective")
st.subheader("Can you rescue this lesson plan?")

st.info("You have 3 minutes to identify and repair the OBE alignment problem.")

st.markdown("""
### Lesson Scenario

**CLO:** Students will be able to **evaluate persuasive strategies** in an argumentative text.

**Teaching:** The teacher explains five persuasive strategies using slides.

**Activity:** Students underline persuasive words in a sample text.

**Assessment:** Students list five persuasive strategies.
""")

st.divider()

st.subheader("1️⃣ Give your OBE verdict")

verdict = st.radio(
    "How OBE-aligned is this lesson?",
    ["🟢 OBE READY", "🟡 OBE-ish", "🔴 OBE BLIND"],
    index=None
)

st.subheader("2️⃣ Find the alignment break")

problem = st.radio(
    "Where is the main problem?",
    [
        "CLO ↔ Teaching",
        "CLO ↔ Activity",
        "CLO ↔ Assessment",
        "Everything is aligned"
    ],
    index=None
)

st.subheader("3️⃣ Repair the lesson")

repair = st.radio(
    "Which assessment best aligns with the CLO?",
    [
        "A. Define persuasive strategy.",
        "B. List five persuasive strategies.",
        "C. Evaluate which persuasive strategy is most effective and justify your answer."
    ],
    index=None
)

if st.button("🔍 Reveal My OBE Score", use_container_width=True):

    score = 0

    if verdict == "🔴 OBE BLIND":
        score += 1

    if problem == "CLO ↔ Assessment":
        score += 1

    if repair and repair.startswith("C."):
        score += 1

    if score == 3:
        st.success("🏆 OBE ARCHITECT — Alignment Restored!")
        st.balloons()

    elif score == 2:
        st.warning("🔎 OBE DETECTIVE — Almost there!")

    else:
        st.error("🛠️ ALIGNMENT APPRENTICE — Look again!")

    st.markdown("""
    ### Why?

    The CLO requires students to **evaluate**, but the original assessment only asks them to **list**.

    **Evaluate → List ❌**

    After the repair:

    **Evaluate → Evaluate + Justify ✅**

    ### Constructive Alignment

    **CLO → Teaching & Learning → Assessment**
    """)

    st.divider()

    st.markdown("""
    ### 💡 The Bigger Question

    You just repaired the alignment manually.

    **Can AI help us design this alignment correctly from the beginning?**
    """)

    st.success("➡️ Let's find out with the OBE Lesson Planner!")
