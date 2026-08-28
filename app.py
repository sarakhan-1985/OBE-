import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Fire the Lesson! 🔥",
    page_icon="🔥",
    layout="centered"
)

# --------------------------------------------------
# SIMPLE STYLING
# --------------------------------------------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    margin-bottom: 25px;
}

.case-box {
    padding: 22px;
    border-radius: 18px;
    border: 2px solid #ddd;
    margin-bottom: 20px;
}

.big-text {
    font-size: 22px;
    font-weight: 700;
}

.center {
    text-align: center;
}

.small-note {
    text-align: center;
    font-size: 14px;
    opacity: 0.75;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "case" not in st.session_state:
    st.session_state.case = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False


def next_case():
    st.session_state.case += 1
    st.session_state.answered = False


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🔥 FIRE THE LESSON!</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">The slightly dangerous OBE Icebreaker 😄</div>',
    unsafe_allow_html=True
)

st.info(
    "🚨 You are now the **OBE Committee**. "
    "Some very questionable lesson plans have arrived. "
    "Your job is to decide whether they survive!"
)

progress = (st.session_state.case - 1) / 4
st.progress(progress)

st.caption(f"Case {min(st.session_state.case,4)} of 4")


# ==================================================
# CASE 1
# ==================================================

if st.session_state.case == 1:

    st.header("🏊 Case 1: The Swimming Professor")

    st.markdown("""
### 🎯 CLO
Students will be able to **swim 50 metres**.

### 👨‍🏫 Teaching
The teacher delivers a PowerPoint:

> **10 Important Principles of Swimming**

### 📚 Student Activity
Students read:

> *Chapter 3: How to Swim*

### 📝 Assessment

**Define swimming. [10 marks]**
""")

    st.subheader("⚖️ OBE Verdict")

    choice = st.radio(
        "What should happen to this lesson?",
        [
            "🟢 APPROVE IT!",
            "🟡 MAYBE... LET'S DISCUSS",
            "🔴 FIRE THE LESSON! 🔥"
        ],
        index=None,
        key="case1"
    )

    if choice and not st.session_state.answered:

        if choice == "🔴 FIRE THE LESSON! 🔥":
            st.success("✅ CORRECT! The lesson has officially been fired. 🔥")
            st.session_state.score += 1
        else:
            st.error("🚨 OBE Police would like a word with you.")

        st.session_state.answered = True

    if st.session_state.answered:

        st.markdown("---")

        st.error("""
### 🚨 OBE POLICE REPORT

**CLO:** SWIM 🏊  
**Teaching:** LISTEN 👂  
**Activity:** READ 📖  
**Assessment:** DEFINE ✍️  

### ❌ Nobody actually swims!
""")

        st.info(
            "💡 If students are expected to **DO** something, "
            "teaching and assessment must give them the opportunity to **DO it**."
        )

        if st.button("➡️ Next Case", use_container_width=True):
            next_case()
            st.rerun()


# ==================================================
# CASE 2
# ==================================================

elif st.session_state.case == 2:

    st.header("🎂 Case 2: MasterChef University")

    st.markdown("""
### 🎯 CLO
Students will be able to **prepare a cake**.

### 👩‍🏫 Teaching
The teacher explains:

> **The History of Cake: 1850–2026**

### 📺 Activity
Students watch a cake-making video.

### 📝 Assessment

**List five ingredients used in cake.**
""")

    st.subheader("👨‍🍳 Your Verdict?")

    choice = st.radio(
        "Choose wisely...",
        [
            "🌟 MICHELIN STAR!",
            "🟡 NEEDS MORE BAKING",
            "🔥 GET OUT OF MY KITCHEN!"
        ],
        index=None,
        key="case2"
    )

    if choice and not st.session_state.answered:

        if choice == "🔥 GET OUT OF MY KITCHEN!":
            st.success("😂 Gordon Ramsay would be proud.")
            st.session_state.score += 1
        else:
            st.warning("🤔 The cake may be delicious... but the OBE isn't.")

        st.session_state.answered = True

    if st.session_state.answered:

        st.markdown("---")

        st.warning("""
### THE PROBLEM

🎯 **CLO:** PREPARE  

📺 **Activity:** WATCH  

📝 **Assessment:** LIST  

### PREPARE ≠ LIST
""")

        st.success("""
A better assessment would be:

> **Prepare a cake following the given criteria and justify your choice of ingredients.**
""")

        if st.button("➡️ Next Case", use_container_width=True):
            next_case()
            st.rerun()


# ==================================================
# CASE 3
# ==================================================

elif st.session_state.case == 3:

    st.header("🎤 Case 3: The PowerPoint Professor")

    st.markdown("""
### 🎯 CLO
Students will be able to **create a persuasive presentation**.

### 👩‍🏫 Teaching
Teacher gives a **50-minute lecture** about presentations.

### 👀 Activity
Students watch the teacher's PowerPoint.

### 📝 Assessment
Students:

> **Define persuasive presentation.**
""")

    st.subheader("⚖️ What happens now?")

    choice = st.radio(
        "OBE Committee decision:",
        [
            "🟢 PERFECTLY ALIGNED",
            "🟡 OBE-ish",
            "🔴 THIS LESSON NEEDS HELP 🚑"
        ],
        index=None,
        key="case3"
    )

    if choice and not st.session_state.answered:

        if choice == "🔴 THIS LESSON NEEDS HELP 🚑":
            st.success("✅ Correct. Please call the Alignment Ambulance. 🚑")
            st.session_state.score += 1
        else:
            st.error("😬 The OBE Committee has concerns.")

        st.session_state.answered = True

    if st.session_state.answered:

        st.markdown("---")

        st.error("""
### ALIGNMENT EMERGENCY 🚨

**CREATE** a presentation  
↓  

Teacher asks students to...

**WATCH + DEFINE**

### ❌ CREATE ≠ DEFINE
""")

        st.info("""
A better activity might require students to:

**Design → Present → Receive Feedback → Revise**
""")

        if st.button("➡️ Final Boss", use_container_width=True):
            next_case()
            st.rerun()


# ==================================================
# CASE 4
# ==================================================

elif st.session_state.case == 4:

    st.header("👑 FINAL BOSS: Applied Linguistics")

    st.markdown("""
Okay. No more swimming. No more cake.

Now let's make it academic. 😎

---

### 🎯 CLO

Students will be able to:

**Evaluate the effectiveness of corrective feedback strategies in ESL classrooms.**

### 👩‍🏫 Teaching

Teacher explains different corrective feedback strategies.

### 👥 Activity

Students compare two classroom scenarios.

### 📝 Assessment

Students are asked to:

> **List five types of corrective feedback.**
""")

    st.subheader("🚨 OBE Crime Detected?")

    choice = st.radio(
        "What is your verdict?",
        [
            "🟢 Completely aligned",
            "🟡 Slightly suspicious",
            "🔴 OBE CRIME DETECTED 🚨"
        ],
        index=None,
        key="case4"
    )

    if choice and not st.session_state.answered:

        if choice == "🔴 OBE CRIME DETECTED 🚨":
            st.success("🚨 Correct! You caught the alignment criminal.")
            st.session_state.score += 1
        else:
            st.warning("🔍 Look closely at the CLO verb.")

        st.session_state.answered = True

    if st.session_state.answered:

        st.markdown("---")

        st.error("""
### THE CLUE WAS THE VERB 🔍

CLO asks students to:

# **EVALUATE**

Assessment asks students to:

# **LIST**

### Evaluate ≠ List
""")

        st.subheader("🛠️ Can you repair it?")

        repair = st.radio(
            "Which assessment actually matches the CLO?",
            [
                "A. Define corrective feedback.",
                "B. List five corrective feedback strategies.",
                "C. Evaluate which feedback strategy is more effective in the two scenarios and justify your decision."
            ],
            index=None,
            key="repair"
        )

        if repair:

            if repair.startswith("C."):

                st.balloons()

                st.success("""
# 🎉 ALIGNMENT RESTORED!

### EVALUATE → EVALUATE + JUSTIFY ✅
""")

                st.markdown("---")

                st.markdown("## 🏆 Your OBE Committee Result")

                score = st.session_state.score

                if score == 4:
                    st.success("""
### 👑 OBE LEGEND

You successfully fired every bad lesson.

The OBE Committee is impressed.
""")

                elif score >= 2:
                    st.info("""
### 🔎 OBE DETECTIVE

Your alignment instincts are working!
""")

                else:
                    st.warning("""
### 🛠️ ALIGNMENT APPRENTICE

There is still hope. 😄
""")

                st.markdown("---")

                st.markdown("""
## 🤔 But here's the real question...

You just **identified** bad alignment.

You even **repaired** it.

### But can we DESIGN alignment correctly from the beginning?

And can **AI help us do it?**
""")

                st.success("""
# 🚀 LET'S FIND OUT...

### Welcome to the AI-Assisted OBE Lesson Planner
""")

                st.caption(
                    "Certification valid for approximately 30 seconds. 😂"
                )

            else:

                st.error("""
🚨 Nope!

Look at the CLO again:

**EVALUATE**

Your assessment must allow students to demonstrate **evaluation**.
""")


# ==================================================
# RESET
# ==================================================

st.markdown("---")

if st.button("🔄 Restart Game"):
    st.session_state.clear()
    st.rerun()

st.markdown(
    '<div class="small-note">🔥 Fire the Lesson! — OBE Icebreaker</div>',
    unsafe_allow_html=True
)
