import streamlit as st # type: ignore
import pandas as pd
from components.sidebar import sidebar
from components.calendar_view import calendar_view
from components.charts import charts_view
from components.smart_insights import insights_view

from features.add_expense import add_expense
from features.export_data import export_data
from features.budget_alerts import check_budget_alerts
from features.monthly_comparison import show_monthly_comparison
from features.recurring_detector import detect_recurring_expenses
from features.voice_input import voice_to_text_input
from chatbot.bot import chatbot_tab
from utils.helpers import load_data

# Beautiful page configuration
st.set_page_config(
    page_title="Smart Expense Visualizer",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Full dark theme with high-contrast text
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #0b1120; }
    .main .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1200px; background: transparent; }

    /* Sidebar */
    .css-1d391kg { background: #0b1120; }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #0f172a; color: #e5e7eb;
        border-radius: 14px 14px 0 0; font-weight: 700; font-size: 16px; padding: 12px 22px;
        margin: 0 2px; border: 1px solid rgba(255,255,255,0.08); transition: background .2s ease, color .2s ease, box-shadow .2s ease;
    }
    .stTabs [data-baseweb="tab"]:hover { background: #111827; }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(180deg, #6366f1 0%, #8b5cf6 100%);
        color: #ffffff; border: 1px solid rgba(255,255,255,0.15);
        box-shadow: inset 0 -3px 0 #fb7185, 0 6px 18px rgba(99,102,241,0.25);
    }

    /* Tab panel */
    .stTabs [data-baseweb="tab-panel"] {
        background: #0f172a; border-radius: 0 0 12px 12px; padding: 20px; border: 1px solid rgba(255,255,255,0.08); border-top: none;
    }

    /* Header */
    .main-header { background: linear-gradient(135deg, #6d28d9 0%, #7c3aed 50%, #9333ea 100%); padding: 28px; border-radius: 14px; margin-bottom: 24px; text-align: center; color: #ffffff; box-shadow: 0 10px 30px rgba(124,58,237,0.25); }
    .main-header *, .main-header h1, .main-header p { color: #ffffff !important; }
    .main-header h1 { font-size: 2.4em; margin: 0; text-shadow: 0 2px 6px rgba(0,0,0,0.25); }
    .main-header p { font-size: 1.05em; margin: 8px 0 0 0; opacity: 1; text-shadow: 0 1px 3px rgba(0,0,0,0.25); }

    /* Metric containers */
    .metric-container { background: #ffffff; border-radius: 12px; padding: 16px; margin: 12px 0; border: 1px solid #e5e7eb; }

    /* Streamlit metric - gradient pill style readable on dark */
    .stMetric { background: transparent; padding: 0; }
    .stMetric [data-testid="metric-container"] { 
        background: linear-gradient(135deg, rgba(99,102,241,0.95) 0%, rgba(139,92,246,0.95) 100%);
        color: #ffffff !important; padding: 20px; border-radius: 16px; text-align: center; border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }
    .stMetric [data-testid="metric-container"] * { color: #ffffff !important; text-shadow: 0 1px 3px rgba(0,0,0,0.35) !important; }

    /* Buttons */
    .stButton > button { background: #1f2937 !important; color: #ffffff !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 10px; padding: 10px 20px; font-weight: 700; }
    .stButton > button:hover { filter: brightness(1.12); }

    /* Inputs */
    .stTextInput > div > div > input, .stNumberInput > div > div > input, .stSelectbox > div > div > select {
        border-radius: 10px; border: 1px solid #e5e7eb; background-color: #ffffff !important; color: #111827 !important; font-size: 16px !important; padding: 12px !important;
    }
    .stTextInput > div > div > input:focus, .stNumberInput > div > div > input:focus, .stSelectbox > div > div > select:focus {
        border-color: #111827; box-shadow: 0 0 0 3px rgba(17,24,39,0.08);
    }
    .stTextInput > div > div > input::placeholder { color: #6b7280 !important; opacity: 1 !important; }
    .stTextInput input[type="text"] { color: #111827 !important; background-color: #ffffff !important; }
    .stTextInput[data-testid="textInput"] input { color: #111827 !important; background-color: #ffffff !important; border: 1px solid #e5e7eb !important; }
    .stTextInput[data-testid="textInput"] input:focus { border-color: #111827 !important; }

    /* Messages */
    .stSuccess { background: #ecfdf5; border: 1px solid #10b981; border-radius: 10px; color: #065f46; }
    .stError { background: #fef2f2; border: 1px solid #ef4444; border-radius: 10px; color: #7f1d1d; }
    .stWarning { background: #fffbeb; border: 1px solid #f59e0b; border-radius: 10px; color: #78350f; }
    .stInfo { background: #eff6ff; border: 1px solid #3b82f6; border-radius: 10px; color: #1e3a8a; }

    .dataframe { border-radius: 10px; overflow: hidden; border: 1px solid rgba(255,255,255,0.08); }

    /* Ensure general text is light */
    .stMarkdown, .stText, .stDataFrame, .stTable, .stExpander, .stContainer, .stColumn, .stTabs, .stSidebar { color: #e5e7eb !important; }
</style>
""", unsafe_allow_html=True)

# Beautiful header
st.markdown("""
<div class="main-header">
    <h1>💰 Smart Expense Visualizer</h1>
    <p>Your Personal Finance Dashboard with AI-Powered Insights</p>
</div>
""", unsafe_allow_html=True)

# Load data
data = load_data()

# Display quick stats
if not data.empty:
    total_expenses = data['Amount'].sum()
    total_transactions = len(data)
    avg_expense = data['Amount'].mean()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💰 Total Expenses", f"₹{total_expenses:,.0f}")
    
    with col2:
        st.metric("📊 Transactions", f"{total_transactions}")
    
    with col3:
        st.metric("📈 Average per Transaction", f"₹{avg_expense:,.0f}")
    
    with col4:
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
            active_days = len(data['Date'].dt.date.unique())
            st.metric("📅 Active Days", f"{active_days}")
        else:
            st.metric("📅 Active Days", "N/A")

# Sidebar
sidebar()

# Main tabs with beautiful styling
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📅 Calendar View", 
    "📊 Charts & Analytics", 
    "🧠 Smart Insights", 
    "🛠 Add/Edit Expenses", 
    "📤 Export & Reports",
    "🤖 AI Chatbot"
])

with tab1:
    calendar_view(data)

with tab2:
    charts_view(data)

with tab3:
    insights_view(data)
    detect_recurring_expenses(data)
    check_budget_alerts(data)

with tab4:
    voice_to_text_input()
    add_expense()

with tab5:
    export_data(data)
    show_monthly_comparison(data)

with tab6:
    chatbot_tab()
