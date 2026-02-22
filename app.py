import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide", page_title="AI Automation Dashboard")

# ---------------- SESSION STATE INIT ----------------
if "sales_data" not in st.session_state:
    st.session_state["sales_data"] = pd.DataFrame({
        "Product": ["Laptop", "Mobile", "Tablet", "TV"],
        "Sales": [120, 300, 150, 80]
    })

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ff0080, #ff0000, #0000ff);
    background-attachment: fixed;
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ff4d6d, #845ec2);
}

.glass-card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 0px 20px rgba(255,255,255,0.2);
    margin-bottom: 20px;
}

.title-box {
    background: rgba(0,0,0,0.4);
    padding: 20px;
    border-radius: 20px;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🤖 AI Dashboard")
page = st.sidebar.radio("Navigation", ["Home", "Admin", "User", "Settings"])

# ========================= HOME =========================
if page == "Home":

    st.markdown('<div class="title-box">🚀 AI Automation Dashboard</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="glass-card">👤 Users<br><h2>120</h2></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">💰 Revenue<br><h2>₹2,50,000</h2></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="glass-card">🤖 AI Requests<br><h2>980</h2></div>', unsafe_allow_html=True)

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("### 📊 Sales Table")
        st.dataframe(
            st.session_state["sales_data"],
            use_container_width=True,
            height=450
        )

    with col5:
        st.markdown("### 📈 Sales Chart")
        st.bar_chart(
            st.session_state["sales_data"].set_index("Product"),
            use_container_width=True,
            height=450
        )

# ========================= ADMIN =========================
elif page == "Admin":

    st.markdown('<div class="title-box">🛠 Admin Panel</div>', unsafe_allow_html=True)

    # ----- Data Overview -----
    st.markdown("### 📊 Data Overview")
    st.write("Total Products:", len(st.session_state["sales_data"]))
    st.write("Total Sales:", st.session_state["sales_data"]["Sales"].sum())

    st.divider()

    # ----- Add Product Section -----
    st.markdown("### ➕ Add New Product")

    col1, col2, col3 = st.columns([3,3,2])

    with col1:
        product_name = st.text_input("Product Name")

    with col2:
        product_sales = st.number_input("Sales Value", min_value=0.0)

    with col3:
        st.write("")
        st.write("")
        if st.button("Add Product"):
            if product_name.strip() != "":
                new_row = pd.DataFrame(
                    [[product_name, product_sales]],
                    columns=["Product", "Sales"]
                )
                st.session_state["sales_data"] = pd.concat(
                    [st.session_state["sales_data"], new_row],
                    ignore_index=True
                )
                st.success("Product Added Successfully!")
                st.rerun()
            else:
                st.warning("Please enter product name")

    st.divider()

    # ----- Clear Data -----
    if st.button("🗑 Clear All Data"):
        st.session_state["sales_data"] = pd.DataFrame(columns=["Product", "Sales"])
        st.success("All data cleared!")
        st.rerun()

# ========================= USER =========================
elif page == "User":

    st.markdown('<div class="title-box">👤 User Dashboard</div>', unsafe_allow_html=True)

    st.dataframe(
        st.session_state["sales_data"],
        use_container_width=True,
        height=500
    )

# ========================= SETTINGS =========================
elif page == "Settings":

    st.markdown('<div class="title-box">⚙ Settings</div>', unsafe_allow_html=True)

    theme = st.selectbox("Select Theme Mode", ["Default", "Dark", "Light"])
    notifications = st.toggle("Enable Notifications")

    st.write("Theme:", theme)
    st.write("Notifications Enabled:", notifications)