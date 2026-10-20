import streamlit as st


st.title("~ Books by Vibe ~")
vibe = st.text_input("What's your vibe?")
st.session_state["vibe"] = vibe

if st.session_state["vibe"] != "":
    st.write("Searching for books...")
    st.write(f"Match vibe: {vibe}")
