import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/classify"

st.set_page_config(
    page_title="SMS Fraud Detection",
    layout="centered",
)

# Custom CSS for styling (will be applied globally across the frontend)
# Streamlit's default styling is quite plain so we override it here
# unsafe_allow_html=True is required any time we pass raw HTML or CSS to streamlit
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
        }

        .stApp {
            background-color: #faf9f6;
        }

        .block-container {
            max-width: 680px !important;
            padding-top: 0 !important;
        }

        /* ── hero ── */
        .hero {
            padding: 4rem 0 3rem 0;
            text-align: center;
        }
        .hero-eyebrow {
            font-family: 'DM Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: #b0a89a;
            margin-bottom: 1.2rem;
        }
        .hero-title {
            font-family: 'DM Serif Display', serif;
            font-size: 3rem;
            font-weight: 400;
            color: #1c1915;
            line-height: 1.1;
            margin: 0 0 0.4rem 0;
        }
        .hero-title em {
            font-style: italic;
            color: #8a7d6b;
        }
        .hero-sub {
            font-size: 0.85rem;
            color: #9e9485;
            font-weight: 300;
            margin-top: 0.8rem;
            line-height: 1.6;
        }

        /* ── divider ── */
        .rule {
            border: none;
            border-top: 1px solid #e8e3db;
            margin: 0 0 2.2rem 0;
        }

        /* ── textarea ── */
        .stTextArea textarea {
            background-color: #ffffff !important;
            color: #1c1915 !important;
            border: 1px solid #ddd8cf !important;
            border-radius: 2px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.92rem !important;
            font-weight: 300 !important;
            line-height: 1.7 !important;
            padding: 1rem 1.1rem !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
            transition: border-color 0.2s, box-shadow 0.2s !important;
            resize: none !important;
        }
        .stTextArea textarea:focus {
            border-color: #1c1915 !important;
            box-shadow: 0 0 0 3px rgba(28,25,21,0.06) !important;
        }
        .stTextArea textarea::placeholder {
            color: #c5bdb2 !important;
        }

        /* ── button ── */
        .stButton > button {
            background-color: #1c1915 !important;
            color: #faf9f6 !important;
            border: none !important;
            border-radius: 2px !important;
            font-family: 'DM Mono', monospace !important;
            font-size: 0.7rem !important;
            font-weight: 500 !important;
            letter-spacing: 0.14em !important;
            text-transform: uppercase !important;
            padding: 0.75rem 2.5rem !important;
            height: auto !important;
            line-height: 1.2 !important;
            width: 100% !important;
            transition: background-color 0.15s, transform 0.1s !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.12) !important;
        }
        .stButton > button:hover {
            background-color: #332e28 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 3px 8px rgba(0,0,0,0.14) !important;
        }
        .stButton > button:active {
            transform: translateY(0) !important;
        }

        /* ── result ── */
        .result-wrap {
            margin-top: 1.8rem;
            animation: fadeUp 0.35s ease;
        }
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(8px); }
            to   { opacity: 1; transform: translateY(0);   }
        }

        .result-tag {
            font-family: 'DM Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }
        .tag-spam { color: #c0392b; }
        .tag-ham  { color: #27ae60; }

        .result-headline {
            font-family: 'DM Serif Display', serif;
            font-size: 2rem;
            font-weight: 400;
            line-height: 1.1;
        }
        .headline-spam { color: #c0392b; }
        .headline-ham  { color: #27ae60; }

        .result-body {
            font-size: 0.82rem;
            color: #9e9485;
            font-weight: 300;
            margin-top: 0.35rem;
            line-height: 1.5;
        }

        .confidence-row {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-top: 1.1rem;
        }
        .confidence-track {
            flex: 1;
            height: 2px;
            background: #e8e3db;
            border-radius: 1px;
            overflow: hidden;
        }
        .confidence-fill-spam { height: 2px; background: #c0392b; border-radius: 1px; }
        .confidence-fill-ham  { height: 2px; background: #27ae60; border-radius: 1px; }
        .confidence-num {
            font-family: 'DM Mono', monospace;
            font-size: 0.72rem;
            color: #b0a89a;
            white-space: nowrap;
        }

        .result-rule {
            border: none;
            border-top: 1px solid #e8e3db;
            margin: 1.4rem 0 0 0;
        }

        /* ── error ── */
        .err {
            margin-top: 1.4rem;
            padding: 1rem 1.2rem;
            border-left: 2px solid #e0b050;
            background: #fffdf5;
            font-size: 0.8rem;
            color: #7a6020;
            line-height: 1.65;
            font-weight: 300;
        }
        .err code {
            font-family: 'DM Mono', monospace;
            font-size: 0.75rem;
            background: #fef9e7;
            padding: 0.1rem 0.35rem;
            border-radius: 2px;
        }

        /* ── about ── */
        .about {
            margin-top: 3.5rem;
            padding-top: 2rem;
            border-top: 1px solid #e8e3db;
        }
        .about-eyebrow {
            font-family: 'DM Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: #c5bdb2;
            margin-bottom: 1.4rem;
        }
        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem 2.5rem;
        }
        .about-item-title {
            font-family: 'DM Serif Display', serif;
            font-size: 0.95rem;
            color: #1c1915;
            margin-bottom: 0.3rem;
        }
        .about-item-body {
            font-size: 0.78rem;
            color: #9e9485;
            font-weight: 300;
            line-height: 1.6;
        }
        .about-item-body strong {
            color: #5a5248;
            font-weight: 400;
        }

        /* ── footer ── */
        .footer {
            margin-top: 3rem;
            padding-bottom: 2rem;
            text-align: center;
            font-family: 'DM Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.1em;
            color: #d4cfc8;
            text-transform: uppercase;
            line-height: 2;
        }

        /* hide streamlit chrome */
        #MainMenu, footer, header { visibility: hidden; }
    </style>
""",
    unsafe_allow_html=True,
)

# === hero ===
st.markdown(
    """
    <div class="hero">
        <div class="hero-eyebrow">RTU · HPC Challenge 2026</div>
        <div class="hero-title">SMS Fraud<br><em>Detection</em></div>
        <div class="hero-sub">
            Paste any SMS message below, and the model will analyze it <br>
            to determine whether it appears to be spam and provide a <br>
            confidence level for its assessment.
        </div>
    </div>
    <hr class="rule"/>
""",
    unsafe_allow_html=True,
)


# === input ===
message = st.text_area(
    "message",
    placeholder="Type or paste an SMS message here…",
    height=130,
    label_visibility="collapsed",
)

st.markdown("<div style='height:0.7rem'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 1, 1.2])
with col2:
    classify = st.button("Analyse", use_container_width=True)

# === result ===
# this block only runs when the user clicks "Analyse"
if classify:
    if not message.strip():
        st.markdown(
            '<div class="err">Please enter a message before analysing.</div>',
            unsafe_allow_html=True,
        )
    elif len(message.strip()) < 10:
        st.markdown(
            '<div class="err">Message is too short for a reliable analysis.</div>',
            unsafe_allow_html=True,
        )
    else:
        try:
            with st.spinner("Analysing message patterns..."):
                response = requests.post(API_URL, json={"message": message}, timeout=10)
            response.raise_for_status()
            data = response.json()

            # extract the prediction and confidence from the API response
            prediction = data["prediction"]
            confidence = data["confidence"]
            is_spam = prediction == "spam"

            # based on whether it's spam or ham, set different text and styles for the result display
            tag = "Spam" if is_spam else "Ham"
            headline = "This looks like spam." if is_spam else "Looks legitimate."
            body = (
                "Our model flagged this message as likely fraudulent."
                if is_spam
                else "No significant fraud signals detected in this message."
            )
            tag_cls = "tag-spam" if is_spam else "tag-ham"
            h_cls = "headline-spam" if is_spam else "headline-ham"
            fill_cls = "confidence-fill-spam" if is_spam else "confidence-fill-ham"

            st.markdown(
                f"""
                <div class="result-wrap">
                    <div class="result-tag {tag_cls}">{tag}</div>
                    <div class="result-headline {h_cls}">{headline}</div>
                    <div class="result-body">{body}</div>
                    <div class="confidence-row">
                        <div class="confidence-track">
                            <div class="{fill_cls}" style="width:{confidence}%"></div>
                        </div>
                        <div class="confidence-num">{confidence}% confidence</div>
                    </div>
                    <hr class="result-rule"/>
                </div>
            """,
                unsafe_allow_html=True,
            )

        except requests.exceptions.ConnectionError:
            # This error occurs when the frontend cannot connect to the API server, likely because it's not running.
            st.markdown(
                """
                <div class="err">
                    Cannot reach the API! Please make sure the server is running:<br/><br/>
                    <code>uvicorn src.api:app --reload</code>
                </div>
            """,
                unsafe_allow_html=True,
            )
        except requests.exceptions.Timeout:
            # This error occurs when the API server takes too long to respond, which could indicate it's overloaded or there's a network issue.
            st.markdown(
                '<div class="err">Request timed out. The server might be overloaded.</div>',
                unsafe_allow_html=True,
            )
        except Exception as e:
            # Catch any other unexpected errors and display a generic error message.
            st.markdown(
                f'<div class="err">Unexpected error: {e}</div>',
                unsafe_allow_html=True,
            )

# === about ===
# This is the HTML that the CSS is applying to.
# static info section at the bottom: four cards in a 2x2 grid
st.markdown(
    """
    <div class="about">
        <div class="about-eyebrow">About this project</div>
        <div class="about-grid">
            <div>
                <div class="about-item-title">What it does</div>
                <div class="about-item-body">
                    Classifies SMS messages as <strong>spam</strong> or <strong>ham</strong> using a model
                    trained on the UCI SMS Spam Collection (~5,500 messages).
                </div>
            </div>
            <div>
                <div class="about-item-title">How it works</div>
                <div class="about-item-body">
                    Messages are vectorised with <strong>TF-IDF</strong>, then classified by the best model
                    found via grid search across Logistic Regression, Naive Bayes, SVM, and Random Forest.
                </div>
            </div>
            <div>
                <div class="about-item-title">The HPC angle</div>
                <div class="about-item-body">
                    Grid search runs <strong>1,000+ model trainings</strong> with 10-fold cross-validation
                    on RTU's RUDENS cluster, compressing hours of compute into minutes.
                </div>
            </div>
            <div>
                <div class="about-item-title">Team</div>
                <div class="about-item-body">
                    <strong>Ayma Rehman · Matthew Harris</strong><br/>
                    <strong>Evelīna Šadurska · Klints Legranžs</strong><br/>
                    In collaboration with Ģirts Bērziņš, Swedbank.
                </div>
            </div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# === footer ===
st.markdown(
    """
    <div class="footer">
        RTU HPC Challenge 2026 <br/>
        Riga Technical University <br/>
        In Collaboration with Swedbank
    </div>
    """,
    unsafe_allow_html=True,
)
