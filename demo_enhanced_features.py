#!/usr/bin/env python3
"""
Demo script to showcase the enhanced features of Smart Expense Visualizer
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

def create_demo_data():
    """Create sample data for demonstration"""
    np.random.seed(42)
    
    # Generate sample expense data
    categories = ['Food', 'Travel', 'Shopping', 'Entertainment', 'Utilities', 'Health', 'Education', 'Other']
    dates = pd.date_range(start='2025-07-01', end='2025-08-10', freq='D')
    
    data = []
    for date in dates:
        # Randomly decide if there are expenses on this day (70% chance)
        if np.random.random() > 0.3:
            # 1-3 expenses per day
            num_expenses = np.random.randint(1, 4)
            for _ in range(num_expenses):
                category = np.random.choice(categories)
                amount = np.random.exponential(200)  # Exponential distribution for realistic amounts
                amount = min(amount, 5000)  # Cap at 5000
                
                notes = [
                    f"Expense on {category.lower()}",
                    f"Purchase at {category.lower()} store",
                    f"Payment for {category.lower()}",
                    ""
                ]
                note = np.random.choice(notes)
                
                data.append({
                    'Date': date.strftime('%Y-%m-%d'),
                    'Category': category,
                    'Amount': round(amount, 2),
                    'Note': note
                })
    
    return pd.DataFrame(data)

def demo_enhanced_features():
    """Demonstrate the enhanced features"""
    
    st.set_page_config(
        page_title="Smart Expense Visualizer - Demo",
        page_icon="💰",
        layout="wide"
    )
    
    # Beautiful header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    ">
        <h1 style="font-size: 3em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            💰 Smart Expense Visualizer
        </h1>
        <p style="font-size: 1.2em; margin: 10px 0 0 0; opacity: 0.9;">
            Enhanced with Beautiful UI, Interactive Charts & AI-Powered Insights
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create demo data
    data = create_demo_data()
    
    st.markdown("## 🎨 Enhanced Features Demo")
    
    # Key improvements
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin: 10px 0;
            box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
        ">
            <h3>🎨 Beautiful UI</h3>
            <p>Modern gradients, animations, and responsive design</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin: 10px 0;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        ">
            <h3>📊 Interactive Charts</h3>
            <p>Plotly-powered charts with hover effects and animations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #1abc9c, #16a085);
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin: 10px 0;
            box-shadow: 0 4px 15px rgba(26, 188, 156, 0.3);
        ">
            <h3>🧠 Smart Insights</h3>
            <p>AI-powered analytics and spending recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Demo data stats
    st.markdown("### 📊 Demo Data Overview")
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
        active_days = len(data['Date'].unique())
        st.metric("📅 Active Days", f"{active_days}")
    
    # Beautiful charts demo
    st.markdown("### 📊 Interactive Charts Demo")
    
    # Category distribution pie chart
    category_totals = data.groupby('Category')['Amount'].sum()
    
    fig_pie = px.pie(
        values=category_totals.values,
        names=category_totals.index,
        title="Spending by Category",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig_pie.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Amount: ₹%{value:,.0f}<br>Percentage: %{percent}<extra></extra>'
    )
    
    fig_pie.update_layout(
        title_font_size=20,
        title_x=0.5,
        font=dict(size=14),
        height=400
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Daily spending trend
    data['Date'] = pd.to_datetime(data['Date'])
    daily_totals = data.groupby(data['Date'].dt.date)['Amount'].sum().reset_index()
    
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=daily_totals['Date'],
        y=daily_totals['Amount'],
        mode='lines+markers',
        name='Daily Spending',
        line=dict(width=3, color='#667eea'),
        marker=dict(size=8, color='#ff6b6b'),
        fill='tonexty',
        fillcolor='rgba(102, 126, 234, 0.1)'
    ))
    
    fig_line.update_layout(
        title="Daily Spending Trend",
        title_font_size=20,
        title_x=0.5,
        xaxis_title="Date",
        yaxis_title="Amount (₹)",
        font=dict(size=14),
        hovermode='x unified',
        height=400
    )
    
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Enhanced features list
    st.markdown("### ✨ Key Enhancements")
    
    features = [
        "🎨 **Modern UI Design**: Beautiful gradients, animations, and responsive layout",
        "📊 **Interactive Charts**: Plotly-powered charts with hover effects and zoom",
        "🧠 **Smart Analytics**: AI-powered insights and spending recommendations",
        "📱 **Mobile Responsive**: Works perfectly on all device sizes",
        "🎯 **Color-Coded Categories**: Visual category identification with custom colors",
        "📈 **Trend Analysis**: Daily, weekly, and monthly spending patterns",
        "💡 **Smart Alerts**: Spending warnings and budget recommendations",
        "🎭 **Smooth Animations**: Hover effects and transitions throughout",
        "📊 **Enhanced Metrics**: Comprehensive statistics and KPIs",
        "🎨 **Beautiful Cards**: Modern card-based layout for better organization"
    ]
    
    for feature in features:
        st.markdown(f"• {feature}")
    
    st.markdown("### 🚀 Ready to Experience the Full App?")
    st.markdown("Run `streamlit run app.py` to see all the enhanced features in action!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 30px;">
        <p>💰 Smart Expense Visualizer - Enhanced with Beautiful UI & AI-Powered Insights</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    demo_enhanced_features()
