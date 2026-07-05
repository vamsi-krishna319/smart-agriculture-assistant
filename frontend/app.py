import streamlit as st

st.set_page_config(
    page_title="Smart Agriculture Assistant",
    page_icon="🌾",
    layout="wide"
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root{
    --color-bg: #F5F7F0;
    --color-bg-card: #FBFAF5;
    --color-bg-sunken: #ECEFE1;
    --color-primary: #1F3D2B;
    --color-primary-light: #335C42;
    --color-accent: #C9971C;
    --color-accent-soft: #F1E3B4;
    --color-soil: #6B4226;
    --color-sky: #4A7C9E;
    --color-moss: #4F7942;
    --color-rust: #A6412C;
    --color-text: #1A2A1E;
    --color-text-soft: #52604F;
    --font-display: 'Fraunces', serif;
    --font-body: 'IBM Plex Sans', sans-serif;
    --font-mono: 'IBM Plex Mono', monospace;
}

[data-testid="stAppViewContainer"]{ background: var(--color-bg); }
[data-testid="stAppViewContainer"] * { font-family: var(--font-body); color: var(--color-text); }
html, body { font-family: var(--font-body); }

[data-testid="stSidebar"]{ background: var(--color-primary); }
[data-testid="stSidebar"] * { color: #F1EEE1 !important; font-family: var(--font-body); }
[data-testid="stSidebar"] a { color: var(--color-accent) !important; }

h1, h2, h3 { font-family: var(--font-display) !important; color: var(--color-primary) !important; letter-spacing: -0.01em; }
h1 { font-weight: 700 !important; border-bottom: 3px solid var(--color-accent); padding-bottom: 0.35rem; display: inline-block; }
h2 { font-weight: 600 !important; }
h3 { font-weight: 600 !important; font-style: italic; color: var(--color-soil) !important; }

hr {
    border: none !important;
    height: 12px !important;
    margin: 1.75rem 0 !important;
    background: repeating-linear-gradient(90deg, var(--color-soil) 0px, var(--color-soil) 2px, transparent 2px, transparent 13px) !important;
    opacity: 0.30;
    border-radius: 2px;
}

.stButton > button, .stFormSubmitButton > button, .stDownloadButton > button {
    background: var(--color-primary);
    color: #F5F7F0 !important;
    border: none;
    border-radius: 4px;
    font-family: var(--font-body);
    font-weight: 600;
    padding: 0.55rem 1.4rem;
    letter-spacing: 0.02em;
    transition: background 0.15s ease, transform 0.1s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover, .stDownloadButton > button:hover {
    background: var(--color-accent);
    color: var(--color-primary) !important;
    transform: translateY(-1px);
}

[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input, [data-baseweb="select"] > div {
    background: var(--color-bg-card) !important;
    border: 1.5px solid var(--color-bg-sunken) !important;
    border-radius: 4px !important;
    font-family: var(--font-body) !important;
}
[data-testid="stTextInput"] input:focus, [data-testid="stNumberInput"] input:focus {
    border-color: var(--color-accent) !important;
    box-shadow: 0 0 0 1px var(--color-accent) !important;
}

[data-testid="stFileUploaderDropzone"] {
    background: var(--color-bg-card) !important;
    border: 2px dashed var(--color-soil) !important;
    border-radius: 6px !important;
}

[data-testid="stMetric"] { background: var(--color-bg-card); border-left: 4px solid var(--color-soil); border-radius: 4px; padding: 0.85rem 1rem; }
[data-testid="stMetricLabel"] { font-family: var(--font-body) !important; color: var(--color-text-soft) !important; font-size: 0.82rem !important; text-transform: uppercase; letter-spacing: 0.06em; }
[data-testid="stMetricValue"] { font-family: var(--font-mono) !important; color: var(--color-primary) !important; font-weight: 600 !important; }

[data-testid="stAlert"] { border-radius: 4px !important; border-left-width: 4px !important; border-left-style: solid !important; }
div[data-testid="stAlert"]:has(svg[title="Success"]) { border-left-color: var(--color-moss) !important; background: #EBF2E6 !important; }
div[data-testid="stAlert"]:has(svg[title="Info"]) { border-left-color: var(--color-sky) !important; background: #E8F0F4 !important; }
div[data-testid="stAlert"]:has(svg[title="Warning"]) { border-left-color: var(--color-accent) !important; background: #FBF3DF !important; }
div[data-testid="stAlert"]:has(svg[title="Error"]) { border-left-color: var(--color-rust) !important; background: #F7E9E6 !important; }

[data-testid="stJson"] { background: var(--color-bg-sunken) !important; border-radius: 4px; font-family: var(--font-mono) !important; }

.ag-stepper { display: flex; align-items: center; gap: 0.4rem; margin: 0.25rem 0 1.5rem 0; flex-wrap: wrap; }
.ag-step { font-family: var(--font-mono); font-size: 0.8rem; font-weight: 500; padding: 0.3rem 0.85rem; border-radius: 999px; border: 1.5px solid var(--color-primary); color: var(--color-primary); background: transparent; }
.ag-step.active { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-primary); font-weight: 600; }
.ag-step.done { background: var(--color-primary); border-color: var(--color-primary); color: #F5F7F0; }
.ag-step-arrow { color: var(--color-soil); font-size: 0.9rem; opacity: 0.6; }

.ag-card { background: var(--color-bg-card); border-left: 4px solid var(--color-soil); border-radius: 4px; padding: 1.1rem 1.3rem; margin-bottom: 1rem; }
</style>
""",
    unsafe_allow_html=True
)

st.title("🌾 Smart Agriculture Assistant")

st.markdown(
    """
<div class="ag-stepper">
  <span class="ag-step">① Register</span>
  <span class="ag-step-arrow">→</span>
  <span class="ag-step">② Analyze Crop</span>
  <span class="ag-step-arrow">→</span>
  <span class="ag-step">③ Get Report</span>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    """
<div class="ag-card">

Welcome to the AI Powered Smart Agriculture Assistant.

Using this application farmers can:

- 👨‍🌾 Register
- 📷 Upload Crop Images
- 🤖 Detect Crop Diseases
- 🌦 Analyze Weather
- 🌱 Get Fertilizer Suggestions
- 💧 Receive Irrigation Advice
- 📄 Download AI Reports

</div>
""",
    unsafe_allow_html=True
)

st.success(
    "Use the left sidebar to navigate through the application."
)
