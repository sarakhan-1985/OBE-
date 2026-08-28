import streamlit as st
import random

# ------------------------------------------------
# PAGE SETUP
# ------------------------------------------------

st.set_page_config(
    page_title="Crack the OBE Code",
    page_icon="🔐",
    layout="centered"
)

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------

st.markdown("""
<style>

.title {
    text-align:center;
    font-size:48px;
    font-weight:900;
    margin-bottom:0;
}

.subtitle {
    text-align:center;
    font-size:22px;
    font-weight:600;
    margin-bottom:25px;
}

.card {
    padding:25px;
    border-radius:18px;
    border:3px solid #ddd;
    text-align:center;
    font-size:22px;
    font-weight:700;
    margin-top:20px;
    margin-bottom:25px;
    background-color:#fafafa;
}

.station {
    text-align:center;
    padding:10px;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------
# BLOOM CARDS
# ------------------------------------------------

cards = [

    {
        "text": "List five characteristics of academic writing.",
        "answer": "Remember",
        "reason": "The learner is recalling previously learned information."
    },

    {
        "text": "Explain constructive alignment in your own words.",
        "answer": "Understand",
        "reason": "The learner demonstrates understanding by explaining an idea."
    },

    {
        "text": "Use the given rubric to assess a sample paragraph.",
        "answer": "Apply",
        "reason": "The learner uses knowledge or a procedure in a new task."
    },

    {
        "text": "Compare two lesson plans and identify differences in CLO alignment.",
        "answer": "Analyze",
        "reason": "The learner breaks information into parts and examines relationships."
    },

    {
        "text": "Judge which assessment method best measures the CLO and justify your answer.",
        "answer": "Evaluate",
        "reason": "The learner makes a judgement using criteria and evidence."
    },

    {
        "text": "Design an OBE-aligned classroom activity for the given CLO.",
        "answer": "Create",
        "reason": "The learner produces something new."
    },

    {
        "text": "Define Outcome-Based Education.",
        "answer": "Remember",
        "reason": "The learner retrieves a definition from memory."
    },

    {
        "text": "Summarize the main principles of OBE.",
        "answer": "Understand",
        "reason": "Summarising demonstrates comprehension of information."
    },

    {
        "text": "Demonstrate how Bloom's Taxonomy can be used to revise a CLO.",
        "answer": "Apply",
        "reason": "The learner applies a framework to a practical task."
    },

    {
        "text": "Examine a lesson plan and identify where alignment breaks down.",
        "answer": "Analyze",
        "reason": "The learner examines relationships among different components."
    },

    {
        "text": "Critique an AI-generated lesson plan using OBE principles.",
        "answer": "Evaluate",
        "reason": "Critiquing requires judgement against established criteria."
    },

    {
        "text": "Develop an assessment task aligned with the given CLO.",
        "answer": "Create",
        "reason": "The learner constructs a new assessment."
    }
]


# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------

if "card" not in st.session_state:
    st.session_state.card = random.choice(cards)

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 0


# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.markdown(
    '<div class="title">🔐 CRACK THE OBE CODE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">You have ONE card. Find where it belongs!</div>',
    unsafe_allow_html=True
)

st.info(
    "🎯 Read your card → Choose its Bloom's station → "
    "Lock your answer → Be ready to defend your choice!"
)


# ------------------------------------------------
# CARD
# ------------------------------------------------

st.markdown("### 🃏 YOUR CARD")

st.markdown(
    f"""
    <div class="card">
    {st.session_state.card["text"]}
    </div>
    """,
    unsafe_allow_html=True
)


# ------------------------------------------------
# STATIONS
# ------------------------------------------------

st.markdown("## 🚉 Choose Your Station")

col1, col2, col3 = st.columns(3)

with col1:
    remember = st.button(
        "🧠 REMEMBER",
        use_container_width=True
    )

with col2:
    understand = st.button(
        "💡 UNDERSTAND",
        use_container_width=True
    )

with col3:
    apply = st.button(
        "⚙️ APPLY",
        use_container_width=True
    )


col4, col5, col6 = st.columns(3)

with col4:
    analyze = st.button(
        "🔎 ANALYZE",
        use_container_width=True
    )

with col5:
    evaluate = st.button(
        "📋 EVALUATE",
        use_container_width=True
    )

with col6:
    create = st.button(
        "🎨 CREATE",
        use_container_width=True
    )


# ------------------------------------------------
# CAPTURE CHOICE
# ------------------------------------------------

choice = None

if remember:
    choice = "Remember"

elif understand:
    choice = "Understand"

elif apply:
    choice = "Apply"

elif analyze:
    choice = "Analyze"

elif evaluate:
    choice = "Evaluate"

elif create:
    choice = "Create"


# ------------------------------------------------
# RESULT
# ------------------------------------------------

if choice:

    correct = st.session_state.card["answer"]

    st.session_state.attempts += 1

    if choice == correct:

        st.session_state.score += 1

        st.success(
            f"🔓 CODE CRACKED! Your station is **{correct.upper()}**."
        )

        st.balloons()

    else:

        st.error(
            f"🚨 OBE ALARM! You chose **{choice.upper()}**."
        )

        st.warning(
            f"Your card actually belongs at the "
            f"**{correct.upper()}** station."
        )


    st.markdown("### 🧠 Why?")

    st.info(
        st.session_state.card["reason"]
    )


    # DEFEND YOUR CHOICE
    st.markdown("---")

    st.markdown("## 🎤 DEFEND YOUR CHOICE!")

    st.markdown(
        """
        Imagine someone at another station disagrees with you.

        **You have 20 seconds to justify your decision.**

        Use this sentence:

        > **“I placed this card at ______ because the learner has to ______.”**
        """
    )


    # FUNNY MESSAGE
    if choice == correct:

        funny_messages = [
            "😎 Bloom would approve.",
            "🏆 The OBE Committee is impressed.",
            "🔐 One code successfully cracked!",
            "🎓 Academic credibility preserved.",
            "🚨 No OBE crimes detected here."
        ]

        st.success(random.choice(funny_messages))

    else:

        funny_messages = [
            "😂 Bloom's Taxonomy would like a meeting.",
            "🚑 Please send constructive alignment immediately.",
            "👀 The OBE Committee saw that.",
            "😅 Your card may have boarded the wrong train.",
            "🚨 Alignment Police have been notified."
        ]

        st.warning(random.choice(funny_messages))


# ------------------------------------------------
# NEW CARD
# ------------------------------------------------

st.markdown("---")

if st.button(
    "🎲 GIVE ME ANOTHER CARD",
    use_container_width=True
):

    current = st.session_state.card

    new_card = random.choice(cards)

    while new_card == current and len(cards) > 1:
        new_card = random.choice(cards)

    st.session_state.card = new_card
    st.rerun()


# ------------------------------------------------
# SCORE
# ------------------------------------------------

st.markdown("---")

st.markdown("### 🏆 Your OBE Score")

st.metric(
    "Codes Cracked",
    f"{st.session_state.score} / {st.session_state.attempts}"
    if st.session_state.attempts
    else "0"
)


# ------------------------------------------------
# TRANSITION TO LESSON PLANNING
# ------------------------------------------------

st.markdown("---")

st.markdown("""
## 🎯 You just made an OBE decision.

You matched an **observable action** with a **level of learning**.

But a lesson contains much more than one action.

### 🤔 So what happens when we have to align...

**CLO → Teaching Activity → Assessment?**

That's where lesson planning gets interesting.
""")

st.success(
    "🚀 Next Challenge: Can AI help us build an entire OBE-aligned lesson?"
)
