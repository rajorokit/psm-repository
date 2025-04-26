import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength by Tahira shoaib", page_icon="🌖", layout="centered")

# Custom CSS
st.markdown("""
<style>
.main {text-align:center}
.stTextInput {width: 60% !important; margin: auto;}
.stButton button {width: 50%; background-color: #4CAF50; color: white; font-size:18px; }
.stButton button:hover { background-color: #45a049}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Upper and lowercase letters check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **uppercase (A-Z) and lowercase (a-z) letters**.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    return score, feedback

# Input field
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

# Button
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Display result
        if score == 4:
            st.success("✅ **Strong Password** - Your password is secure.")
        elif score == 3:
            st.info("⚠️ **Moderate Password** - Consider improving it by adding more features.")
        else:
            st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

        # Display feedback
        if feedback:
            with st.expander("🔍 **Improve Your Password**"):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠️ Please enter a password first!")
