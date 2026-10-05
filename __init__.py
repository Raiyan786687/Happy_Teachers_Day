import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Special Tribute to Miss Kausar | Happy Teacher's Day",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom HTML/CSS/JS Styling inside Streamlit
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
        * { font-family: 'Poppins', sans-serif; }
        
        .main { background-color: #050b14; color: #f8fafc; }

        /* Banner */
        .header-banner {
            background: linear-gradient(135deg, #1e1b4b, #0f172a);
            border: 1px solid rgba(168, 85, 247, 0.3);
            text-align: center; padding: 40px; border-radius: 24px;
            margin-bottom: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .header-banner h2 { font-size: 36px; color: #c084fc; margin-bottom: 10px; font-weight: 800; }
        .header-banner p { color: #94a3b8; font-size: 18px; }

        /* Chemistry Card */
        .chem-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(168, 85, 247, 0.2);
            border-left: 8px solid #a855f7;
            border-radius: 24px; padding: 40px;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        }
        .badge {
            background: rgba(168, 85, 247, 0.15); border: 1px solid #a855f7;
            padding: 8px 20px; border-radius: 20px; font-size: 14px; color: #e9d5ff;
            display: inline-block; margin-bottom: 25px; font-weight: 600;
        }
        
        /* Chemical Diagram Box */
        .lab-box {
            background: rgba(15, 23, 42, 0.9);
            border: 2px dashed rgba(168, 85, 247, 0.5);
            border-radius: 20px; padding: 30px; text-align: center; height: 100%;
            display: flex; flex-direction: column; justify-content: center;
        }
        .formula {
            font-size: 26px; font-weight: 800; color: #c084fc; margin-bottom: 15px;
            letter-spacing: 1px;
        }
        .quote {
            font-size: 14px; color: #94a3b8; font-style: italic; line-height: 1.6;
        }

        /* Favourite Teacher Highlight Banner */
        .favourite-banner {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(56, 189, 248, 0.2));
            border: 2px solid #a855f7;
            text-align: center; padding: 25px; border-radius: 20px;
            margin-top: 40px; box-shadow: 0 10px 30px rgba(168, 85, 247, 0.25);
        }
        .favourite-banner h3 {
            font-size: 28px; font-weight: 800;
            background: linear-gradient(to right, #c084fc, #38bdf8);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Session State for Surprise Reveal
if "kausar_surprise_open" not in st.session_state:
    st.session_state.kausar_surprise_open = False

# ----------------- SURPRISE INTRO SCREEN -----------------
if not st.session_state.kausar_surprise_open:
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 75vh; text-align: center; padding: 20px;">
            <div style="background: rgba(255, 255, 255, 0.04); border: 2px solid #a855f7; padding: 50px 40px; border-radius: 30px; box-shadow: 0 15px 50px rgba(168, 85, 247, 0.3); backdrop-filter: blur(20px); max-width: 650px; width: 100%;">
                <h1 style="font-size: 38px; margin-bottom: 20px; font-weight: 800; background: linear-gradient(to right, #c084fc, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🧪 Special Chemistry Tribute!</h1>
                <p style="font-size: 18px; color: #cbd5e1; margin-bottom: 35px; line-height: 1.6;">Respected Miss Kausar, a wonderful Teacher's Day surprise crafted exclusively for you with 💙 and code by your student, <b>Rayyan</b>.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎁 Click to Open Surprise", use_container_width=True, type="primary"):
            st.session_state.kausar_surprise_open = True
            st.rerun()

# ----------------- MAIN WEBSITE CONTENT FOR MISS KAUSAR -----------------
else:
    st.markdown("""
        <div class="header-banner">
            <h2>Happy Teacher's Day, Miss Kausar! 🌸</h2>
            <p>To the brilliant mentor who makes chemistry come alive in the classroom.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="chem-card">
            <span class="badge">🧪 H₂O of Wisdom & Ultimate Catalyst of Success</span>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 0.8])
    
    with col1:
        st.markdown("""
            <p style="color: #cbd5e1; font-size: 17px; line-height: 1.9; margin-bottom: 20px;">
            Respected Miss Kausar, your presence in our classroom acts like a perfect positive catalyst—accelerating our minds toward greatness and making difficult concepts click instantly without ever exhausting your patience!</p>
            <p style="color: #cbd5e1; font-size: 17px; line-height: 1.9; margin-bottom: 20px;">
            You have a rare gift for turning complex chemical equations, periodic tables, and atomic structures into pure, fascinating stories. Even when formulas get complicated, your clear explanations dissolve all confusion faster than a neutralization reaction.</p>
            <p style="color: #cbd5e1; font-size: 17px; line-height: 1.9; margin-bottom: 20px;">
            Thank you for sparking our curiosity, believing in our potential, and teaching us how elements bond together to create incredible things. We are truly lucky to have you as our chemistry mentor!</p>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="lab-box">
                <div class="formula">C₁₂H₂₂O₁₁ + H₂O</div>
                <div style="font-size: 13px; color: #38bdf8; margin-bottom: 15px; font-weight: 600;">(Pure Sweetness + Infinite Dedication)</div>
                <p class="quote">"Education is not just filling a pail, but lighting a permanent flame—and you have lit a blazing fire of science in our hearts!"</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Special Favourite Teacher Highlight Section
    st.markdown("""
        <div class="favourite-banner">
            <h3>⭐ Miss Kausar, You are my Favourite teacher! 💙</h3>
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #64748b; margin-top: 20px;'>© 2026 Teacher's Day Tribute. Designed with 💙 by Rayyan specifically for Miss Kausar.</p>", unsafe_allow_html=True)