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
