import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="OBE Review Board",
    page_icon="⚖️",
    layout="centered"
)

# ---------------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 900;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    font-size: 21px;
    font-weight: 600;
    margin-bottom: 25px;
}

.case-title {
    font-size: 28px;
    font-weight: 800;
    margin-top: 10px;
}

.case-box {
    background-color: #f8f9fa;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #ddd;
    margin-bottom: 18px;
}

.audit-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #fff8e1;
    border-left: 6px solid #f0ad4e;
}

.final-box {
    padding: 24px;
    border-radius: 18px;
    border: 2px solid #ddd;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CASE DATA
# ---------------------------------------------------------

cases = [

    {
        "discipline": "🇵🇰 Pakistan Studies",
        "title": "The Analysis That Became Recall",
        "clo": "Analyze the political and socio-economic factors contributing to the creation of Pakistan.",
        "teaching": """
- Examination of political speeches  
- Constitutional developments  
- Historical documents  
- Economic indicators from British India
""",
        "assessment": """
**Question:** Explain five major factors that led to the creation of Pakistan.  
**Marks:** 20
""",
        "rubric": """
- Identification of factors — 8 marks  
- Factual accuracy — 6 marks  
- Organization — 3 marks  
- Language — 3 marks
""",
        "correct": "🔴 RETURN FOR REDESIGN",
        "issue": "Cognitive Demand / Evidence",
        "explanation": """
The CLO requires students to **analyze relationships among political and socio-economic factors**.

However, the assessment mainly rewards:

**identification + explanation + factual recall**

There is little evidence that students must examine relationships, causes, interactions, or relative significance.
""",
        "diagnostic": "cognitive"
    },

    {
        "discipline": "🧠 Psychology",
        "title": "A Case That Actually Works",
        "clo": "Evaluate the effectiveness of different therapeutic approaches for managing anxiety disorders.",
        "teaching": """
- Examination of CBT, psychodynamic and humanistic approaches  
- Review of relevant research findings  
- Discussion of clinical cases
""",
        "assessment": """
Students compare **CBT and psychodynamic therapy** and recommend the more appropriate intervention for a provided case, supporting their recommendation with research evidence.
""",
        "rubric": """
- Comparison of approaches — 25%  
- Evaluation of evidence — 30%  
- Application to case — 25%  
- Justification — 20%
""",
        "correct": "🟢 APPROVE",
        "issue": "No significant alignment problem",
        "explanation": """
The CLO, teaching activity, assessment task, and rubric all provide evidence of **evaluation**.

Students must compare alternatives, use research evidence, apply the approaches to a case, and justify their judgement.
""",
        "diagnostic": "evidence"
    },

    {
        "discipline": "📜 History",
        "title": "The Verb-Matching Trap",
        "clo": "Analyze how political, economic and social factors influenced the French Revolution.",
        "teaching": """
Students examine:

- Primary historical documents  
- Economic records  
- Political writings  
- Accounts from different social groups
""",
        "assessment": """
**Analyze the political causes of the French Revolution using two provided historical documents.**
""",
        "rubric": """
- Analysis — 40%  
- Evidence — 30%  
- Argument — 20%  
- Academic writing — 10%
""",
        "correct": "🟡 APPROVE WITH REVISION",
        "issue": "Construct Coverage",
        "explanation": """
The Bloom's verb appears to align:

**Analyze → Analyze**

But the CLO includes:

**political + economic + social factors**

The assessment measures **political factors only**.

The verb aligns, but the **full construct is not covered**.
""",
        "diagnostic": "construct"
    },

    {
        "discipline": "📚 English",
        "title": "The Rubric Trap",
        "clo": "Critically evaluate how language constructs gender identities in literary texts.",
        "teaching": """
Students examine:

- Characterization  
- Lexical choices  
- Dialogue  
- Narrative perspective  
- Representation of gender
""",
        "assessment": """
Write a **1,500-word critical analysis** examining the construction of gender identity in one selected literary text.
""",
        "rubric": """
- Grammar and language — 30%  
- Organization — 25%  
- Referencing — 20%  
- Presentation — 15%  
- Critical analysis — 10%
""",
        "correct": "🔴 RETURN FOR REDESIGN",
        "issue": "Rubric–CLO Misalignment",
        "explanation": """
The assessment **task** appears aligned.

However, only **10% of the marks** actually measure critical analysis.

Most marks reward language, organization, referencing and presentation.

Therefore, the rubric provides weak evidence of attainment of the stated CLO.
""",
        "diagnostic": "rubric"
    },

    {
        "discipline": "👥 Social Sciences",
        "title": "The Attainment Evidence Trap",
        "clo": "Evaluate the impact of social media on political participation among young adults.",
        "teaching": """
Students examine:

- Empirical studies  
- Survey findings  
- Competing theoretical perspectives  
- Social-media participation data
""",
        "assessment": """
Students analyze provided data and write a report evaluating whether social media increases meaningful political participation.
""",
        "rubric": """
The department calculates CLO attainment using a:

**10-mark MCQ quiz**

covering definitions of:

- political participation  
- social media engagement  
- civic participation
""",
        "correct": "🔴 RETURN FOR REDESIGN",
        "issue": "Attainment Evidence",
        "explanation": """
The course contains an appropriate assessment task.

However, the **instrument used to calculate CLO attainment** measures definitions and recall rather than evaluation.

Therefore, the reported CLO attainment is not defensible from this evidence.
""",
        "diagnostic": "attainment"
    }
]

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "case_index" not in st.session_state:
    st.session_state.case_index = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "answers" not in st.session_state:
    st.session_state.answers = []

if "reason_answers" not in st.session_state:
    st.session_state.reason_answers = []

if "confidence" not in st.session_state:
    st.session_state.confidence = []

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">⚖️ THE OBE REVIEW BOARD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Would YOU approve this course?</div>',
    unsafe_allow_html=True
)

st.info("""
You have been appointed to an **Academic Review Board**.

You will review course-design evidence from different disciplines.

Your task is **not simply to match Bloom's verbs**.

Your task is to decide whether the evidence genuinely demonstrates the CLO.
""")

# ---------------------------------------------------------
# PROGRESS
# ---------------------------------------------------------

total_cases = len(cases)
current_index = st.session_state.case_index

if current_index < total_cases:

    progress = current_index / total_cases
    st.progress(progress)

    st.caption(f"Course File {current_index + 1} of {total_cases}")

    case = cases[current_index]

    # -----------------------------------------------------
    # CASE DISPLAY
    # -----------------------------------------------------

    st.markdown(
        f'<div class="case-title">{case["discipline"]}</div>',
        unsafe_allow_html=True
    )

    st.subheader(case["title"])

    st.markdown("### 🎯 Course Learning Outcome")

    st.info(case["clo"])

    st.markdown("### 👩‍🏫 Teaching & Learning Evidence")

    st.markdown(case["teaching"])

    st.markdown("### 📝 Assessment Evidence")

    st.markdown(case["assessment"])

    with st.expander("📋 View Rubric / Attainment Evidence"):
        st.markdown(case["rubric"])

    st.markdown("---")

    # -----------------------------------------------------
    # BOARD DECISION
    # -----------------------------------------------------

    st.markdown("## ⚖️ Your Board Decision")

    decision = st.radio(
        "Would you approve this alignment?",
        [
            "🟢 APPROVE",
            "🟡 APPROVE WITH REVISION",
            "🔴 RETURN FOR REDESIGN"
        ],
        index=None,
        key=f"decision_{current_index}"
    )

    # -----------------------------------------------------
    # REASON
    # -----------------------------------------------------

    st.markdown("### 🔍 What most influenced your decision?")

    reason = st.radio(
        "Choose the strongest issue:",
        [
            "Cognitive level",
            "Construct coverage",
            "Teaching–CLO alignment",
            "Assessment–CLO alignment",
            "Rubric–CLO alignment",
            "Attainment evidence",
            "No significant alignment problem"
        ],
        index=None,
        key=f"reason_{current_index}"
    )

    # -----------------------------------------------------
    # CONFIDENCE
    # -----------------------------------------------------

    confidence = st.slider(
        "How confident are you in your decision?",
        min_value=1,
        max_value=5,
        value=3,
        help="1 = Not confident | 5 = Very confident"
    )

    # -----------------------------------------------------
    # SUBMIT
    # -----------------------------------------------------

    if not st.session_state.answered:

        if st.button(
            "🔒 LOCK BOARD DECISION",
            use_container_width=True
        ):

            if decision is None or reason is None:
                st.warning("Please make both a board decision and select your main reason.")

            else:

                st.session_state.answers.append(decision)
                st.session_state.reason_answers.append(reason)
                st.session_state.confidence.append(confidence)

                st.session_state.answered = True
                st.rerun()

    # -----------------------------------------------------
    # REVEAL
    # -----------------------------------------------------

    if st.session_state.answered:

        user_decision = st.session_state.answers[-1]

        st.markdown("---")

        st.markdown("## 📋 QEC AUDIT FINDING")

        if user_decision == case["correct"]:
            st.success("✅ Your Board decision is defensible.")

        else:
            st.warning("⚠️ Your decision differs from the reference review.")

        st.markdown(
            f"""
### Recommended Decision

**{case["correct"]}**

### Primary Issue

**{case["issue"]}**
"""
        )

        st.markdown(
            f"""
<div class="audit-box">
{case["explanation"]}
</div>
""",
            unsafe_allow_html=True
        )

        # -------------------------------------------------
        # KEY TAKEAWAY
        # -------------------------------------------------

        if case["diagnostic"] == "cognitive":

            st.info("""
### Key Principle

**Topic relevance does not guarantee cognitive alignment.**

Ask:

> What must students actually DO to demonstrate the CLO?
""")

        elif case["diagnostic"] == "construct":

            st.info("""
### Key Principle

**Verb alignment ≠ construct alignment.**

A matching Bloom's verb may still assess only part of the outcome.
""")

        elif case["diagnostic"] == "rubric":

            st.info("""
### Key Principle

**An aligned assessment task can still have a misaligned rubric.**

Ask:

> What actually receives marks?
""")

        elif case["diagnostic"] == "attainment":

            st.info("""
### Key Principle

**Course assessment and CLO-attainment evidence are not automatically the same thing.**

Ask:

> Which evidence is actually being used to claim attainment?
""")

        elif case["diagnostic"] == "evidence":

            st.info("""
### Key Principle

Good OBE alignment means that the:

**CLO → Learning Experience → Assessment → Rubric → Evidence**

tell the same story.
""")

        # -------------------------------------------------
        # NEXT CASE
        # -------------------------------------------------

        if st.button(
            "➡️ OPEN NEXT COURSE FILE",
            use_container_width=True
        ):
            st.session_state.case_index += 1
            st.session_state.answered = False
            st.rerun()

# =========================================================
# FINAL RESULTS
# =========================================================

else:

    st.progress(1.0)

    st.markdown("# 🏆 BOARD REVIEW COMPLETE")

    correct_count = 0

    for i, answer in enumerate(st.session_state.answers):
        if answer == cases[i]["correct"]:
            correct_count += 1

    percentage = round(
        correct_count / len(cases) * 100
    )

    st.metric(
        "Defensible Board Decisions",
        f"{correct_count} / {len(cases)}"
    )

    st.metric(
        "Review Accuracy",
        f"{percentage}%"
    )

    # -----------------------------------------------------
    # DIAGNOSTIC PROFILE
    # -----------------------------------------------------

    selected_reasons = st.session_state.reason_answers

    rubric_count = selected_reasons.count("Rubric–CLO alignment")
    construct_count = selected_reasons.count("Construct coverage")
    attainment_count = selected_reasons.count("Attainment evidence")
    cognitive_count = selected_reasons.count("Cognitive level")

    st.markdown("---")

    st.markdown("## 🔎 Your OBE Reviewer Profile")

    if correct_count == 5:

        st.success("""
### 🏆 THE OBE AUDITOR

You consistently looked beyond surface-level verb matching and examined whether the assessment evidence genuinely demonstrated the CLO.
""")

    elif rubric_count >= 2:

        st.info("""
### 📋 THE RUBRIC AUDITOR

You pay close attention to what actually receives marks.

Your instinct is:

**“Does the rubric measure what the CLO claims?”**
""")

    elif construct_count >= 2:

        st.info("""
### 🎯 THE CONSTRUCT CHECKER

You frequently examine whether the full scope of the CLO is actually represented in assessment.
""")

    elif attainment_count >= 2:

        st.info("""
### 🔎 THE EVIDENCE HUNTER

Your strongest reviewing instinct is:

**“What evidence actually proves that students attained this outcome?”**
""")

    elif cognitive_count >= 2:

        st.info("""
### 🧠 THE COGNITIVE ALIGNMENT CHECKER

You pay particular attention to whether assessment tasks genuinely operate at the cognitive level demanded by the CLO.
""")

    else:

        st.info("""
### ⚖️ THE BALANCED REVIEWER

You considered several dimensions of OBE alignment rather than relying on a single indicator.
""")

    # -----------------------------------------------------
    # CONFIDENCE
    # -----------------------------------------------------

    avg_confidence = sum(
        st.session_state.confidence
    ) / len(st.session_state.confidence)

    st.metric(
        "Average Review Confidence",
        f"{avg_confidence:.1f} / 5"
    )

    # -----------------------------------------------------
    # FINAL MESSAGE
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown("""
# 🔐 THE OBE CODE

OBE alignment is **not simply:**

### Evaluate = Evaluate

A defensible OBE lesson asks whether the following chain is coherent:

## 🎯 CLO
### ↓
## 👩‍🏫 Learning Experience
### ↓
## 📝 Assessment
### ↓
## 📋 Rubric
### ↓
## 📊 Evidence of Attainment
""")

    st.success("""
### If one link breaks, the reported CLO attainment may become difficult to defend.
""")

    st.markdown("---")

    st.markdown("""
## 🤖 And now comes the AI question...

AI can generate a lesson plan in seconds.

But can it ensure that:

- the **CLO is measurable**,
- the **learning activity prepares students for it**,
- the **assessment generates the right evidence**,
- and the **rubric actually measures attainment**?

### That's the challenge of AI-assisted OBE lesson planning.
""")

    st.success(
        "🚀 Let's test it with the OBE Lesson Planner."
    )

    # -----------------------------------------------------
    # RESTART
    # -----------------------------------------------------

    st.markdown("---")

    if st.button(
        "🔄 START A NEW BOARD REVIEW",
        use_container_width=True
    ):
        st.session_state.clear()
        st.rerun()
