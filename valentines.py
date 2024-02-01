import streamlit as st

def valentine_proposal():
    st.title("Valentine's Day Proposal 💖")

    text_message = """
    As we celebrate four incredible years together, I find myself more in love with you each day.
    Your laughter is my favorite melody, and your presence, my greatest comfort.
    """

    # Display the text without scrolling
    st.markdown(f"<p style='font-size: 18px; line-height: 1.6;'>{text_message}</p>", unsafe_allow_html=True)

    # Display the yes/no radio buttons without a default choice
    choice = st.radio("Will you be my Valentine this year?", ("Yes", "No"), index=None)

    # Display appropriate message based on the choice
    if choice == "Yes":
        st.success("🌹🥰 Yess! Thanks for making me the luckiest guy. I want to enjoy every moment with you 🥰🌹")
    elif choice == "No":
        st.error("❌ This option is not allowed. Please reconsider! ❤️")

if __name__ == "__main__":
    valentine_proposal()
